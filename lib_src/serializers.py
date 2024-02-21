from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from costings.models import Ledger
from orders.models import Order, OrderInvoice, OrderInvoiceDetail
from paids.models import (Expense, PaidInvoice, PaidInvoiceDetail, RateExpense,
                          RateIncoterm)
from partials.models import (Apportionment, ApportionmentDetail, InfoInvoice,
                             InfoInvoiceDetail, Partial)
from products.models import Product
from suppliers.models import Supplier
from filemanager.models import FileManager
from labels.models import Label


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
    ordinal_parcial = serializers.IntegerField(required=False)
    partial_url = serializers.CharField(required=False)
    
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


class FileManagerSerializer(ModelSerializer):
    class Meta:
        model = FileManager
        fields = ('__all__')


class LabelSerializer(ModelSerializer):
    class Meta:
        model = Label
        fields = ('__all__')