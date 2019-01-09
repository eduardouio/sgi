from costings.models.Ledger import Ledger
from orders.models.Order import Order
from orders.models.OrderInvoice import OrderInvoice
from orders.models.OrderInvoiceDetail import OrderInvoiceDetail
from paids.models.Expense import Expense
from paids.models.PaidInvoice import PaidInvoice
from paids.models.PaidInvoiceDetail import PaidInvoiceDetail
from paids.models.RateExpense import RateExpense
from paids.models.RateIncoterm import RateIncoterm
from partials.models.InfoInvoice import InfoInvoice
from partials.models.InfoInvoiceDetail import InfoInvoiceDetail
from partials.models.Apportionment import Apportionment
from partials.models.ApportionmentDetail import ApportionmentDetail
from partials.models.Partial import Partial
from products.models.Product import Product
from suppliers.models.Supplier import Supplier
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class LedgerSerializer(ModelSerializer):
    class Meta:
        model = Ledger
        fields = ('__all__')


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')


class OrderInvoiceSerializer(ModelSerializer):
    valor_tasa_trimestral = serializers.FloatField()
    
    class Meta:
        model = OrderInvoice
        fields = ('__all__')


class OrderInvoiceDetailSerializer(ModelSerializer):
    class Meta:
        model = OrderInvoiceDetail
        fields = ('__all__')


class ExpenseSerializer(ModelSerializer):
    ordinal_parcial = serializers.IntegerField()    

    class Meta:
        model = Expense
        fields = ('__all__')


class PaidInvoiceSerializer(ModelSerializer):
    class Meta:
        model = PaidInvoice
        fields = ('__all__')


class PaidInvoiceDetailSerializer(ModelSerializer):
    class Meta:
        model = PaidInvoiceDetail
        fields = ('__all__')


class RateExpenseSerializer(ModelSerializer):
    class Meta:
        model = RateExpense
        fields = ('__all__')


class RateIncotermSerializer(ModelSerializer):
    class Meta:
        model = RateIncoterm
        fields = ('__all__')


class InfoInvoiceSerializer(ModelSerializer):
    total_value =serializers.FloatField()
    class Meta:
        model = InfoInvoice
        fields = ('__all__')


class InfoInvoiceDetailSerializer(ModelSerializer):
    class Meta:
        model = InfoInvoiceDetail
        fields = ('__all__')


class ApportionmentSerializer(ModelSerializer):
    class Meta:
        model = Apportionment
        fields = ('__all__')


class ApportionmentDetailSerializer(ModelSerializer):
    class Meta:
        model = ApportionmentDetail
        fields = ('__all__')


class PartialSerializer(ModelSerializer):
    ordinal_parcial = serializers.IntegerField()
    partial_url = serializers.CharField()
    
    class Meta:
        model = Partial
        fields = ('__all__')


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('__all__')