import unittest
# from flask_basic import app as tested_app
from flask_webtest import TestApp
import sys
#sys.path.insert(1, '../app/')
from titan.api import app

class TestAPI(unittest.TestCase):
    
    
    def test(self):
        '''
        **Basic test for API response**
        '''
        # creating a client to interact with the app
        tested_app = TestApp(app)
        
        # calling /api/ endpoint
        hello = tested_app.get('/api')
        tretas = tested_app.get('/tretas')
        
        # asserting the body
        self.assertEqual(hello.json['Status'], 'Working')
        self.assertEqual(tretas.json['Tretas'], 'Pesadas')
        
if __name__ == '__main__':
    unittest.main()


    