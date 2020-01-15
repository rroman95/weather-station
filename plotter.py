import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import bme280_output

plt.style.use('fivethirtyeight')

x = []
y1 = []
y2 = []

humidity, pressure, ambient_temperature = bme280_output.read_all()

index = count()

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['Time']
    y1 = data['Temperature']
    y2 = data['Humidity']
    plt.cla()
    plt.plot(x,y1, label = 'Temperature')
    plt.plot(x,y2, label = 'Humidity')
    plt.legend (loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()

