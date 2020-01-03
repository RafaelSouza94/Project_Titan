import unittest
import requests_mock
import json
from flask_webtest import TestApp

from ..app import app

class TestOTX(unittest.TestCase):
    
    def setUp(self):
        self.tested_app = TestApp(app)
        self.adapter = requests_mock.Adapter()
    
    def test_otx_response(self):    
        otx_test = self.tested_app.get('/otx/')
        self.assertEqual(otx_test.json['Status'], 'Working')
        
    '''def test_otx_ip_info(self):
        mocked_value = json.dumps({'ip':'info'})
        self.adapter.register_uri(
            'POST', 
            'http://0.0.0.0:5000/otx/getinfoip', 
            text=mocked_value
        ) 
        otx_ip_info = self.tested_app.post_json(
            '/otx/getinfoip',
            {"ip":"113.52.135.33"}
        )
        assert "Error" not in otx_ip_info'''
    
if __name__ == '__main__':
    unittest.main()
