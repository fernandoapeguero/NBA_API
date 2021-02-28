from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
import os

from app import create_app
from models import db


app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
    port = int(os.environ.get("PORT", 5000))
    manager.add_command('runserver', Server(host='0.0.0.0', port=port, debug=True))

