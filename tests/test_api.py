import unittest
from flask_basic import app as tested_app
from flask_webtest import TestApp

class TestAPI(unittest.TestCase):
    
    def test_help(self):
        # creating a client to interact with the app
        app = TestApp(tested_app)
        
        # calling /api/ endpoint
        hello = app.get('/api')
        
        # asserting the body
        self.assertEqual(hello.json['Status'], 'Working')
        
if __name__ == '__main__':
    unittest.main()