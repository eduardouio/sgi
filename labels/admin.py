from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from labels.models import Label, OneLabel


class LabelAdmin(SimpleHistoryAdmin):
    list_display = (
        'id_label',
        'initial_range',
        'end_range',
        'quantity',
        'parcial',
    )

    search_fields = [
        'initial_range',
        'end_range',
        'parcial',
    ]


class OneLabelAdmin(SimpleHistoryAdmin):
    search_fields = [
        'cod_contable',
        'code_label',
        'bg_status',
    ]

    list_display = (
        'id_one_label',
        'cod_contable',
        'code_label',
        'bg_status',
        'date_created',
        'activated_date',
        'validated_date',
    )

    list_filter = (
        'bg_status',
    )


admin.site.register(Label, LabelAdmin)
admin.site.register(OneLabel, OneLabelAdmin)
