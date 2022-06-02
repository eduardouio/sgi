from django.test import TestCase
from labels.lib_src import LoginSafeTrack


class TESTLoginSafeTrack(TestCase):

    def setUp(self):
        self.login_safe_track = LoginSafeTrack()
        return super().setUp()

    def test_get_jwt(self):
        self.login_safe_track.get_jwt()
