from flask import render_template,request,redirect,url_for,abort
 
from . import main
from .forms import BlogForm,UpdateProfile
# from .. import db

from .forms import BlogForm

from flask_login import login_required 

from flask import render_template,redirect,url_for, abort
from . import main

from .. import db,photos
from ..models import User,Blog,Comment,Subscribe
from .forms import BlogForm,CommentForm,SubscriptionForm

from ..request import get_quotes
from ..email import mail_message

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quotes = get_quotes()
    
    all_blogs = Blog.get_blogs()
    
    title = 'Home - Welcome to The best blogs Website Online'

    return render_template('index.html', title = title ,all_blogs = all_blogs,quotes=quotes)


@main.route('/blog/new', methods = ['GET','POST'])
def new_blog():
    form = BlogForm()
    blogs =Blog.get_blogs()

    if form.validate_on_submit():
       
        description = form.description.data
        new_blog = Blog(description=description)
        new_blog.save_blogs()
        return redirect(url_for('main.index',description=description))
        

    title = 'Welcome to The best blogs Website Online'
    return render_template('blog.html',title = title, Blog_form=form,blogs=blogs)


@main.route('/blogs')
def dipslay_blogs():
   all_blogs = Blog.blogs()
   print(all_blogs)
   return render_template("index.html",all_blogs=all_blogs) 

@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def create_blog():
   form = BlogForm()
   Blog = blog.Blog


   if form.validate_on_submit():
       
       teaser = form.teaser.data
       blog = form.blog.data
       new_blog = Blog(user_id=current_user.id,teaser=teaser, blog=blog)
       new_blog.save_new()
       return redirect(url_for('.index',blog = blog))

   
   return render_template('blog.html', blog_form=form)


@main.route('/blogs')
def display_blog():
   all_blogs = Blog.get_blogs()
   print(all_blogs)
   return render_template("index.html",all_blogs=all_blogs)

@main.route('/comment/delete/<int:id>')

def delete_comment(id):

  
  comment=Comment.query.filter_by(id=id).all()
  if comment is not None:
      comment.delete_comment()

  db.session.add(comment)
  db.session.commit()    

  
  return redirect('.main.index')   


@main.route('/comment/new/<int:id>', methods = ['GET','POST'])
def new_comment(id):
    form = CommentForm()
    comment = form.comment.data
    
    if form.validate_on_submit():
        new_comment = Comment(blog_id =id ,comment=comment)
        new_comment.save_comments()
        return redirect(url_for('main.index'))
    
    comments=Comment.query.filter_by(blog_id=id).all()

    title = 'Welcome to The best blogs Website Online'
    return render_template('comment.html',comments=comments,comment_form=form)


@main.route('/comments')
def dipslay_comments():
  
   all_comments = Comment. get_comments()
   print(all_comments)
   return render_template("comment.html",all_comments=all_comments) 



@main.route('/subscribe', methods = ['GET','POST'])
def new_subscription():
    form = SubscriptionForm()
    email= form.email.data
    

    if form.validate_on_submit():
        new_subscription = Subscribe(email=email)
        db.session.add(new_subscription)
        db.session.commit()
        mail_message("Welcome to quote and blogs","email/welcome_user",new_subscription.email,new_subscription=new_subscription)
       

        return redirect(url_for('main.index'))
   
    return render_template('subscription.html',form=form)






@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))




