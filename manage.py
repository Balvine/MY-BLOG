from app import create_app, db
from flask_script import Manager,server
from app.models import User
from flask_migrate import Migrate, MigrateCommand




@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Comment=Comment, Post=Post)


if __name__ == '__main__':
    
    manager.run()
