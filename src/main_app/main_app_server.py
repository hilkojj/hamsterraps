import socket
from ..common import config
import queue
import pickle

send_queue = queue.Queue()

def start():

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("localhost", config.MAIN_APP_PORT))
    s.listen()
    while True:
      try:
        conn, addr = s.accept()
        print('Connected by', addr)
        while True:
          packet = send_queue.get()
          data_string = pickle.dumps(packet)
          conn.send(data_string)
      except Exception as e:
        print(e)

