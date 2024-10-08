from flask import Blueprint, url_for, render_template, redirect, request
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
import sqlalchemy.exc

from models import db, Users

register = Blueprint('register', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(register)

@register.route('/register', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if username and email and password and confirm_password:
            if password == confirm_password:
                # Verifique se o email já existe
                existing_user = Users.query.filter_by(email=email).first()
                if existing_user:
                    return redirect(url_for('register.show') + '?error=user-or-email-exists')

                try:
                    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')  # Método de hash atualizado
                    new_user = Users(username=username, email=email, password=hashed_password)
                    db.session.add(new_user)
                    db.session.commit()
                except sqlalchemy.exc.IntegrityError as e:
                    print(f"IntegrityError: {e}")
                    return redirect(url_for('register.show') + '?error=user-or-email-exists')

                return redirect(url_for('login.show') + '?success=account-created')
            else:
                return redirect(url_for('register.show') + '?error=passwords-do-not-match')
        else:
            return redirect(url_for('register.show') + '?error=missing-fields')
    else:
        return render_template('register.html')
