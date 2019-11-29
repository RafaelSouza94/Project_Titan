import unittest
from titan import api
from flask_webtest import TestApp

class TestAPI(unittest.TestCase):
    
    def test_help(self):
        # creating a client to interact with the app
        app = TestApp(api.app)
        
        # calling /api/ endpoint
        hello = app.get('/api')
        
        # asserting the body
        self.assertEqual(hello.json['Status'], 'Working')
        
if __name__ == '__main__':
    unittest.main()