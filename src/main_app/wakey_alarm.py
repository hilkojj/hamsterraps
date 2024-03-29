from sys import stdout
from ..common import db
import time
import sched
import subprocess

def activate_alarm(alarm_timestamp):
  print("ALARM", alarm_timestamp)
  proc = subprocess.Popen(["python", "-m", "src.buzzer.buzzer", "nice", "alarm"])
  proc.wait()
  proc = subprocess.Popen(["python", "-m", "src.buzzer.buzzer", "nice", "mii"])
  proc.wait()
  proc = subprocess.Popen(["python", "-m", "src.buzzer.buzzer", "nice", "mario_underworld"])
  proc.wait()
  proc = subprocess.Popen(["python", "-m", "src.buzzer.buzzer", "nice", "tetris"])
  proc.wait()


def start():

  db_con = db.get_connection()
  cur = db_con.cursor()

  cur.execute("INSERT INTO alarms VALUES (?, ?)", (1633069613, 1633069613))
  db_con.commit()

  cur.execute("SELECT * FROM alarms WHERE alarm_timestamp > ?", (time.time(),))

  scheduler = sched.scheduler(time.time, time.sleep)

  for alarm in cur.fetchall():
    print(alarm)
    sched_alarm_id = scheduler.enterabs(alarm[0], 1, activate_alarm, (alarm[0],))
    break

  scheduler.run()
  print("scheduler done")


