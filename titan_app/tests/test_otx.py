import unittest
from flask_webtest import TestApp

from ..app import app

class TestOTX(unittest.TestCase):
    
    def test(self):
        '''
        **Basic test for OTX response**
        '''
        
        # creating a client to interact with the app
        tested_app = TestApp(app)
        
        # calling /otx/ endpoint
        otx_test = tested_app.get('/otx')
        
        # asserting the body
        self.assertEqual(otx_test.json['Status'], 'Working')
        
if __name__ == '__main__':
    unittest.main()
