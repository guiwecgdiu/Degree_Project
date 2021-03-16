from flask_script import Manager, Server
from src import app
from src import db
from src.Models.Users import User
from src.Models.Staffs import Staff
from src.Models.Reservations import Reservation
from src.Models.Pets import Pet
from src.Models.Accounts import Accounts
from flask_migrate import Migrate, MigrateCommand

# 自定义的控制台
# 控制台 输入 python script.py shell 可以打开自定义的控制台，类似于flask shell
# 输入 python script.py xxx 可以使用自定义命令，比如server是启动服务器

manager = Manager(app)
migrate=Migrate(app,db)

# 自定义命令 xxx
manager.add_command("server",Server())
manager.add_command('db', MigrateCommand)


@manager.shell
# 用shell 命令创建命令行
def make_shell_context():
# 返回的字典会告诉Flask Script在打开命令行时，执行一些默认的导入工作
    return dict(app=app, db=db, Pet=Pet, User=User, Staff=Staff, Reservation=Reservation,Accounts=Accounts)

if __name__=="__main__":
    manager.run()