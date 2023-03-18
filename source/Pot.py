class Pot:
    def __init__(self, name=None, weight_empty=None,
                 weight_with_soil_before_calcination=None, weight_with_soil_after_calcination=None):
        self._name = name
        self._weight_empty = weight_empty
        self._weight_with_soil_before_calcination = weight_with_soil_before_calcination
        self._weight_with_soil_after_calcination = weight_with_soil_after_calcination

    @property
    def name(self):
        return self._name

    @property
    def weight_empty(self):
        return self._weight_empty

    @property
    def weight_with_soil_before_calcination(self):
        return self._weight_with_soil_before_calcination

    @property
    def weight_with_soil_after_calcination(self):
        return self._weight_with_soil_after_calcination
