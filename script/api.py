from fastapi import FastAPI, Path, HTTPException
import numpy as np
import pandas as pd
import pickle






app = FastAPI(title="Congestion")



def create_X_prediction(HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits,Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost,GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income):




  X_prediction_dict = {'HighBP' : [0], 'HighChol' : [0], 'CholCheck' : [0], 'BMI' : [0], 'Smoker' : [0], 'Stroke' : [0], 'HeartDiseaseorAttack' : [0], 'PhysActivity' : [0], 'Fruits' : [0],'Veggies' : [0], 'HvyAlcoholConsump' : [0], 'AnyHealthcare' : [0], 'NoDocbcCost' : [0],'GenHlth' : [0], 'MentHlth' : [0], 'PhysHlth' : [0], 'DiffWalk' : [0], 'Sex' : [0], 'Age' : [0], 'Education' : [0], 'Income' : [0]}
  X_prediction = pd.DataFrame(X_prediction_dict)
  X_prediction[['HighBP','HighChol','CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits','Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost','GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income']] = HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits,Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost,GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income
  X_prediction[['HighBP','HighChol','CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits','Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost','GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income']] =  X_prediction[['HighBP','HighChol','CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits','Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost','GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income']].astype('float')

  return X_prediction






@app.get("/prediction/")
async def prediction(HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits,Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost,GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income):

    with open('modele/modeleDecisionTree.pkl', 'rb') as file:

    #Call load method to deserialze
      m = pickle.load(file)

      return str(m.predict(create_X_prediction(HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits,Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost,GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income))[0])



# @app.get("/predictionClust/")
# async def prediction(date):

#     with open('modele/modeleRF.pkl', 'rb') as file:

#     #Call load method to deserialze
#       m = pickle.load(file)

#       LQTs = m.predict(create_X_prediction(date))

#       with open('../modele/modeleClust.pkl', 'rb') as file:

#     #Call load method to deserialze
#         c = pickle.load(file)

#         df_Clust= pd.DataFrame(LQTs, columns=['Traffic'])

#         return c.predict(df_Clust)[0].astype('str')



# @app.get("/predictionCalend/")
# async def prediction():

#       today = date.today()
#       hour = 9
#       minute = 0
#       time = datetime.datetime(today.year, today.month, today.day ,hour, minute)

#       predic_list = []

#       for i in range(4,13):

#         if minute == 60:
#           hour += 1
#           minute = 0

#         time = datetime.datetime(today.year, today.month, today.day ,hour, minute)

#         with open('../modele/modeleRF.pkl', 'rb') as file:

#         #Call load method to deserialze
#           m = pickle.load(file)

#           LQTs = m.predict(create_X_prediction(time))

#           with open('../modele/modeleClust.pkl', 'rb') as file:

#         #Call load method to deserialze
#             c = pickle.load(file)

#             df_Clust= pd.DataFrame(LQTs, columns=['Traffic'])


#             minute += 15

#             predic_list.append(c.predict(df_Clust)[0].astype('str'))

#       return predic_list


