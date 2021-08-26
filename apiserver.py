# from http.server import BaseHTTPRequestHandler, HTTPServer
import db
import tempsensor

import time
from flask import Flask, request
from flask_cors import CORS
import socketio
import eventlet
eventlet.monkey_patch()

HOST_NAME = "localhost"
SERVER_PORT = 8000
LOG_SOCKET_IO = True
LOG_WSGI = False

db_con = db.get_connection()
cur = db_con.cursor()

temp, humid = 0, 0
viewers = 0


sio = socketio.Server(cors_allowed_origins="*", logger=LOG_SOCKET_IO, engineio_logger=LOG_SOCKET_IO)
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app, static_files={
  # '/': {'content_type': 'text/html', 'filename': 'index.html'}
})
CORS(app)

@app.route("/")
def hello_world():
  return "Hello. Visit <a href='https://hilkojj.nl/hamster/'>hilkojj.nl/hamster</a>"

@app.route("/sensor_data.json")
def get_sensor_data():

  table_name = {
    "minute": "temp_humid_minute",
    "10minutes": "temp_humid_10minutes",
    "hour": "temp_humid_hour",
  }.get(
    request.args.get('frequency', default="minute", type=str),
    "temp_humid_minute" # default table_name
  )
  since_date =  request.args.get('since_date', default=0, type=int)
  to_date =     request.args.get('to_date', default=time.time(), type=int)

  LIMIT = 24 * 365

  cur.execute("SELECT * FROM {0} WHERE date > ? AND date < ? ORDER BY date ASC LIMIT {1}".format(table_name, LIMIT), (since_date, to_date))
  return {
    "datapoints": cur.fetchall()
  }

def send_sensor_data(to=None):
  sio.emit("temperature", temp, to=to)
  sio.emit("humidity", humid, to=to)

def set_temp_humid(t, h):
  global temp
  global humid
  temp, humid = t, h
  send_sensor_data()

tempsensor.on_update.append(set_temp_humid)

@sio.event
def connect(sid, environ):
  print('SOCKETIO connect ', sid)
  global viewers
  viewers += 1
  sio.emit("viewers", viewers)

@sio.event
def request_sensor_data(sid):
  send_sensor_data(to=sid)

@sio.event
def request_viewers(sid):
  global viewers
  sio.emit("viewers", viewers, to=sid)

@sio.event
def disconnect(sid):
  print('SOCKETIO disconnect ', sid)
  global viewers
  viewers -= 1
  sio.emit("viewers", viewers)

def start():
  eventlet.wsgi.server(eventlet.listen((HOST_NAME, SERVER_PORT)), app, log_output=LOG_WSGI)
