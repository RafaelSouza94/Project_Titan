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
            '/otx/getinfo/ip',
            {"ip":"113.52.135.33"}
        )
        assert "Error" in otx_ip_info
        
    def test_otx_ip_info_no_ip(self):
        otx_ip_info = self.tested_app.post_json(
            '/otx/getinfo/ip',
            {"nothing":"again"}
        )
        assert "Error" in otx_ip_info
        
    def test_otx_url_info_not_json(self):
        otx_url_info = self.tested_app.post(
            '/otx/getinfo/url',
            {"url":"google.com"}
        )
        assert "Error" in otx_url_info
        
    def test_otx_url_info_no_url(self):
        otx_url_info = self.tested_app.post_json(
            '/otx/getinfo/url',
            {"nothing":"again"}
        )
        assert "Error" in otx_url_info    
    
if __name__ == '__main__':
    unittest.main()
