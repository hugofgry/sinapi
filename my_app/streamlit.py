import streamlit as st
import streamlit_authenticator as stauth
from PIL import Image
from onglets import pages_2
from onglets import main_pages
import os
from dotenv import load_dotenv
from pathlib import Path
import dbapp
# from onglets import registration
import psycopg2 as psp
from onglets import connexion
from onglets import page_3




conn, c = dbapp.connect_app('../credentials.env')
users = dbapp.get_data(c)

dotenv_path = Path('../credentials.env')
load_dotenv(dotenv_path=dotenv_path)
data = os.getenv('CSV')


def page1() :
  main_pages.main_page()



def page2():

  pages_2.page2(data)



def page3() :
  page_3.page3(data)

# def register():
#   registration.user_registration(conn, c)

def co():

  connexion.logging(users, page1, page2, page3)






co()





