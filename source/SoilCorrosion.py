from LabSample import LabSample

CHARACTERISTICS = ["RESISTIVITY",
                   "CATHODIC_CURRENT_DENSITY",
                   ]
AGGRNESS_LEVELS = ["низкая",
                   "средняя",
                   "высокая",
                   ]


class SoilCorrosion(LabSample):
    def __init__(self, number=None, borehole=None, depth=None, soil_name=None,
                 resistivity=None, cathodic_current_density=None):
        super().__init__(number, borehole, depth, soil_name)
        self._resistivity = resistivity
        self._cathodic_current_density = cathodic_current_density

    @property
    def resistivity(self):
        return self._resistivity

    @resistivity.setter
    def resistivity(self, resistivity):
        self._resistivity = resistivity

    @property
    def cathodic_current_density(self):
        return self._cathodic_current_density

    @cathodic_current_density.setter
    def cathodic_current_density(self, cathodic_current_density):
        self._cathodic_current_density = cathodic_current_density

    def get_inaccuracy(self, characteristic):
        if characteristic == CHARACTERISTICS[0]:
            if self._resistivity:
                return self._resistivity * 0.02 + 0.1
        elif characteristic == CHARACTERISTICS[1]:
            if self._cathodic_current_density:
                return self._cathodic_current_density * 0.03

        return None

    def get_corrosion_aggrness_to_steel(self, characteristic):
        if characteristic == CHARACTERISTICS[0]:
            if self._resistivity:
                if self._resistivity > 50:
                    return AGGRNESS_LEVELS[0]
                elif 20 <= self._resistivity <= 50:
                    return AGGRNESS_LEVELS[1]
                elif 0 <= self._resistivity < 20:
                    return AGGRNESS_LEVELS[2]

        elif characteristic == CHARACTERISTICS[1]:
            if self._cathodic_current_density:
                if 0 <= self._cathodic_current_density <= 50:
                    return AGGRNESS_LEVELS[0]
                elif 50 < self._cathodic_current_density <= 200:
                    return AGGRNESS_LEVELS[1]
                elif self._cathodic_current_density > 200:
                    return AGGRNESS_LEVELS[2]

        return None
