from django.test import TestCase
from labels.lib_src import LoginSafeTrack


class TESTLoginSafeTrack(TestCase):

    def setUp(self):
        self.login_safe_track = LoginSafeTrack()
        return super().setUp()

    def test_success_get_token(self):
        spected_data = {
            'status_code': 200,
            'sub': '4e6b02f1-c83b-47a2-a76e-663569e8c71b',
            'error_message': '',
            }

        token = self.login_safe_track.get_token()
        self.assertEqual(token['sub'], spected_data['sub'])
        self.assertEqual(token['status_code'], spected_data['status_code'])
        self.assertEqual(token['error_message'], spected_data['error_message'])

    def error_get_token(self):
        token = self.login_safe_track.get_token()
        self.assertNotEqual(token['status_code'], 200)
        self.assertTrue(bool(token['error_message']))
