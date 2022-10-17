import streamlit as st
import os
from dotenv import load_dotenv
from pathlib import Path
import psycopg2 as psp
import streamlit_authenticator as stauth
import dbapp
# from onglets import registration

# conn, c = dbapp.connect_app()

# def register():

#   registration.user_registration(conn, c)






def logging(users, page1, page2, page3):



  names = [user[1] for user in users]
  usernames = [user[2] for user in users]
  passwords = [user[3] for user in users]




  hashed_passwords = stauth.Hasher(passwords).generate()

  credentials = {"usernames":{}}

  for uname,name,pwd in zip(usernames,names,hashed_passwords):
      user_dict = {"name": name, "password": pwd}
      credentials["usernames"].update({uname: user_dict})









  authenticator = stauth.Authenticate(credentials,'cookie_name', 'signature_key', cookie_expiry_days=30)





  name, authentication_status,username = authenticator.login('Login','main')



  if authentication_status :



    authenticator.logout("Deconnexion","sidebar")



    page_names_to_funcs = {

    "Prédiction avancée": page1,
    "Analyse": page2,
    "Metrics" : page3
    }

    selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()

  elif authentication_status == False:

      st.error('Username/password is incorrect')


  elif authentication_status == None:

      st.warning('Please enter your username and password')





  # page_names_to_funcs = {

  # "Inscription": register

  # }


  # page_names_to_funcs["Inscription"]()







    # with st.form("my_form2"):


    #   st.subheader("Create an Account")
    #   name= st.text_input('Nom')
    #   name2 = st.text_input("Prénom")

    #   new_user = st.text_input("Nom d'utilisateur")
    #   new_passwd = st.text_input('Mot de passe',type='password')

    #   submitted = st.form_submit_button("SignUp")


    #   if submitted:

    #     totalName = name +' '+ name2
    #     print('joy')
    #     c.execute('''SELECT * FROM Users''')
    #     users= c.fetchall()
    #     usernames = [user[2] for user in users]
    #     print(usernames)

    #     if usernames == new_user :

    #       st.error("Nom d'utilisateur déjà utilisé", icon="🚨")

    #     else :

    #       c.execute('''INSERT INTO Users (name, username, password) VALUES (%s,%s,%s)''',(totalName, new_user, new_passwd))
    #       conn.commit()
    #       st.success("You have successfully created an account.Go to the Login Menu to login")



    #   else :
    #     print('error')

















