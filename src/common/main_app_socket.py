from . import config
import socket
import pickle
import time

class SensorData:
  temperature = 0
  humidity = 0

class MainAppPacket:
  sensor_data = None

def connect(on_sensor_data):

  while True:
    try:

      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", config.MAIN_APP_PORT))
        print('Connected to main app')

        while True:
          data = s.recv(4096)
          if not data:
            print('Disconnected from main app')
            time.sleep(1)
            break
          packet = pickle.loads(data)
          if packet.sensor_data is not None:
            on_sensor_data(packet.sensor_data)
        
    except Exception:
      time.sleep(1)
