import os
import secrets
from PIL import Image
from flask import render_template, flash, redirect, url_for, request
from flaskapp import app, db, bcrypt
from flaskapp.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskapp.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

# Highlight Post
highlightPost =	{
    'author': 'Bassam Mednini',
    'title': 'Highlight Post 1',
    'content': 'This is a HIGHLIGHT POST. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.',
    'date_posted': '10. September 2018',
    'image_url': 'https://images.pexels.com/photos/218983/pexels-photo-218983.jpeg?cs=srgb&dl=architecture-background-buildings-218983.jpg&fm=jpg'
}

# Artikel
posts = [
    {
        'author': 'Bassam Mednini',
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.',
        'date_posted': '16. September 2018',
        'image_url': 'https://images.pexels.com/photos/734983/pexels-photo-734983.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260'
    },
    {
        'author': 'Max Mustermann',
        'title': 'Blog Post 2',
        'content': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.',
        'date_posted': '17. September 2018',
        'image_url': 'https://images.pexels.com/photos/734983/pexels-photo-734983.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260'
    },
    {
        'author': 'Max Musterfrau',
        'title': 'Blog Post 3',
        'content': 'Dritter Beitrag',
        'date_posted': '18. September 2018',
        'image_url': 'https://images.pexels.com/photos/734983/pexels-photo-734983.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260'
    }
]

# Home
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, highlightPost=highlightPost)

# Registration
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    # Bei erfolgreicher Registration -> success-alert via Bootstrap
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Dein Account wurde erfolgreich registriert. Jetzt anmelden!', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Registration', form=form)

# Login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    # Bei erfolgreicher Anmeldung -> success-alert via Bootstrap
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Willkommen zurück!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Anmeldung fehlgeschlagen. Bitte versuche es erneut.', 'danger')
    return render_template('login.html', title='Login', form=form)

# Ausloggen
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_images/', picture_fn)

    # Maximalgröße für PB  
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

# Account
@app.route("/profil", methods=['GET', 'POST'])
@login_required
def profil():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data 
        current_user.email = form.email.data 
        db.session.commit()
        flash('Dein Profil wurde aktualisiert.', 'success')
        return redirect(url_for('profil'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_images/' + current_user.image_file)
    return render_template('profil.html', title='Profil', image_file=image_file, form=form)