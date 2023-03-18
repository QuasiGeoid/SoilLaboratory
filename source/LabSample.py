from abc import ABC, abstractmethod


class LabSample(ABC):
    @abstractmethod
    def __init__(self, number=None, borehole=None, depth=None, soil_name=None):
        self._number = number
        self._borehole = borehole
        self._depth = depth
        self._soil_name = soil_name

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def borehole(self):
        return self._borehole

    @borehole.setter
    def borehole(self, borehole):
        self._borehole = borehole

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, depth):
        self._depth = depth

    @property
    def soil_name(self):
        return self._soil_name

    @soil_name.setter
    def soil_name(self, soil_name):
        self._soil_name = soil_name
