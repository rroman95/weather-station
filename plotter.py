import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import bme280_output

plt.style.use('fivethirtyeight')

x_vals = []
y1 = []
y2 = []

humidity, pressure, ambient_temperature = bme280_output.read_all()

index = count()

def animate(i):
    humidity, pressure, ambient_temperature = bme280_output.read_all()
    x_vals.append(next(index))
    y1.append(ambient_temperature)
    y2.append(humidity)
    plt.cla()
    plt.plot(x_vals,y1, label = 'Temperature')
    plt.plot(x_vals,y2, label = 'Humidity')
    plt.legend (loc='upper left')

ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()
