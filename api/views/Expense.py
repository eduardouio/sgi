from lib_src.serializers import ExpenseSerializer
from paids.models.Expense import Expense
from rest_framework import generics

class ExpenseCreateView(generics.CreateAPIView):
    queryset = Expense.object.all()
    serializer_class = ExpenseSerializer


class ExpenseDeleteView(generics.DestroyAPIView):
    queryset = Expense.object.all()
    serializer_class = ExpenseSerializer


class ExpenseDetailView(generics.RetrieveAPIView):
    queryset = Expense.object.all()
    serializer_class = ExpenseSerializer


class ExpenseUpdateView(generics.UpdateAPIView):
    queryset = Expense.object.all()
    serializer_class = ExpenseSerializer