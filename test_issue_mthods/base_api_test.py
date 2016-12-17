import unittest
import requests
import yaml
import xmltodict


class BaseAPITest(unittest.TestCase):
    def setUp(self):
        self.settings = yaml.load(open('settings.yaml').read())
        self.base_url = self.settings['base_url']

        self._login()

    def _login(self):
        url = self.base_url + '/user/login'

        params = {
            'login': self.settings['credentials']['login'],
            'password': self.settings['credentials']['password']
        }

        r = requests.post(url, data=params)
        self.assertEquals(r.status_code, 200)
        self.cookies = r.cookies

    def create_issue(self):
        url = self.base_url + '/issue'
        params = {
            'project': 'API',
            'summary': 'test issue plz delete me',
            'description': 'some description'
        }

        r = requests.put(url, data=params, cookies=self.cookies)
        self.assertEquals(r.status_code, 201, r.text)

        location = r.headers['Location']
        issue_id = location.split('/')[-1]

        return issue_id







