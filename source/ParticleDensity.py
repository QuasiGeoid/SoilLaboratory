from LabSample import LabSample
from Pycnometer import Pycnometer


class ParticleDensity(LabSample):
    def __init__(self, number=None, borehole=None, depth=None, soil_name=None,
                 pycnometer=Pycnometer()):
        super().__init__(number, borehole, depth, soil_name)
        self.pycnometer = pycnometer
        self._weight_dry_soil = self.pycnometer.weight_with_soil - self.pycnometer.weight_empty
        self._density = self._weight_dry_soil / (self._weight_dry_soil + self.pycnometer.weight_with_water -
                                                 self.pycnometer.weight_with_water_and_soil)

    @property
    def weight_dry_soil(self):
        return self._weight_dry_soil

    @property
    def density(self):
        return self._density
