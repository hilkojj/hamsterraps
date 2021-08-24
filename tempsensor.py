import Adafruit_DHT
import time
import db

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def start():
    timer = 0
    tempAvg = 0
    humidAvg = 0

    minuteTimer = 0
    hourTimer = 0

    while True:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))

            if humidity > 100:
                print("Invalid")
            else:
                tempAvg += temperature
                humidAvg += humidity
                timer += 1

        else:
            print("Sensor failure. Check wiring.")

        SLEEP_TIME = 1.1
        time.sleep(SLEEP_TIME)
        minuteTimer += SLEEP_TIME
        hourTimer += SLEEP_TIME

        if timer == 10:
            tempAvg /= timer
            humidAvg /= timer

            frequencyLabel = "FREQUENT"
            if minuteTimer > 60:
                minuteTimer = 0
                frequencyLabel = "MINUTE"
            if hourTimer > 60 * 60:
                hourTimer = 0
                frequencyLabel = "HOUR"

            print("AVERAGE-{2}       Temp={0:0.1f}C Humidity={1:0.1f}%".format(tempAvg, humidAvg, frequencyLabel))

            # add average data to database
            try:
                db.firestore_db.collection("temperatureHumidity").add(
                    {"temperature": tempAvg, "humidity": humidAvg, "time": db.firestore.SERVER_TIMESTAMP, "frequency": frequencyLabel}
                )
            except Exception as e:
                print("Error while adding to db:", e)

            tempAvg = 0
            humidAvg = 0
            timer = 0

