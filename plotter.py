import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import bme280_output
import os.path
from datetime import date

plt.style.use('fivethirtyeight')

x = []
y1 = []
y2 = []

humidity, pressure, ambient_temperature = bme280_output.read_all()

index = count()
dir = r"/home/pi/weather-station/data/"
filename = str(date.today())

def animate(i):
    data = pd.read_csv(os.path.join(dir,filename+'.csv'))
    x = data['Time']
    y1 = data['Temperature']
    y2 = data['Humidity']
    plt.cla()
    plt.plot(x,y1, label = 'Temperature')
    plt.plot(x,y2, label = 'Humidity')
    plt.xticks(rotation=90)
    plt.legend (loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

