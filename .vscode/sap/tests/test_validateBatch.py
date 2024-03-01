from django.test import TestCase
from labels.lib_src import ValidateBatchSafeTrack
from labels.lib_src import LoginSafeTrack


class TESTValidateBacth(TestCase):

    def setUp(self):
        self.batchs = [
            {
                'batch': 'LO000536',
                'first_tag': '0037HDN3',
                'last_tag': '0037I5E8',
                'quantity': 1000
            },
            {
                'batch': 'LO000528',
                'first_tag': '0037IX90',
                'last_tag': '0037JP05',
                'quantity': 1000
            },
            {
                'batch': 'LO001354',
                'first_tag': '002Y4Z64',
                'last_tag': '002Y5QX6',
                'quantity': 1000
            },
            {
                'batch': 'LO001351',
                'first_tag': '002ZSRZ1',
                'last_tag': '002ZTJQ6',
                'quantity': 1000
            },
            {
                'batch': 'LO001355',
                'first_tag': '002ZS068',
                'last_tag': '002ZSRX5',
                'quantity': 1000
            },
        ]
        login = LoginSafeTrack()
        self.validate_batch = ValidateBatchSafeTrack(login)
        return super().setUp()

    def test_batch(self):
        for bacth in self.batchs:
            result = self.validate_batch.validate(bacth['batch'])
            for key in bacth:
                self.assertEqual(result[key], bacth[key])

    def test_bad_batch(self):
        batchs = [
            {
                'batch': 'LO9999999',
                'first_tag': '0037HDN3',
                'last_tag': '0037I5E8',
                'quantity': 1000
            },
            {
                'batch': 'LO00052976',
                'first_tag': '0037IX90',
                'last_tag': '0037JP05',
                'quantity': 1000
            },
        ]

        for bacth in batchs:
            result = self.validate_batch.validate(bacth['batch'])
            self.assertEqual(result['status'], 500)
