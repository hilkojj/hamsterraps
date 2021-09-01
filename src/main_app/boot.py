from . import tempsensor, main_app_server
from .ledstrips import controller
from ..common import db, logging

import threading

if __name__ == "__main__":

  logging.log_to("main_latest.log")

  db.create_db()

  # start reading temperature sensor data:
  tempsensor_thread = threading.Thread(target=tempsensor.start)
  tempsensor_thread.start()

  # start LEDSTRIP animations:
  led_thread = threading.Thread(target=controller.start)
  led_thread.start()

  # start main app server:
  server_thread = threading.Thread(target=main_app_server.start)
  server_thread.start()

  # wait till all have finished:
  tempsensor_thread .join()
  server_thread     .join()
  led_thread        .join()
