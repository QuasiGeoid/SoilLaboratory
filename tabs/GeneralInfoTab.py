from tabs.AbstractSoilLabTab import AbstractSoilLabTab
from table_models.GeneralInfoTableModel import GeneralInfoTableModel


class GeneralInfoTab(AbstractSoilLabTab):
    """Class to describe a laboratory research object."""

    def __init__(self, table_model=GeneralInfoTableModel(), parent=None):
        super().__init__(table_model, parent)
        self._title = "Лаб объект"

