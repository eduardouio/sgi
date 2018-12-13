from django.contrib import admin
from costings.models.Ledger import Ledger

class LedgerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ledger, LedgerAdmin)