import ntplib
import time
import urllib.request
tfile = open('temperature.csv', 'a')
hfile = open('humidity.csv', 'a')
p1file = open('pm1.csv', 'a')
p2file = open('pm2.csv', 'a')
p10file = open('pm10.csv', 'a')
with urllib.request.urlopen('http://sensor:8080/humidity') as response:
    humidity = float(response.read())
with urllib.request.urlopen('http://sensor:8080/temperature') as response:
    temperature = float(response.read())
with urllib.request.urlopen('http://sensor:8081/pm1') as response:
    pm1 = int(response.read())
with urllib.request.urlopen('http://sensor:8081/pm2') as response:
    pm2 = int(response.read())
with urllib.request.urlopen('http://sensor:8081/pm10') as response:
    pm10 = int(response.read())

epoc=int(time.time())
tfile.write(str(epoc)+'000,' + str(temperature) + '\n')
hfile.write(str(epoc)+'000,' + str(humidity) + '\n')
if pm1 != -1:
    p1file.write(str(epoc)+'000,' + str(pm1) + '\n')
    p2file.write(str(epoc)+'000,' + str(pm2) + '\n')
    p10file.write(str(epoc)+'000,' + str(pm10) + '\n')
print(humidity,temperature,pm1,pm2,pm10)

