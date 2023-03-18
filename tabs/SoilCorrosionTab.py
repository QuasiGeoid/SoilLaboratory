from tabs.AbstractSoilLabTab import AbstractSoilLabTabSoilSamples
from table_models.SoilCorrosionTableModel import SoilCorrosionTableModel


class SoilCorrosionTab(AbstractSoilLabTabSoilSamples):
    def __init__(self, table_model=SoilCorrosionTableModel(), parent=None):
        super().__init__(table_model, parent)
        self._title = "Коррозия грунта к стали"
