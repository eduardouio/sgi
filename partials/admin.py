from django.contrib import admin
from partials.models.Partial import Partial
from partials.models.Apportionment import Apportionment
from partials.models.ApportionmentDetail import ApportionmentDetail
from partials.models.InfoInvoice import InfoInvoice
from partials.models.InfoInvoiceDetail import InfoInvoiceDetail

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