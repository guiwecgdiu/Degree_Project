from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_dropzone import Dropzone
from flask_avatars import Avatars
from flask_socketio import SocketIO

mail=Mail()
moment=Moment()
db=SQLAlchemy()
bootstrap=Bootstrap()
migrate=Migrate()
dropzone=Dropzone()
avatars=Avatars()
socketio = SocketIO()

