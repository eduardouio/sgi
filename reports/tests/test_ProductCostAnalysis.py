from django.test import TestCase
from reports.lib_src import ProductCostAnalysis
from products.models import Product


class TESTProductCostAnalysis(TestCase):

    def test_get_info(self):
        pca = ProductCostAnalysis('01011080011917010750')
        product = Product.get_by_cod_contable('01011080011917010750')
        report = pca.get()
        self.assertEqual(len(report['history']), 1)
        self.assertEqual(report['product'], product)

    def test_info_product_does_exist(self):
        pca = ProductCostAnalysis('010110800119170750')
        product = Product.get_by_cod_contable('010110800119170750')
        report = pca.get()
        self.assertEqual(product, None)
        self.assertEqual(report, None)

    def test_get_info_deep(self):
        pca = ProductCostAnalysis('01011080011917010750', 5)
        product = Product.get_by_cod_contable('01011080011917010750')
        report = pca.get()
        self.assertEqual(len(report['history']), 1)
        self.assertEqual(report['product'], product)
