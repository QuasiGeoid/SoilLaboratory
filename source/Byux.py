class Byux:
    def __init__(self, name=None, weight_empty=None, weight_with_wet_soil=None, weight_with_dry_soil=None):
        self._name = name
        self._weight_empty = weight_empty
        self._weight_with_wet_soil = weight_with_wet_soil
        self._weight_with_dry_soil = weight_with_dry_soil

    @property
    def name(self):
        return self._name

    @property
    def weight_empty(self):
        return self._weight_empty

    @property
    def weight_with_wet_soil(self):
        return self._weight_with_wet_soil

    @property
    def weight_with_dry_soil(self):
        return self._weight_with_dry_soil

