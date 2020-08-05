#!/usr/bin/env python
# coding: utf-8

# myapp/mycron.py


from .models import Csvdata
import csv
import pandas as pd





def delete_read_csv(self):
    # self.stdout.write('Reset Database ...')
    Csvdata.objects.all().delete()
    with open('/home/rtst15/Django_PTP_visual/f_csv/ptpTime30min_1.csv', 'r') as f:
        dr = csv.DictReader(f)
        s = pd.DataFrame(dr)
    ss = []
    for i in range(len(s)):
        st = (s['__REALTIME_TIMESTAMP'][i], s['UTC'][i],s['Master Offset'][i],s['Frequency'][i],s['Path Delay'][i])
        ss.append(st)
    for i in range(len(s)):
        Csvdata.objects.create(realtime_timestamp=ss[i][0], utc=ss[i][1], master_offset=ss[i][2], frequency=ss[i][3], path_delay=ss[i][4])

    # self.stdout.write(self.style.SUCCESS('Reset Database complete.'))


