#/usr/bin/python3
# https://www.delftstack.com/howto/python/python-play-mp3/
# https://schedule.readthedocs.io/en/stable/
import os
import sys
import random
import glob
import schedule
import time
from termux import API as api

# from datetime import datetime, timedelta, time

#path=os.getcwd() + r'/*.MP3'
#def hello_world:
#	print("Hello World")

def play_mp3():
    path=os.getcwd() + r'/sounds/*.??3'
    files = glob.glob(path)
    d=random.choice(files)
    #os.startfile(d)
    # cmd = "afplay '" + d +"'"
    cmd = "termux-media-player play '" + d +"'"
    print(cmd)
    os.system(cmd)
    # api.generic(cmd)
if len(sys.argv)>1:
    timee = str(sys.argv[1])
else:
    timee = r'23:00'

# Run every 5 to 10 seconds.

schedule.every(1).to(4).seconds.until(timee).do(play_mp3)

# play_mp3()
# files=os.listdir(path)
# while True:
#    schedule.run_pending()
#    time.sleep(1)

while 1:
    n = schedule.idle_seconds()
    if n is None:
        # no more jobs
        break
    elif n > 0:
        # sleep exactly the right amount of time
        print(F'Wait {n} seconds')
        time.sleep(n)
    schedule.run_pending()
