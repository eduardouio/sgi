import json
import os

from django.test import TestCase
from datetime import date

from lib_src import LocalWarenhouseArrivals


class LocalWarenhouseArrivalsTEST(TestCase):

    def setUp(self):
        return super().setUp()

    def test_dates(self):
        spected_data = [
            {'year': 2019, 'month': 7, 'start': date(2019, 7, 1), 'end': date(2019, 7, 31)},
            {'year': 2019, 'month': 2, 'start': date(2019, 2, 1), 'end': date(2019, 2, 28)},
            {'year': 2020, 'month': 2, 'start': date(2020, 2, 1), 'end': date(2020, 2, 29)},
            {'year': 2019, 'month': 0, 'start': date(2019, 1, 1), 'end': date(2019, 12, 31)},
            {'year': 2020, 'month': 0, 'start': date(2020, 1, 1), 'end': date(2020, 12, 31)},
        ]
        for spec in spected_data:
            local_arrivals = LocalWarenhouseArrivals(
                spec['year'], spec['month']
                )

            self.assertEqual(local_arrivals.date_start, spec['start'])
            self.assertEqual(local_arrivals.date_end, spec['end'])

    def test_get_year_orders(self):
        '''comprobamos los pedidos llegados en un anio'''
        path_base = os.sep.join(
            os.path.abspath(__file__).split(os.sep)[:-1] + ['data/']
            )
        f_orders = open(path_base + 'orders_year_2019.json', 'r')
        orders_data = f_orders.read()
        f_partials = open(path_base + 'partials_year_2019.json', 'r')
        partials_data = f_partials.read()

        spected_data = {
            'consumo': json.loads(orders_data),
            'almagro': json.loads(partials_data),
        }
        data = LocalWarenhouseArrivals(2019, 0).get()
        self.assertIsInstance(data, dict)
        self.assertEqual(
            spected_data['almagro'].__len__(),
            data['almagro'].__len__(),
        )
        self.assertEqual(
            spected_data['consumo'].__len__(),
            data['consumo'].__len__(),
            )

    def test_get_orders_in_month(self):
        '''comprobamos los pedidos llegados en un mes'''      
        self.assertTrue(1)
