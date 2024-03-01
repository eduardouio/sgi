from django.test import TestCase
from labels.lib_src import ValidateRangeSafeTrack
from labels.lib_src import LoginSafeTrack
from logs.app_log import loggin


class TESTValidateRangeSafeTrack(TestCase):

    def setUp(self):
        loggin('t', 'inciamos validado de los rangos')
        self.spected_data = {
            'first_tag': '001RTH00',
            'last_tag': '001S73I1',
            'quantity': 19,
            'status_code': 200,
            'cheked_reverse': False,
            'concordance': True,
            'difference': 0,
        }
        login = LoginSafeTrack()
        self.validateRange = ValidateRangeSafeTrack(login)

    def test_validate_range_ordered(self):
        response = self.validateRange.validate(
            self.spected_data['first_tag'],
            self.spected_data['last_tag'],
            self.spected_data['quantity']
        )

        for test in self.spected_data:
            self.assertEqual(self.spected_data[test], response[test])

    def test_validate_range_unordered(self):
        self.spected_data['cheked_reverse'] = True
        response = self.validateRange.validate(
            self.spected_data['last_tag'],
            self.spected_data['first_tag'],
            self.spected_data['quantity']
        )

        for test in self.spected_data:
            self.assertEqual(self.spected_data[test], response[test])

    def test_invalid_range(self):
        self.spected_data['first_tag'] = '001S73ZZ'
        self.spected_data['last_tag'] = '331RTH00'
        self.spected_data['concordance'] = False
        self.spected_data['difference'] = 29981
        self.spected_data['quantity'] = 19

        response = self.validateRange.validate(
            self.spected_data['first_tag'],
            self.spected_data['last_tag'],
            self.spected_data['quantity']
        )
        for test in self.spected_data:
            if test != 'quantity':
                self.assertEqual(self.spected_data[test], response[test])
