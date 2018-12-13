from  unittest import TestCase
from app_log import Log

class testLog(TestCase):
    def test_success_log(self):
        Log.success('Todo esta genial!')
        f = open('log.log','r')
        self.assertEqual(f,'Todo esta genial!')
