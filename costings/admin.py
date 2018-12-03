from django.contrib import admin
from .models import Ledger

class LedgerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ledger, LedgerAdmin)