import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_squared_error
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import pickle
import numpy as np
import psycopg2 as psp



def get_data(conn, c) :

  c.execute('''SELECT valeurs.valeur AS valeur, symptomes.facteur AS facteur, patient.diabete_binary AS diabete_binary, patient_id FROM valeurs
  JOIN patient
  ON patient_id = patient.id
  JOIN symptomes
  ON symptome_id = symptomes.id;''')

  df_init = c.fetchall()

  data = pd.DataFrame(df_init)

  data.rename(columns={0: "valeur", 1: "facteur", 2 :'diabetes_binary', 3 : 'patient'}, inplace = True)

  df = data.pivot(index = ['patient', 'diabetes_binary'], columns='facteur', values='valeur')

  df.reset_index('diabetes_binary', inplace=True)

  return df


def create_train_data(df):

  df.drop_duplicates(inplace=True)

  class_0 = df[df['diabetes_binary'] == 0]
  class_1 = df[df['diabetes_binary'] == 1]

  # over sampling of the minority class 1
  class_1_over = class_1.sample(len(class_0), replace=True)

  # Creating a new dataframe with over sampled class 1 df and class 0 df
  df1_new = pd.concat([class_1_over, class_0], axis=0)

  x = df1_new.drop('diabetes_binary', axis = 1) # features
  y = df1_new[['diabetes_binary']] # labels

  x_train ,x_test ,y_train ,y_test =train_test_split( x,y,train_size =0.8)

  return x_train ,x_test ,y_train ,y_test


def model(x_train,y_train):

  model=DecisionTreeClassifier( max_depth=25)
  model.fit( x_train ,y_train )
  prediction=model.score( x_train ,y_train )

  return model


def extract_model(model):

  with open('../modele/modeleDecisionTree.pkl', 'wb') as file:

    pickle.dump(model, file)



