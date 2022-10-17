import psycopg2 as psp
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path

def connect_app(path):

  dotenv_path = Path(path)
  load_dotenv(dotenv_path=dotenv_path)


  conn = psp.connect(
            database=os.getenv('DATABASE'),
            user = os.getenv('USER'),
            password = os.getenv('PASSWORD'),
            host = os.getenv('HOST'),
            port = os.getenv('PORT')
        )
  c = conn.cursor()

  return conn, c



# c.execute(''' CREATE TABLE IF NOT EXISTS Users (id SERIAL PRIMARY KEY, name VARCHAR(255), username VARCHAR(255), password VARCHAR(255) )''')
# conn.commit()

# c.execute('''INSERT INTO Users (name, username, password) VALUES ('Hugo Fugeray', 'rayden', 'chantnat')''')
# conn.commit()







def get_data(c):

  c.execute('''SELECT * FROM Users''')
  user = c.fetchall()

  return user



