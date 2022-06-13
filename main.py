import requests
from bs4 import BeautifulSoup


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


for x in range(47, 60):
    URL = f"https://www.turkdiab.org/diyabet-hakkinda-hersey.asp?lang=TR&id={x}"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    headline = soup.find('h1')

    contents = soup.find_all('p')
    print(headline)
    contentList = []
    for pElements in range(len(contents)-2):
        contentList.append(contents[pElements].text)
    db.collection('DiabetInformations').document(headline.text).set({'details': contentList, 'title': headline.text, 'id': x})

