from LabSample import LabSample
from Byux import Byux


class YieldStress(LabSample):
    def __init__(self, number=None, borehole=None, depth=None, soil_name=None,
                 byux=Byux()):
        super().__init__(number, borehole, depth, soil_name)
        self.byux = byux
        self._weight_evaporated_water = self.byux.weight_with_wet_soil - self.byux.weight_with_dry_soil
        self._weight_dry_soil = self.byux.weight_with_dry_soil - self.byux.weight_empty
        self._yield_stress = self._weight_evaporated_water / self._weight_dry_soil * 100

    @property
    def weight_evaporated_water(self):
        return self._weight_evaporated_water

    @property
    def weight_dry_soil(self):
        return self._weight_dry_soil

    @property
    def yield_stress(self):
        return self._yield_stress

