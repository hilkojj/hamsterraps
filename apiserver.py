# from http.server import BaseHTTPRequestHandler, HTTPServer
import db
import tempsensor

from flask import Flask
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

@app.route("/")
def hello_world():
    return "Hello. Visit <a href='https://hilkojj.nl/hamster/'>hilkojj.nl/hamster</a>"

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

  # class ApiServer(BaseHTTPRequestHandler):
  #   def do_GET(self):
  #     try:
  #       response_obj = {}

  #       if self.path == "/current_sensor_data.json":
  #         self.send_response(200)

  #         cur.execute("SELECT * FROM temp_humid_minute ORDER BY date DESC LIMIT 1")

  #         response_obj["date"], response_obj["temperature"], response_obj["humidity"] = cur.fetchone()

  #       elif self.path == "/day_sensor_data.json":
  #         self.send_response(200)

  #         cur.execute("SELECT * FROM temp_humid_minute ORDER BY date DESC LIMIT 1440")
  #         response_obj["datapoints"] = []

  #         for row in cur:
  #           point = {}
  #           point["date"], point["temperature"], point["humidity"] = row
  #           response_obj["datapoints"].append(point)

  #       else:
  #         self.send_response(404)
          
  #         response_obj["error"] = "this is not a valid path"

  #       self.send_header("Content-type", "application/json")
  #       self.end_headers()
  #       self.wfile.write(bytes(json.dumps(response_obj, indent=2), "utf-8"))
  #     except BrokenPipeError:
  #       pass


  # webServer = HTTPServer((HOST_NAME, SERVER_PORT), ApiServer)
  # print("ApiServer started http://%s:%s" % (HOST_NAME, SERVER_PORT))

  # try:
  #   webServer.serve_forever()
  # except KeyboardInterrupt:
  #   pass

  # webServer.server_close()
  # print("Server stopped.")