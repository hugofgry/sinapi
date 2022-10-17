import psycopg2 as psp
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path

def connect_app():



  conn = psp.connect(
            database="ddjssp3av7n08u",
            user = "gdtbovqaxnpwcw",
            password = "403a6bfbbb1a897e2be9d0df66baef3e48d1bd260afd6f839e1f3d7d3f60a1fe",
            host = "ec2-44-209-57-4.compute-1.amazonaws.com",
            port = "5432"
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



