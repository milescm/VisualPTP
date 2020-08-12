from django.shortcuts import render, redirect
from .models import Csvdata
import csv, io, os
from django.http import HttpResponse, Http404
from myproject.settings import STATIC_ROOT

def home(request):
    return render(request, 'myapp/home.html')

def showdata(request):
    csv = Csvdata.objects.all()
    
    realtime_timestamp = []
    utc = []
    master_offset = []
    frequency = []
    path_delay = []

    count = 0
    for row in csv.values_list():
        if(count>10):
            break
        else:
            realtime_timestamp.append(row[1])
            utc.append(row[2])
            master_offset.append(row[3])
            frequency.append(row[4])
            path_delay.append(row[5])
        count+=1
        
    return render(request, 'myapp/showdata.html', 
    {'realtime_timestamp': realtime_timestamp,
        'utc': utc,
        'master_offset': master_offset,
        'frequency': frequency,
        'path_delay': path_delay,
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
        text = "The Data already exits!"
        return render(request, 'myapp/error.html', {'text': text})
    else:
        if request.FILES.__len__()==0:
            text = "No uplaod file"
            return render(request, 'myapp/error.html', {'text': text})
        else:
            uploadFile = request.FILES['file']
            if uploadFile.name.find('csv')<0:
                text = "This file is not csv file"
                return render(request, 'myapp/error.html', {'text': text})
            else:
                read = uploadFile.read().decode('utf8')
                readLine = read.split('\n')

                tmp_str = []

                       
                for line in readLine:
                    tmp_str.append(line.split(','))
                
                for i in range(1,len(tmp_str)-1):
                    Csvdata.objects.create(realtime_timestamp=tmp_str[i][1], utc=tmp_str[i][2],master_offset=tmp_str[i][3],frequency=tmp_str[i][4],path_delay=tmp_str[i][5])
               
           
                return render(request, 'myapp/filecheck.html')



def downloadcsv(request):
    file_path = os.path.join(STATIC_ROOT, 'testfile.csv')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-Excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
