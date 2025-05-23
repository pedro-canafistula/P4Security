from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint('auth', __name__, template_folder='../templates')

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if email == 'admin@example.com' and senha == '123456':
            return 'Login bem-sucedido!'
        else:
            return 'Credenciais inválidas.'
    return render_template('auth/login.html')
