import db
import psycopg2 as psp
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path
import modeleTD
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_squared_error
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import pickle
import numpy as np

dotenv_path = Path('../credentials.env')
load_dotenv(dotenv_path=dotenv_path)


dataForDb = pd.read_csv(os.getenv('CSV'))

conn, c = db.connect_dbt()

dataDB = modeleTD.get_data(conn, c)

x_train ,x_test ,y_train ,y_test = modeleTD.create_train_data(dataDB)

modele = modeleTD.model(x_train,y_train)

def modeleChoice(conn, c, dataForDb, modele):



  user_input = input('db ou modele :')


  if user_input == 'db':

    db.patient(conn, c, dataForDb)
    db.symptomes(conn, c, dataForDb)
    db.valeurs(conn, c, dataForDb)

  elif user_input == 'modele':

    modeleTD.extract_model(modele)

  else :
    print('Ecrivez "db" ou "modele"')

modeleChoice(conn, c, dataForDb, modele)
