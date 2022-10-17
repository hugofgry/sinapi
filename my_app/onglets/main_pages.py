import streamlit as st
from PIL import Image
import requests
import time
import streamlit_authenticator as stauth




def fetch(session, url):
    try:
        result = session.get(url)
        return result.json()
    except Exception:
        return {}

def main_page():

    image = Image.open('image/diabete-type2.jpeg')
    st.image(image)
    st.title("Prédiagnostique d'un diabète")
    session = requests.Session()

    with st.form("my_form"):
      BP = st.selectbox(
       "Avez vous une pression arterielle élevée ?", ("Oui", "Non"))

      CHOL = st.selectbox(
       "Avez vous un choléstérol élevé ?", ("Oui", "Non"))

      CholCheck = st.selectbox(
       "Avez vous fais une analyse, datant d'il y a moins de 5 ans, de choléstérol ?", ("Oui", "Non"))

      BMI = st.number_input(
       "Quel est votre indice de masse corporelle ?")

      Smoker = st.selectbox(
       "Avez vous fumez plus de 100 cigarettes au cours de votre vie ? (5 paquet = 100 cigarettes) " , ("Oui", "Non"))

      Stroke = st.selectbox(
       "Avez vous eu un AVC ?", ("Oui", "Non"))

      HeartDiseaseorAttack = st.selectbox(
       "Avez vous une maladie coronarienne ou eu un infarctus du myocarde ?", ("Oui", "Non"))

      PhysActivity = st.selectbox(
       "Avez vous eu une activité physique durant ces 30 derniers jours (le travail n'est pas inclu)?", ("Oui", "Non"))

      Fruits = st.selectbox(
       "Consommez-vous un ou plusieurs fruits par jour ?", ("Oui", "Non"))

      Veggies = st.selectbox(
       "Consommez-vous un ou plusieurs légumes par jour ?", ("Oui", "Non"))

      HvyAlcoholConsump = st.selectbox(
       "Buvez-vous beaucoup d'alcool ? (hommes adultes buvant plus de 14 verres par semaine et femmes adultes buvant plus de 7 verres par semaine)", ("Oui", "Non"))

      AnyHealthcare = st.selectbox(
       "Avez vous un type de couverture de soins de santé ? (y compris l'assurance maladie, les plans prépayés tels que HMO, etc...)", ("Oui", "Non"))

      NoDocbcCost = st.selectbox(
       "Y a-t-il eu un moment au cours des 12 derniers mois où vous avez eu besoin de consulter un médecin, mais que vous n'avez pas pu en raison du coût ?", ("Oui", "Non"))

      GenHlth = st.selectbox(
       "Diriez-vous qu'en général votre santé est : ?", ('Excellente', 'Très bonne', 'Bonne', 'Passable', 'Mauvaise'))

      MentHlth = st.number_input(
       "En pensant maintenant à votre santé mentale (qui comprend le stress, la dépression et les problèmes émotionnels), pendant combien de jours, au cours des 30 derniers jours, votre santé mentale n'a-t-elle pas été bonne ?" ,step=1)

      PhysHlth = st.number_input(
       "Maintenant, en pensant à votre santé physique (qui comprend les maladies physiques et les blessures), pendant combien de jours, au cours des 30 derniers jours, votre santé physique n'a-t-elle pas été bonne ?", step=1)

      DiffWalk = st.selectbox(
       "Avez-vous de sérieuses difficultés à marcher ou à monter des escaliers ?", ('Oui', 'Non'))

      Sex = st.selectbox(
       "Quel est votre sexe ?", ('Homme', 'Femme'))

      Age = st.number_input(
       "Quel est votre âge ?", step= 1)

      Education = st.selectbox(
       "Votre niveau d'étude est :  ?", ("Jamais fréquenté l'école ou seulement la maternelle", "École élémentaire", "Un ou plusieurs lycées", "Diplôme d'études secondaires (Baccalauréat)", "Université", "Diplome universaitaire ou équivalent"))

      Income = st.selectbox(
       "Vos revenus annuels ?", ("Moins de 10 000", "Moins de 15 000", "Moins de 20 000", "Moins de 25 000", "Moins de 35 000", "Moins de 50 000", "Moins de 75 000", "75 000 ou plus"))





      submitted = st.form_submit_button("Valider")



      liste = [BP, CHOL, CholCheck, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies, HvyAlcoholConsump , AnyHealthcare, NoDocbcCost, GenHlth, DiffWalk, Sex, Education, Income]
      listeReplace = []

      if submitted:

        for l in liste :

            save = l.replace('Oui', '1').replace('Non', '0').replace('Excellente', '1').replace('Très bonne', '2').replace('Bonne', '3').replace('PPassable','4').replace('Mauvaise','5').replace('Homme','1').replace('Femme','0').replace("Jamais fréquenté l'école ou seulement la maternelle", "1").replace("École élémentaire", "2").replace("Un ou plusieurs lycées", "3").replace("Diplôme d'études secondaires (Baccalauréat)", "4").replace("Université","5").replace("Diplome universaitaire ou équivalent","6").replace("Moins de 10 000","1").replace("Moins de 15 000","2").replace("Moins de 20 000","3").replace("Moins de 25 000","4").replace("Moins de 35 000","5").replace("Moins de 50 000","6").replace("Moins de 75 000","7").replace("75 000 ou plus","8")
            listeReplace.append(save)









        data = fetch(session, f"https://projectapidb.herokuapp.com/prediction/?HighBP={int(listeReplace[0][0])}&HighChol={int(listeReplace[1][0])}&CholCheck={int(listeReplace[2][0])}&BMI={BMI}&Smoker={int(listeReplace[3][0])}&Stroke={int(listeReplace[4][0])}&HeartDiseaseorAttack={int(listeReplace[5][0])}&PhysActivity={int(listeReplace[6][0])}&Fruits={int(listeReplace[7][0])}&Veggies={int(listeReplace[8][0])}&HvyAlcoholConsump={int(listeReplace[9][0])}&AnyHealthcare={int(listeReplace[10][0])}&NoDocbcCost={int(listeReplace[11][0])}&GenHlth={int(listeReplace[12][0])}&MentHlth={MentHlth}&PhysHlth={PhysHlth}&DiffWalk={int(listeReplace[13][0])}&Sex={int(listeReplace[14][0])}&Age={Age}&Education={int(listeReplace[15][0])}&Income={int(listeReplace[16][0])}")
        my_bar = st.progress(0)


        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)

        if data == "0":

           st.write("Pas de diabètes")

        elif data == "1":
          st.warning('Vous avez un diabète, allez consulter un medecin !', icon="⚠️")

          st.info(f'Vous pouvez prendre rdv sur : https://www.doctolib.fr', icon="ℹ️")

        else:
           st.error("Error")
