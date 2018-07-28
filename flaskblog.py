from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Bassam Mednini',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 28, 2018'
    },
    {
        'author': 'Mednini Bassam',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 29, 2018'
    }
]

# Einfache Ausgabe
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

# Debug-Modus aktivieren
if __name__ == '__main__':
    app.run(debug=True)