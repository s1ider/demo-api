import unittest
import requests
import yaml


class TestCreateIssue(unittest.TestCase):
    def setUp(self):
        settings = yaml.load(open('settings.yaml').read())
        self.base_url = settings['base_url']
        login = settings['credentials']['login']
        pwd = settings['credentials']['password']
        self.creds = (login, pwd)

    def test_create_issue(self):
        url = self.base_url + '/issue'

        params = {
            'project': 'API',
            'summary': 'Awesome summary',
            'description': 'created by autotests'
        }

        r = requests.put(url, data=params, auth=self.creds)
        self.assertEquals(r.status_code, 201)

        location = r.headers['Location']
        r = requests.get(location, auth=self.creds)
        self.assertEquals(r.status_code, 200)

    def test_create_issue_without_project(self):
        url = self.base_url + '/issue'

        params = {
            'project': 'ZZZ',
            'summary': 'Awesome summary',
            'description': 'created by autotests'
        }

        r = requests.put(url, data=params, auth=self.creds)
        self.assertEquals(r.status_code, 403)



if __name__ == '__main__':
    unittest.main()
