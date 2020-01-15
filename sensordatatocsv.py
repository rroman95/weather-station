import csv
import random
import time
import bme280_output
from datetime import datetime


Time = 0
Temperature= 0
Humidity = 0


fieldnames = ["Time", "Temperature", "Humidity"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        humidity, pressure, ambient_temperature = bme280_output.read_all()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        info = {
            "Time": current_time,
            "Temperature": round(ambient_temperature,2),
            "Humidity": round(humidity,2)
        }

        csv_writer.writerow(info)
        print(current_time,round(ambient_temperature,2), round(humidity,2))

        
        

    time.sleep(1)
