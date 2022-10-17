import psycopg2 as psp
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path




def connect_dbt():


  dotenv_path = Path('../credentials.env')
  load_dotenv(dotenv_path=dotenv_path)


  conn = psp.connect(
            database=os.getenv('DATABASE_DIABETE'),
            user = os.getenv('USER_DIABETE'),
            password = os.getenv('PASSWORD_DIABETE'),
            host = os.getenv('HOST_DIABETE'),
            port = os.getenv('PORT_DIABETE')
        )
  c = conn.cursor()

  return conn, c









def patient(conn, c, data):

  try:



    c.execute(' CREATE TABLE IF NOT EXISTS patient (id SERIAL PRIMARY KEY, diabete_binary INTEGER)')
    conn.commit()
    print('create')

  except:

    print('error')



  diabete = data['Diabetes_binary'].astype('int')
  # #diabete_binary = int(diabete)


  for row in diabete:


    c.execute(''' INSERT INTO patient (diabete_binary ) VALUES (%s) ''', [row])
    conn.commit()




    c.execute('DROP TABLE patient')




def symptomes(conn, c, data):

  c.execute(''' CREATE TABLE IF NOT EXISTS symptomes (id SERIAL PRIMARY KEY,
    facteur VARCHAR(255) )''')
  conn.commit()
  print('create')


  dataX = data.drop(columns = 'Diabetes_binary')

  facteur = dataX.columns


  for column in facteur :

    c.execute(''' INSERT INTO symptomes (facteur) VALUES (%s) ''', (column,))
    conn.commit()






def valeurs(conn, c, data):

  c.execute(''' CREATE TABLE IF NOT EXISTS valeurs (id SERIAL PRIMARY KEY,
    valeur INTEGER,
    patient_id INTEGER,
    symptome_id INTEGER,
    FOREIGN KEY (patient_id) REFERENCES patient(id),
    FOREIGN KEY (symptome_id) REFERENCES symptomes(id))''')
  conn.commit()
  print('create')

  diabete_feat = data[['HighBP','HighChol','CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits','Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost','GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income']].astype('int')

  for row_feat in diabete_feat.values:


    c.execute(''' INSERT INTO symptome (HighBP,HighChol,CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack,PhysActivity, Fruits,Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost,GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ''', (int(row_feat[0]),int(row_feat[1]),int(row_feat[2]),int(row_feat[3]),int(row_feat[4]),int(row_feat[5]),int(row_feat[6]),int(row_feat[7]),int(row_feat[8]),int(row_feat[9]),int(row_feat[10]),int(row_feat[11]),int(row_feat[12]),int(row_feat[13]),int(row_feat[14]),int(row_feat[15]),int(row_feat[16]),int(row_feat[17]),int(row_feat[18]),int(row_feat[19]),int(row_feat[20])))
    conn.commit()


    counter_row = 1
    counter_value = 1
    symptome_key = 1


    for row in df.iterrows():

          symptome_key = 1

          for value in row[1][1:]:
            value_tuple = (counter_value,value,symptome_key,counter_row)
            print("Now inserting value :" + str(value_tuple))
            c.execute(""" INSERT INTO Valeurs (id,valeur,symptome_id,patient_id) VALUES (%s, %s, %s, %s) """, value_tuple)
            counter_value += 1
            symptome_key += 1
            conn.commit()

          counter_row += 1





def get_data_diabete(c):

  c_dbt.execute('''SELECT * FROM Valeurs''')
  dbt = c_dbt.fetchall()

  return dbt
