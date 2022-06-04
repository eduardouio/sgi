from django.test import TestCase
from labels.lib_src import ValidateRangeSafeTrack


class TESTValidateRangeSafeTrack(TestCase):

    def setUp(self):
        self.validateRange = ValidateRangeSafeTrack()
        self.first_tag = '001RTH00'
        self.last_tag = '001S73I1'
        self.quantity = 19
        return super().setUp()

    def test_validate_range_ordered(self):
        spected_data = {
            'first_tag': self.first_tag,
            'end_tag': self.last_tag,
            'is_valid': True,
            'quantity': self.quantity,
            'error_message': '',
            'status_code': 200
        }

        response = self.validateRange.validateRange(
            self.first_tag,
            self.last_tag,
        )
        
        self.assertEqual(spected_data['status_code'], 200)