from app import create_app
from flask_script import Manager,Server

# Create an app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

if __name__ == '__main__':
    manager.run(host='localhost', port=5003, debug=True)