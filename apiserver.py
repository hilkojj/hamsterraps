from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import db

HOST_NAME = "localhost"
SERVER_PORT = 8000

def start():

  db_con = db.get_connection()
  cur = db_con.cursor()

  class ApiServer(BaseHTTPRequestHandler):
    def do_GET(self):
      try:
        response_obj = {}

        if self.path == "/current_sensor_data.json":
          self.send_response(200)

          cur.execute("SELECT * FROM temp_humid_minute ORDER BY date DESC LIMIT 1")

          response_obj["date"], response_obj["temperature"], response_obj["humidity"] = cur.fetchone()

        elif self.path == "/day_sensor_data.json":
          self.send_response(200)

          cur.execute("SELECT * FROM temp_humid_minute ORDER BY date DESC LIMIT 1440")
          response_obj["datapoints"] = []

          for row in cur:
            point = {}
            point["date"], point["temperature"], point["humidity"] = row
            response_obj["datapoints"].append(point)

        else:
          self.send_response(404)
          
          response_obj["error"] = "this is not a valid path"

        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(response_obj, indent=2), "utf-8"))
      except BrokenPipeError:
        pass


  webServer = HTTPServer((HOST_NAME, SERVER_PORT), ApiServer)
  print("ApiServer started http://%s:%s" % (HOST_NAME, SERVER_PORT))

  try:
    webServer.serve_forever()
  except KeyboardInterrupt:
    pass

  webServer.server_close()
  print("Server stopped.")