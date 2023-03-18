class Pycnometer:
    def __init__(self, name=None, weight_empty=None, weight_with_water=None,
                 weight_with_soil=None, weight_with_water_and_soil=None):
        self._name = name
        self._weight_empty = weight_empty
        self._weight_with_water = weight_with_water
        self._weight_with_soil = weight_with_soil
        self._weight_with_water_and_soil = weight_with_water_and_soil

    @property
    def name(self):
        return self._name

    @property
    def weight_empty(self):
        return self._weight_empty

    @property
    def weight_with_water(self):
        return self._weight_with_water

    @property
    def weight_with_soil(self):
        return self._weight_with_soil

    @property
    def weight_with_water_and_soil(self):
        return self._weight_with_water_and_soil
