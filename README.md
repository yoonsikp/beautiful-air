# beautiful-air
An easy way to collect and display data about the air we breathe.
This project relies on HighCharts to display the data that we generate.


![Alt text](/screenshot.jpg?raw=true "Screenshot")

## Installation
You need Python 3. Run `python3 collect.py` either through linux/cron, or use a watch command as follows:
```
watch -n 60 python3 ~/beautiful-air/collect.py
```

You need any web server to host the csv files, as well as the index.html. A simple Python web server can be started as follows:

```
cd ./beautiful-air/
python3 -m http.server 8080
```

Both can be integrated into `/etc/rc.local` so that the scripts will run on boot. I add a twist by running each command in a `screen`, a virtual terminal that allows reconnection:

```
su -c "cd ~/beautiful-air/ && screen -dmS miniserver python3 -m http.server 8080" -s /bin/sh pi
su -c "cd ~/beautiful-air/ && screen -dmS collect watch -n 60 python3 ~/beautiful-air/collect.py" -s /bin/sh pi
#      directory of csv/html.          friendly name   update interval     path to collect.py             username
```
