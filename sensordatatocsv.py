#!/bin/env python3
import csv
import time
import os.path
import bme280_output
import ds18b20_therm
from datetime import datetime
from datetime import date
import datetime

dir = r"/home/pi/weather-station/data/"
fieldnames = ["Time", "Temp","Grnd.Temp", "Humidity","Pressure",
              "Avg.Temp","Avg.Humidity","Avg.Pressure","Min.Temp","Max.Temp"]
while True:
    
    
    Time = 0
    Temperature= 0
    Humidity = 0
    Bar = 0
    ground_temp = 0
    all_temperature = 0
    all_humidity = 0
    all_bar = 0
    avg_temperature = 0
    avg_humidity = 0
    avg_bar = 0
    max_temp = 0
    min_temp = 0
    NumberOfIterations = 1
    temp_probe = ds18b20_therm.DS18B20()
    filename = str(date.today())
    print ("reset timer and values")
    humidity, pressure, ambient_temperature = bme280_output.read_all()
    min_temp = ambient_temperature
    max_temp = ambient_temperature   
    with open(os.path.join(dir,filename+'.csv'), 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    now = datetime.datetime.now()
    endtime = now.replace(hour = 23, minute = 59, second = 0, microsecond= 0)

    while (now < endtime):

        with open(os.path.join(dir,filename+'.csv'), 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            humidity, pressure, ambient_temperature = bme280_output.read_all()
            ground_temp = temp_probe.read_temp()
            current_time = now.strftime("%H:%M:%S")
            Bar = pressure / 1000
            
            if (ambient_temperature > max_temp):
                max_temp = ambient_temperature
            if (ambient_temperature < min_temp):
                min_temp = ambient_temperature
            
            all_temperature += ambient_temperature
            all_humidity += humidity
            all_bar += Bar
            
            avg_temperature = all_temperature / NumberOfIterations
            avg_humidity = all_humidity / NumberOfIterations
            avg_bar = all_bar / NumberOfIterations
            
            info = {
                "Time": current_time,
                "Temp": round(ambient_temperature,2),
                "Grnd.Temp": round(ground_temp,2),
                "Humidity": round(humidity,2),
                "Pressure": round(Bar,2),
                "Avg.Temp": round(avg_temperature,2),
                "Avg.Humidity": round(avg_humidity,2),
                "Avg.Pressure": round(avg_bar, 2),
                "Min.Temp": round(min_temp, 2),
                "Max.Temp": round (max_temp, 2)                
            }

            csv_writer.writerow(info)
            print(current_time,round(ambient_temperature,2),round(ground_temp,2), round(humidity,2),round (Bar,2))

            
            time.sleep(3600)
            NumberOfIterations += 1
            now = datetime.datetime.now()   
    time.sleep(90)
