from django.shortcuts import render
import random
from .models import Csvdata
import csv
import pandas as pd

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
