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
        
    def test_otx_ip_info(self):
        otx_ip_info = self.tested_app.post(
            '/otx/getinfoip',
            {"ip":"113.52.135.33"}
        )
        assert "Error" in otx_ip_info
    
if __name__ == '__main__':
    unittest.main()
