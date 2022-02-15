from xmlrpc.client import Server
from app import create_app,db
from app.models import User
from flask_script import Manager,server

#Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
if __name__ == '__main__':
    manager.run()


