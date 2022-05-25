from django.test import TestCase

from labels.lib_src import LoginSafeTrack
from logs.app_log import loggin


class TESTLoginSafeTrack(TestCase):

    def setUp(self):
        self.login_safe_track = LoginSafeTrack()
        return super().setUp()

    def test_get_jwt(self):
        loggin('t', 'Test get_jwt')
        self.login_safe_track.get_jwt()