from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db
bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')

def index():
  # get all posts
  db = get_db()
  posts = db.query(Post).order_by(Post.created_at.desc()).all() # getting errors with this and
  # Error: posts = db.query(Post).order_by(Post.created_at.desc()).all() AttributeError: 'sessionmaker' object has no attribute 'query'
  

  return render_template(
    'homepage.html',
    posts=posts # and this one, error: 
  )

@bp.route('/login')

def login():

  return render_template('login.html')

@bp.route('/post/<id>')

def single(id):
  
  # get single post by id
  db = get_db()
  
  post = db.query(Post).filter(Post.id == id).one()
  
  # render single post template

  return render_template(

    'single-post.html',

    post=post
  )
  
  
  
  # mysql -u root -p
  # USE python_news_db;
  # .\venv\Scripts\activate
  # python -m flask run