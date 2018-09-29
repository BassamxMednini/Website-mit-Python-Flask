from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '2b4311fdf854371c367d26a90e81b2d0'

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
        flash(f'Account created for {form.username.data}. Welcome!', 'success')
        return redirect(url_for('home'))
    return render_template('registration.html', title='Registration', form=form)

# Login
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
