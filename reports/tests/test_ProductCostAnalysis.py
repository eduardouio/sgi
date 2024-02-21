from django.test import TestCase
from reports.lib_src import ProductCostAnalysis
from products.models import Product


class TESTProductCostAnalysis(TestCase):

    def test_get_last_item(self):
        my_product = Product.objects.get(pk='02012130020202010750')
        report = ProductCostAnalysis('02012130020202010750', 1).get()
        last_cost = round(float(report['history'][0]['costo_botella']), 2)

        self.assertEqual(report['product'], my_product)
        self.assertEqual(report['history'].__len__(), 1)
        self.assertEqual(last_cost, 10.03)

    def test_get_all_items_for_product(self):
        my_product = Product.objects.get(pk='01011080010207010750')
        report = ProductCostAnalysis('01011080010207010750').get()

        self.assertEqual(report['product'], my_product)
        self.assertEqual(report['history'].__len__(), 33)
        self.assertEqual(
            round(float(report['history'][0]['costo_botella']), 2), 
            2.77
        )
        self.assertEqual(
            round(float(report['history'][-1]['costo_botella']), 2),
            2.66
        )

    def test_product_not_found(self):
        report = ProductCostAnalysis('not-found-product').get()
        self.assertIsNone(report)
