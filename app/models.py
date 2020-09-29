from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    blogs = db.relationship('Blog',backref = 'user',lazy="dynamic")
    email = db.Column(db.String(255),unique = True,index = True)
    
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)
   
    def __repr__(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
            return User.query.get(int(user_id))
   

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    description = db.Column(db.String(255))
    comments = db.relationship('Comment',backref = 'blog',lazy="dynamic")

    
    def save_blogs(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def clear_blogs(cls):
        Blog.all_blogs.clear()

    @classmethod
    def get_blogs(id):
        blogs=Blog.query.all()

        return blogs

   

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
   
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    comment = db.Column(db.String(255))

    def save_comments(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def clear_blogs(cls):
        Blog.all_blogs.clear()
    

    @classmethod
    def get_comments(id):
        all_comments=Comment.query.all()

        return all_comments

    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()    

class Subscribe(db.Model):
    __tablename__ = 'subsribes'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255))
    

    def __repr__(self):
        return f'User {self.username}'


class Quote:
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self,author,id,quote):
        self.author=author
        self.id =id
        self.quote=quote
        