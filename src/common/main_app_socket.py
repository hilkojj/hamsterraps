from . import config
import socket
import pickle

class SensorData:
  temperature = 0
  humidity = 0

class MainAppPacket:
  sensor_data = None

def connect(on_sensor_data):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", config.MAIN_APP_PORT))
    while True:
      data = s.recv(4096)
      if not data:
        print('Disconnected')
        break
      packet = pickle.loads(data)
      if packet.sensor_data is not None:
        on_sensor_data(packet.sensor_data)

