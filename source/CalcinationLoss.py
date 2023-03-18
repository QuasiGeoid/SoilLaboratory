from source.LabSample import LabSample
from source.Pot import Pot


class CalcinationLoss(LabSample):
    def __init__(self, number=None, borehole=None, depth=None, soil_name=None,
                 pot=Pot()):
        super().__init__(number, borehole, depth, soil_name)
        self.pot = pot
        self._loss = (self.pot.weight_with_soil_before_calcination - self.pot.weight_with_soil_after_calcination) / \
                     (self.pot.weight_with_soil_before_calcination - self.pot.weight_empty) * 100

    @property
    def loss(self):
        return self._loss
