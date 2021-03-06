#!/bin/env python3
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import bme280_output
import os.path
from datetime import date
import datetime
import time

plt.style.use('fivethirtyeight')

x = []
y1 = []
y2 = []
y3 = []
y4 = []
min_temp = []
max_temp = []
avg_temperature = []

now = datetime.datetime.now()
endtime = now.replace(hour=23, minute=59,second = 45, microsecond= 0)

dir = r"/home/pi/weather-station/data/"
filename = str(date.today())

def animate(i):
    now = datetime.datetime.now()
    endtime = now.replace(hour=23, minute=59,second = 0, microsecond= 0)
    filename = str(date.today())
    if (now>endtime):
        print ('sleep')
        time.sleep(100)
    data = pd.read_csv(os.path.join(dir,filename+'.csv'))
    x = data['Time']
    y1 = data['Temp']
    y2 = data['Humidity']
    y3 = data['Pressure']
    y4 = data['Grnd.Temp']
    min_temp = data['Min.Temp']
    max_temp = data['Max.Temp']
    avg_temperature = data['Avg.Temp']
    plt.cla()
    plt.plot(x,y1, label = 'Temperature',color = 'red')
    plt.plot(x,y2, label = 'Humidity', color = 'cyan')
    plt.plot(x,y3, label = 'Bar', color = 'green')
    plt.plot(x,y4, 'g--',label = 'Grnd.Temp', color = 'crimson')
    plt.xticks(rotation=90)
    plt.legend (loc='upper left')
    plt.tight_layout()
    plt.savefig('/home/pi/weather-station/data/'+filename+'.png')



ani = FuncAnimation(plt.gcf(), animate, interval=1800)
plt.tight_layout()
plt.show()


