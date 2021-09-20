import sqlite3

def get_connection():
  return sqlite3.connect('prod.db')

def create_db():
  con = get_connection()

  cur = con.cursor()
  cur.execute('''CREATE TABLE IF NOT EXISTS temp_humid_minute
               (date integer, temperature real, humidity real)''')
  cur.execute('''CREATE TABLE IF NOT EXISTS temp_humid_10minutes
               (date integer, temperature real, humidity real)''')
  cur.execute('''CREATE TABLE IF NOT EXISTS temp_humid_hour
               (date integer, temperature real, humidity real)''')

  # cur.execute('''DELETE FROM temp_humid_10minutes WHERE temperature > 25.8''')

  # cur.execute('''CREATE TABLE IF NOT EXISTS current_values
  #              (temperature real, humidity real)''')

  # cur.execute('''VACUUM''')

  con.commit()
  con.close()
