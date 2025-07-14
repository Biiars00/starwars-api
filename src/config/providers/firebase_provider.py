import requests
from decouple import config

FIREBASE_API_KEY = config('FIREBASE_API_KEY')

def firebase_sign_in(email: str, password: str):
    url = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}'
    payload = {
        'email': email,
        'password': password,
        'returnSecureToken': True
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        return {
            'idToken': data['idToken'],
            'refreshToken': data['refreshToken'],
            'uid': data['localId']
        }
    else:
        error_message = response.json().get('error', {}).get('message', 'Erro desconhecido.')
        raise ValueError(error_message)