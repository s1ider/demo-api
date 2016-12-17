from base_api_test import BaseAPITest
import requests


class TestDeleteIssue(BaseAPITest):
    def test_delete_issue(self):
        issue_id = self.create_issue()
        url = self.base_url + '/issue/' + issue_id

        r = requests.delete(url, cookies=self.cookies)
        self.assertEquals(r.status_code, 200)

        r = requests.get(url, cookies=self.cookies)
        self.assertEquals(r.status_code, 404)

    def test_delete_unexisted_issue(self):
        issue_id = 'NOTEXISTED'
        url = self.base_url + '/issue/' + issue_id

        r = requests.delete(url, cookies=self.cookies)
        self.assertEquals(r.status_code, 404)
