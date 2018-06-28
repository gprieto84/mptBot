from flask import render_template
from app import application

@application.route('/')
@application.route('/index')
def index():
    user = {'username':'Maria Luisa (Mi reina)'}
    posts = [
        {
          'author':{'username':'Marianna'},
          'body':'Me gustan los Shokins, las LOL y los Hatchimals'  
        },
        {
          'author':{'username':'German'},
          'body':'Studying very hard to make my dreams come true with my family'  
        }
    ]
    return render_template('index.html',title='Home', user=user, posts=posts)





