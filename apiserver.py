# from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import db

import eventlet
import socketio

HOST_NAME = "localhost"
SERVER_PORT = 8000
LOG_SOCKET_IO = False
LOG_WSGI = False

db_con = db.get_connection()
cur = db_con.cursor()
viewers = 0

sio = socketio.Server(cors_allowed_origins="*", logger=LOG_SOCKET_IO, engineio_logger=LOG_SOCKET_IO) # cbor?
app = socketio.WSGIApp(sio, static_files={
  # '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
  print('SOCKETIO connect ', sid)
  global viewers
  viewers += 1
  sio.emit("viewers", viewers)

def send_sensor_data(to=None):
  sio.emit("temperature", 123, to=to)
  sio.emit("humidity", 10, to=to)

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
  send_sensor_data()

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