import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename='death_valley_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)#数据时从第二行开始的。。。惊了
#    for index,column_header in enumerate(header_row):
#        print(index,column_header)
    highs,lows=[],[]
    dates=[]
    for row in reader:
        try:
            current_date=datetime.strptime(row[0],'%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            continue
            #print(current_date,'missingdata')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
print(dates)
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)#alpha透明度
#传递一个x值系列，两个y值系列
plt.title('daily high,low tem 2014',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#斜的日期标签
plt.ylabel('tem(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()