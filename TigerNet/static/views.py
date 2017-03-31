from flask import render_template
from TigerNet.static import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Nate'}
    posts = [
        {
            'author': {'nickname': 'john'},
            'body': 'Br'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           user=user,
                           posts=posts)
