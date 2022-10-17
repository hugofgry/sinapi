import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_squared_error
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
import numpy as np
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import time
import sklearn.metrics as metrics
import scikitplot as skplt

def page3(data):

  df = pd.read_csv(data)


  liste = list(df.drop(columns='Diabetes_binary').columns)

  feature = st.multiselect('Selectionnez un ou plusieurs facteurs', liste)



  class_0 = df[df['Diabetes_binary'] == 0]
  class_1 = df[df['Diabetes_binary'] == 1]

  # over sampling of the minority class 1
  class_1_over = class_1.sample(len(class_0), replace=True)

  # Creating a new dataframe with over sampled class 1 df and class 0 df
  df1_new = pd.concat([class_1_over, class_0], axis=0)

  x = df1_new[feature] # features
  y = df1_new[['Diabetes_binary']] # labels

  x_train ,x_test ,y_train ,y_test =train_test_split( x,y,train_size =0.8)

  if st.button('Voir les metrics de performances'):

    model=DecisionTreeClassifier( max_depth=25)
    model.fit( x_train ,y_train )
    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_pred)

    st.metric(label="ACCURACY", value=accuracy)
    st.metric(label="PRECISION", value=precision)
    st.metric(label="RECALL", value=recall)
    st.metric(label="F1_SCORE", value=f1)
    st.metric(label="AUC", value=auc)




    with st.spinner('La learning curve et la courbe ROC sont en cours de chargement...'):


        train_sizes, train_scores, test_scores = learning_curve(DecisionTreeClassifier( max_depth=25), x_train, y_train, cv=10, scoring='accuracy', n_jobs=-1, train_sizes=np.linspace(0.01, 1.0, 50))

        train_mean = np.mean(train_scores, axis=1)
        train_std = np.std(train_scores, axis=1)

        test_mean = np.mean(test_scores, axis=1)
        test_std = np.std(test_scores, axis=1)

        plt.subplots(1, figsize=(10,10))
        plt.plot(train_sizes, train_mean, '--', color="#111111",  label="Training score")
        plt.plot(train_sizes, test_mean, color="#111111", label="Cross-validation score")

        plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, color="#DDDDDD")
        plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, color="#DDDDDD")

        plt.title("Learning Curve")
        plt.xlabel("Training Set Size"), plt.ylabel("Accuracy Score"), plt.legend(loc="best")
        plt.tight_layout()
        st.pyplot()


        probs = model.predict_proba(x_test)
        y_true = y_test
        y_probas = probs
        skplt.metrics.plot_roc_curve(y_true, y_probas)
        st.pyplot()




