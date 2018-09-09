from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Pitch, Categeory
from flask_migrate import Migrate, MigrateCommand


app = create_app('development')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Pitch=Pitch, Category=Categeory)


if __name__ == '__main__':
    manager.run()
