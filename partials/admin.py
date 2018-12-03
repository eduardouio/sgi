from django.contrib import admin
from .models import Partial, Apportionment, ApportionmentDetail, InfoInvoice, InfoInvoiceDetail

class PartialAdmin(admin.ModelAdmin):
    pass


class ApportionmentAdmin(admin.ModelAdmin):
    pass


class ApportionmentDetailAdmin(admin.ModelAdmin):
    pass


class InfoInvoiceAdmin(admin.ModelAdmin):
    pass


class InfoInvoiceDetailAdmin(admin.ModelAdmin):
    pass

admin.site.register(Partial, PartialAdmin)
admin.site.register(Apportionment, ApportionmentAdmin)
admin.site.register(ApportionmentDetail, ApportionmentDetailAdmin)
admin.site.register(InfoInvoice, InfoInvoiceAdmin)
admin.site.register(InfoInvoiceDetail, InfoInvoiceDetailAdmin)