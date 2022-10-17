import streamlit as st
import streamlit_authenticator as stauth
import dbapp
import psycopg2 as psp
import os
from dotenv import load_dotenv
from pathlib import Path

conn, c = dbapp.connect_app()

placeholder = st.empty()


def user_registration(conn, c):

    with placeholder.form("my_form2"):

      st.subheader("Create an Account")
      name= st.text_input('Nom')
      name2 = st.text_input("Prénom")

      new_user = st.text_input("Nom d'utilisateur")
      new_passwd = st.text_input('Mot de passe',type='password')

      submitted = st.form_submit_button("SignUp")

      if submitted:

        totalName = name +' '+ name2
        print('joy')
        c.execute('''SELECT * FROM Users''')
        users= c.fetchall()
        usernames = [user[2] for user in users]

        if new_user in usernames :

          st.error("Nom d'utilisateur déjà utilisé", icon="🚨")

        else :

          c.execute('''INSERT INTO Users (name, username, password) VALUES (%s,%s,%s)''',(totalName, new_user, new_passwd))
          conn.commit()
          st.success("You have successfully created an account.Go to the Login Menu to login")
          placeholder.empty()






