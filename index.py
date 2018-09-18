from flask import Flask, render_template
app = Flask(__name__)

highlightPost =	{
    'author': 'Bassam Mednini',
    'title': 'Blog Post 1',
    'content': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.',
    'date_posted': '16. September 2018',
    'image_url': 'https://images.pexels.com/photos/218983/pexels-photo-218983.jpeg?cs=srgb&dl=architecture-background-buildings-218983.jpg&fm=jpg'
}

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

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, highlightPost=highlightPost)
