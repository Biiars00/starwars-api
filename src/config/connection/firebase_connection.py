from firebase_admin import credentials, firestore
import firebase_admin
import os
import json

try:
    firebase_admin.get_app()
except ValueError:
    firebase_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    
    if firebase_json:
        cred_dict = json.loads(firebase_json)
        cred = credentials.Certificate(cred_dict)
    else:
        cred = credentials.Certificate('src/config/connection/firebase_connection.json')
    
    firebase_admin.initialize_app(cred)

db = firestore.client()