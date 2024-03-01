from django.test import TestCase
from labels.lib_src import LoginSafeTrack, ValidateTagSafeTrack
from sgi.settings import EMPRESA


class TESTValidateTagSafeTrack(TestCase):

    def setUp(self):
        self.login  = LoginSafeTrack()
        self.validate_tag_safe_track = ValidateTagSafeTrack(self.login)
        self.true_labels = [
            '001F7QY9',
            '001RTH00',
            '001RU895',
            '001RUZI5',
            '001RVQR0',
            '001RWI07',
            '001RX991',
            '001RY0I6',
            '001RYRR6',
            '001RZJ03',
            '001S0A94',
            '001S11I9',
            '001S1SR9',
            '001S2K06',
            '001S3B90',
            '001S42I5',
            '001S4TR5',
            '001S5L02',
            '001S6C97',
            '001S73I1',
        ]

        self.error_labels = [
            '001S0A90',
            '001S11I0',
            '001S1SR0',
            '001S2K00',
            '001S42I0',
            '001S4TR0',
            '001S5L00',
            '001S6C90',
            '001S73I0',
        ]

        self.true_ice_sku = '3031-018-002474-013-000750-66-213-000077'
        self.false_ice_sku = '3031-018-992474-013-000750-66-213-000099'
        return super().setUp()

    def test_true_labels(self):
        for label in self.true_labels:
            response = self.validate_tag_safe_track.validTag(
                label,
                self.true_ice_sku
            )
            self.assertTrue(response['is_valid'])

    def fail_labels(self):
        spected_data = {
            'name': 'BadRequestError',
            'httpCode': 400,
            'description': 'No found unique mark'
        }
        for label in self.error_labels:
            response = self.validate_tag_safe_track.validTag(
                label,
                self.true_ice_sku
            )
            self.assertDictEqual(
                response['error_message'],
                spected_data
            )
            self.assertEqual(response['status_code'], 400)

    def fail_sku_ice(self):
        valid_tag = '001RUZI5'
        fail_tag = '001RUXX5'

        spected_data_tag_valid = {
                'name': 'BadRequestError',
                'httpCode': 400,
                'description': 'ICE SKU no found'
        }

        spected_data_tag_and_ice_sku_invalid = {
            'name': 'BadRequestError',
            'httpCode': 400,
            'description': 'No found unique mark'
        }

        response = self.validate_tag_safe_track.validTag(
            valid_tag, self.false_ice_sku
        )
        self.assertDictEqual(spected_data_tag_valid, response['error_message'])

        response = self.validate_tag_safe_track.validTag(
            fail_tag, self.false_ice_sku
        )

        self.assertDictEqual(
            response['error_message'],
            spected_data_tag_and_ice_sku_invalid
        )
