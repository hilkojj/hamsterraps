import Adafruit_DHT
import time
import db

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

on_update = []

def start():
  humidity, temperature = 0, 0

  class Frequency():

    def __init__(self, seconds, db_table):
      self.seconds = seconds
      self.last_insert = time.time()
      self.samples = 0
      self.humidAvg = 0
      self.tempAvg = 0
      self.db_table = db_table

    def tick(self):
      self.humidAvg += humidity
      self.tempAvg += temperature

      self.samples += 1
      if time.time() - self.last_insert >= self.seconds:
        self.humidAvg /= self.samples
        self.tempAvg /= self.samples

        print("insert into {0}: Temp={1:0.1f}C Humidity={2:0.1f}%".format(self.db_table, self.tempAvg, self.humidAvg))

        con = db.get_connection()
        cur = con.cursor()

        cur.execute("INSERT INTO {0} VALUES (?, ?, ?)".format(self.db_table), (time.time(), self.tempAvg, self.humidAvg))

        con.commit()
        con.close()

        self.humidAvg, self.tempAvg, self.samples = 0, 0, 0
        self.last_insert = time.time()
        
        

  frequencies = [Frequency(60, "temp_humid_minute"), Frequency(60 * 10, "temp_humid_10minutes"), Frequency(60*60, "temp_humid_hour")]

  failed_once = True

  while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
      
      if humidity > 100:
        if failed_once:
          print("Invalid! Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        else:
          failed_once = True
      else:
        failed_once = False
        for freq in frequencies:
          freq.tick()
        for cb in on_update:
          cb(temperature, humidity)

    else:
      if failed_once:
        print("Sensor failure. Check wiring.")
      else:
        failed_once = True
    time.sleep(1.5)


