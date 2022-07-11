from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from labels.models import Label


class LabelAdmin(SimpleHistoryAdmin):
    list_display = (
        'id_label',
        'initial_range',
        'end_range',
        'quantity',
        'parcial',
    )


admin.site.register(Label, LabelAdmin)
