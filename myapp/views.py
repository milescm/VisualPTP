from django.shortcuts import render, redirect
import random
from .models import Csvdata
import csv, io
import pandas as pd
from django.db import IntegrityError
from django.http import JsonResponse
from django.contrib import messages


def home(request):
    return render(request, 'myapp/home.html')

def showdata(request):
    csv = Csvdata.objects.all()
    
    realtime_timestamp = []
    utc = []
    master_offset = []
    frequency = []
    path_delay = []

    for row in csv.values_list():
        realtime_timestamp.append(row[1])
        utc.append(row[2])
        master_offset.append(row[3])
        frequency.append(row[4])
        path_delay.append(row[5])

    return render(request, 'myapp/showdata.html', 
    {'realtime_timestamp': realtime_timestamp,
        'utc': utc,
        'master_offset': master_offset,
        'frequency': frequency,
        'path_delay': path_delay,
    })



def readcsv(request):
    text = "The Data already exits!"
    if Csvdata.objects.count() != 0:
        return render(request, 'myapp/error.html', {'text': text})

    else:
        with open('/home/rtst15/Django_PTP_visual/f_csv/ptpTime30min_1.csv', 'r') as f:
            dr = csv.DictReader(f)
            s = pd.DataFrame(dr)
        ss = []
        for i in range(len(s)):
            st = (s['__REALTIME_TIMESTAMP'][i], s['UTC'][i],s['Master Offset'][i],s['Frequency'][i],s['Path Delay'][i])
            ss.append(st)
        for i in range(len(s)):
            Csvdata.objects.create(realtime_timestamp=ss[i][0], utc=ss[i][1], master_offset=ss[i][2], frequency=ss[i][3], path_delay=ss[i][4])

        data = Csvdata.objects.all().values()
        return render(request, 'myapp/readcsv.html', {
            'data': data
                })
    
def deletedata(request):
    Csvdata.objects.all().delete()
    return render(request, 'myapp/deletedata.html')

def showgraph(request):
    csv = Csvdata.objects.all()
    offset = []
    timestamp = []
    for row in csv.values_list():
        timestamp.append(row[1])
        offset.append(row[3])

    return render(request, 'myapp/showgraph.html', {
        'offset': offset,
        'timestamp': timestamp
    })


def showstock(request):
    csv = Csvdata.objects.all()
    offset = []
    timestamp = []
    for row in csv.values_list():
        timestamp.append(row[1])
        offset.append(row[3])

    return render(request, 'myapp/showstock.html', {
        'offset': offset,
        'timestamp': timestamp
    })

def userform(request):
    return render(request, 'myapp/userform.html')

def filecheck(request):
    if Csvdata.objects.count() != 0:
        message = "The Data already exits!"
        return JsonResponse({"message": message})
    else:
        if request.FILES.__len__()==0:
            message = "No uplaod file"
            return JsonResponse({"message": message})
        else:
            uploadFile = request.FILES['file']
            if uploadFile.name.find('csv')<0:
                message = "This file is not csv file"
                return JsonResponse({"message": message})
            else:
                read = uploadFile.read().decode('utf8')
                readLine = read.split('\n')

                tmp_str = []

                       
                for line in readLine:
                    tmp_str.append(line.split(','))
                
                for i in range(1,len(tmp_str)-1):
                    Csvdata.objects.create(realtime_timestamp=tmp_str[i][1], utc=tmp_str[i][2],master_offset=tmp_str[i][3],frequency=tmp_str[i][4],path_delay=tmp_str[i][5])
               
           
                return render(request, 'myapp/filecheck.html')



