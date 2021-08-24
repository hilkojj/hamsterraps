import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./raps_firebase_account_key.json")
firebase_admin.initialize_app(cred)

# initialize firestore instance
firestore_db = firestore.client()
