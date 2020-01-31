from pushbullet import Pushbullet
import bme280_output
from datetime import date
import datetime
import os

def sendtophone():
    dir = r"/home/pi/weather-station/data/"
    filename = str(date.today())

    humidity, pressure, ambient_temperature = bme280_output.read_all()
    temperature = round(ambient_temperature,2)
    humidity = round(humidity,2)
    tempdata = str(temperature)
    humdata = str(humidity)
    pb = Pushbullet('o.SpLVyGfhBJGKv9E8UxPs7sWsO7kyzcwi')

    with open(os.path.join(dir,filename+'.png'),"rb") as pic:
                file_data = pb.upload_file(pic, "test.png")
                
    push = pb.push_note("Raspberry Pi","°C :"+ tempdata+ "     Humidity: " + humdata +"%")        
    push = pb.push_file(**file_data)        

sendtophone()
