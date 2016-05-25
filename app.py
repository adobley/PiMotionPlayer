import subprocess
import RPi.GPIO as GPIO
import time
import os
import random

video_player = 'omxplayer'
media_folder = 'media/'
files = os.listdir(media_folder)

sensor_port = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_port, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
  time.sleep(0.1)
  previous_state = current_state
  current_state = GPIO.input(sensor_port)
  if current_state != previous_state:
    if current_state:
      file = random.choice(files)
      file_path = media_folder + file
      subprocess.call([video_player, file_path])
