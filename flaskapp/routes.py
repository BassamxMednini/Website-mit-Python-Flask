from flask import render_template, flash, redirect, url_for
from flaskapp import app, db, bcrypt
from flaskapp.forms import RegistrationForm, LoginForm
# Fürs generieren der Datenbank müssen
# die jeweiligen Klassen importiert werden
from flaskapp.models import User, Post

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
    form = LoginForm()
    # Bei erfolgreicher Anmeldung -> success-alert via Bootstrap
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'Du hast dich erfolgreich angemeldet. Willkommen zurück!', 'success')
            return redirect(url_for('home'))
        else: 
            flash(f'Anmeldung fehlgeschlagen. Bitte versuche es erneut.', 'danger')
    return render_template('login.html', title='Login', form=form)
