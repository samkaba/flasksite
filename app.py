from flask import Flask, redirect, url_for, request, render_template 
from flask_sqlalchemy import SQLAlchemy
import os
from app import app, db





project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(
    os.path.join(project_dir,"mydatabase.db" ))

with app.app_context():
     db.create_all()
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = database_file
# db = SQLAlchemy(app)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


db = SQLAlchemy()
class Book(db.Model):
    name = db.Column(db.String(100),unique=True,
                     nullable=False,primary_key=True)
    author = db.Column(db.String(100),
                       nullable=False)


@app.route('/addbook')
def addbook():
    return render_template('addbook.html')  

@app.route('/submitbook', methods=['POST'])
def submitbook():
    name = request.form['name']
    author = request.form['author']
    return 'Book name is %s and Author is %s' %(name,author)
    return render_template('submitbook.html')


@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)

@app.route('/books')
def books():
    books = [{'name':'Book 1', 'author':'Author 1', 'cover':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWfvaffab6nCQJlCYUatLVhPmb831PjNnHtw&usqp=CAU'},
             {'name':'Book 2', 'author':'Author 2', 'cover':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWfvaffab6nCQJlCYUatLVhPmb831PjNnHtw&usqp=CAU'},
             {'name':'Book 3', 'author':'Author 3', 'cover':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWfvaffab6nCQJlCYUatLVhPmb831PjNnHtw&usqp=CAU'}
             ]
    return render_template('books.html',books=books)



if __name__ == "__main__":
    app.run(debug=True)










































# from flask import Flask, redirect, url_for, request, render_template
# from flask_sqlalchemy import SQLAlchemy
# import os

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# db = SQLAlchemy(app)

# class Book(db.Model):
#     name = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
#     author = db.Column(db.String(100), nullable=False)

# @app.route('/addbook')
# def addbook():
#     return render_template('addbook.html')  

# @app.route('/submitbook', methods=['POST'])
# def submitbook():
#     name = request.form['name']
#     author = request.form['author']
#     new_book = Book(name=name, author=author)
#     db.session.add(new_book)
#     db.session.commit()
#     return f'Book name is {name} and Author is {author}'

# @app.route('/')
# def index():
#     return render_template('index.html')  

# @app.route('/profile/<username>')
# def profile(username):
#     return render_template('profile.html', username=username)

# @app.route('/books')
# def books():
#     books = Book.query.all()
#     return render_template('books.html', books=books)

# if __name__ == "__main__":
#     # Create tables before running the app
#     with app.app_context():
#         db.create_all()

#     app.run(debug=True)






















# @app.route('/')

# def home():
#     return '<h1>This is the home page</h1>'


# @app.route('/profile/<username>')
# def profile(username):
#     return '<h1>This is the profile page for %s</h1>' % username

# @app.route('/profile/<int:id>')
# def profiles(id):
#     return '<h1>This is the profile page for %d</h1>' % id


# @app.route('/admin')
# def welcome_admin():
#     return 'welcome admin'

# @app.route('/guest/<guest>')
# def welcome_guest(guest):
#     return 'welcome guest %s' % guest

# @app.route('/user/<name>')
# def welcome_user(name):
#     if name == 'admin':
#         return redirect(url_for('welcome_admin'))
#     else:
#         return redirect(url_for('welcome_guest', guest=name))