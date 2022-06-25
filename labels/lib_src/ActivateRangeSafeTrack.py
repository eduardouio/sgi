from labels.lib_src import ValidateRangeSafeTrack
from logs.app_log import loggin
from labels.models import Label
from orders.models import OrderInvoiceDetail


class ActivateRangeSafeTrack(ValidateRangeSafeTrack):
    """clase encargada de actvar un rango de etiquetas

    Args:
        ValidateRangeSafeTrack (_type_): _description_
    """

    def __init__(self):
        super().__init__()

    def activate_ranges(self, ranges):
        pass

    def sign(self):
        pass
