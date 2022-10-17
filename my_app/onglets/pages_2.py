import streamlit as st
import os
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd





def page2(data):

  df = pd.read_csv(data)

  st.title('Données utilisées')

  st.dataframe(df)  # Same as st.write(df)Ò

  df1 = df.drop('Diabetes_binary', axis=1).corrwith(df.Diabetes_binary)

  st.title('Corrélation avec les différents facteurs')

  st.bar_chart(df1)

  st.title('Parts des diabétiques dans les données')

  fig = plt.figure(figsize=(10, 4))
  plt.pie( df['Diabetes_binary'].value_counts() ,autopct='%.02f', labels = ["Pas diabétique","Diabétique"] )
  st.pyplot(fig)


  st.set_option('deprecation.showPyplotGlobalUse', False)
  liste = ['HighChol','HighBP','CholCheck','Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits','Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost','GenHlth','DiffWalk','Sex']
  feature = st.selectbox('Avec quel facteur souhaitez-vous comparer ?', (liste))

  class_0 = df[df['Diabetes_binary'] == 0]
  class_1 = df[df['Diabetes_binary'] == 1]

  # over sampling of the minority class 1
  class_1_over = class_1.sample(len(class_0), replace=True)

  # Creating a new dataframe with over sampled class 1 df and class 0 df
  df1_new = pd.concat([class_1_over, class_0], axis=0)
  df1_new['Diabetes_binary'] = df1_new['Diabetes_binary'].replace(0.0 , "Non diabétique").replace(1.0, "Diabétique")
  df1_new = df1_new.replace(0.0, 'Non').replace(1.0, "Oui")



  for l in liste :

    if feature == l :

      df2 = pd.crosstab(df1_new[l],df1_new.Diabetes_binary)
      fig2 = plt.figure(figsize=(10, 4))
      df2.plot.bar()
      st.pyplot()
