import pytest
import modeleTD
import os
from dotenv import load_dotenv
from pathlib import Path
import psycopg2 as psp
import pandas as pd

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


df = modeleTD.get_data(conn, c)


df.drop_duplicates(inplace=True)

class_0 = df[df['diabetes_binary'] == 0]
class_1 = df[df['diabetes_binary'] == 1]

# over sampling of the minority class 1
class_1_over = class_1.sample(len(class_0), replace=True)

# Creating a new dataframe with over sampled class 1 df and class 0 df
df1_new = pd.concat([class_1_over, class_0], axis=0)

x_train ,x_test ,y_train ,y_test = modeleTD.create_train_data(df)

modele = modeleTD.model(x_train,y_train)

def testCo():

  assert str(type(df))== "<class 'pandas.core.frame.DataFrame'>"


def testPrepro():

  assert len(x_test) == round(0.2*len(df1_new))
  assert len(y_test) == round(0.2*len(df1_new))


def testModel():

  assert str(type(modele))== "<class 'sklearn.tree._classes.DecisionTreeClassifier'>"


def test():

  testCo()
  testPrepro()
  testModel()

test()
