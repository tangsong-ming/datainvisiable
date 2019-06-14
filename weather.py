import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename='sitka_weather_07-2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
#    for index,column_header in enumerate(header_row):
#        print(index,column_header)
    highs=[]
    dates=[]
    for row in reader:
        current_date=datetime.strptime(row[0],'%Y/%m/%d')
        print(current_date)
        dates.append(current_date)
        high=int(row[1])
        highs.append(high)
print(dates)
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.title('daily high tem,7 2014',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#斜的日期标签
plt.ylabel('tem(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()