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
        
    def test_otx_ip_info_not_json(self):
        otx_ip_info = self.tested_app.post(
            '/otx/getinfoip',
            {"ip":"113.52.135.33"}
        )
        assert "Error" in otx_ip_info
        
    def test_otx_ip_info_no_ip(self):
        otx_ip_info = self.tested_app.post(
            '/otx/getinfoip',
            {"nothing":"again"}
        )
        assert "Error" in otx_ip_info
        
    '''def test_otx_url_info(self):
        otx_url_info = self.tested_app.post(
            '/otx/getinfourl',
            {"url":"http://google.com"}
        )
        assert "Error" in otx_ip_info'''
    
if __name__ == '__main__':
    unittest.main()
