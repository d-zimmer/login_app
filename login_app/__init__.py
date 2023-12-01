from flask import Flask

app = Flask(__name__)
app.secret_key = '1952415'

from login_app import routes

def clear_cookies():
    if not request.endpoint or request.endpoint == 'static':
        return  # Evita a limpeza de cookies para requisições estáticas
    print("Limpando cookies antes de cada requisição")
    session.clear()