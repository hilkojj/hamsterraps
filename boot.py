import db
import tempsensor
import apiserver

import threading
import sys

class Logger(object):
  def __init__(self, logfile):
    self.terminal = sys.stdout
    self.log = open(logfile, "w")

  def write(self, message):
    self.terminal.write(message)
    self.log.write(message)
    self.log.flush()  # save new contents NOW

  def flush(self):
    self.log.flush()


if __name__ == "__main__": 

  sys.stdout = Logger("latest.log")
  sys.stderr = sys.stdout

  db.create_db()

  # start reading temperature sensor data:
  tempsensor_thread = threading.Thread(target=tempsensor.start)
  tempsensor_thread.start()

  # start API server:
  api_thread = threading.Thread(target=apiserver.start)
  api_thread.start()

  # wait till all have finished:
  tempsensor_thread .join()
  api_thread        .join()
