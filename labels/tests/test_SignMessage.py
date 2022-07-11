from django.test import TestCase
from labels.lib_src import SignMessageSafeTrack
from sgi.settings import EMPRESA


class TestSignMessage(TestCase):

    def setUp(self) -> None:
        self.sign_message = SignMessageSafeTrack()
        return super().setUp()

    def test_sign_individual(self):
        message = '{"uniqueMarks":["0035V4F0"],"iceSku":"3031-018-002474-013-000750-66-213-000077","businessId":"business_id"}'
        spected = {
            'message': '{"uniqueMarks":["0035V4F0"],"iceSku":"3031-018-002474-013-000750-66-213-000077","businessId":"business_id"}',
            'signature': '0x1fa165fcbdb563d4d6a05baae695e7efac82a0610b418388a129eecddee7d5a873d45ca6d2ee1df3062e11199366a3d93eac6f5d3c8e9c49136d07ad10408bdd1c'
        }
        spected['message'] = spected['message'].replace(
            'business_id', EMPRESA['safetrack']['wallet']['business_id']
        )

        result = self.sign_message.sign(message)

        self.assertEqual(result['signature'], spected['signature'])
        self.assertEqual(result['message'], spected['message'])
        