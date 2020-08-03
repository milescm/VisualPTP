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
    

    return render(request, 'myapp/readcsv.html')

def deletedata(request):
    Csvdata.objects.all().delete()
    return render(request, 'myapp/deletedata.html')