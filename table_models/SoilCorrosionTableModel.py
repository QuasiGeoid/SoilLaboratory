from PySide6.QtCore import (Qt, QAbstractTableModel, QModelIndex)

from source.SoilCorrosion import SoilCorrosion


class SoilCorrosionTableModel(QAbstractTableModel):
    def __init__(self, samples=None, parent=None):
        super().__init__(parent)

        if samples is None:
            self._samples = []
            self._samples.append(SoilCorrosion())
        else:
            self._samples = samples

    def rowCount(self, index=QModelIndex()):
        return len(self._samples)

    def columnCount(self, index=QModelIndex()):
        return 10

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if not 0 <= index.row() < len(self._samples):
            return None

        if role == Qt.DisplayRole or role == Qt.EditRole:
            i = index.row()

            number = self._samples[i].number
            borehole = self._samples[i].borehole
            depth = self._samples[i].depth
            soil_name = self._samples[i].soil_name
            resistivity = self._samples[i].resistivity
            resistivity_innacuracy = self._samples[i].get_inaccuracy("RESISTIVITY")
            cathodic_current_density = self._samples[i].cathodic_current_density
            cathodic_current_density_innacuracy = self._samples[i].get_inaccuracy("CATHODIC_CURRENT_DENSITY")

            j = index.column()
            if j == 0:
                return number
            elif j == 1:
                return borehole
            elif j == 2:
                return depth
            elif j == 3:
                return soil_name
            elif j == 4:
                return f'{resistivity:.0f}' if resistivity else ""
            elif j == 5:
                return f'{resistivity_innacuracy:.0f}' if resistivity_innacuracy else ""
            elif j == 6:
                return f'{cathodic_current_density:.0f}' if cathodic_current_density else ""
            elif j == 7:
                return f'{cathodic_current_density_innacuracy:.0f}' if cathodic_current_density_innacuracy else ""
            elif j == 8:
                return self._samples[i].get_corrosion_aggrness_to_steel("RESISTIVITY")
            elif j == 9:
                return self._samples[i].get_corrosion_aggrness_to_steel("CATHODIC_CURRENT_DENSITY")

            return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            if section == 0:
                return "№ пробы"
            if section == 1:
                return "№ скважины"
            if section == 2:
                return "Глубина отбора, м"
            if section == 3:
                return "Наименование грунта"
            if section == 4:
                return "Удельное сопротивление грунта (R), Ом·м"
            if section == 5:
                return "Погрешность"
            if section == 6:
                return "Плотность катодного тока (J), мА/м\u00B2"
            if section == 7:
                return "Погрешность"
            if section == 8:
                return "Агрессивность грунта к стали -" \
                       " по удельному сопротивлению грунта (R)"
            if section == 9:
                return "Агрессивность грунта к стали -" \
                       " по плотности катодного тока (J)"
        if orientation == Qt.Vertical:
            return section + 1

    def setData(self, index, value, role=Qt.EditRole):
        if role != Qt.EditRole:
            return False

        if index.isValid():
            i = index.row()
            j = index.column()
            sample = self._samples[i]
            if j == 0:
                sample.number = value
            elif j == 1:
                sample.borehole = value
            elif j == 2:
                sample.depth = value
            elif j == 3:
                sample.soil_name = value
            elif j == 4:
                try:
                    value = float(value)
                except ValueError:
                    sample.resistivity = ""
                sample.resistivity = value
            elif j == 6:
                try:
                    value = float(value)
                except ValueError:
                    sample.cathodic_current_density = ""
                sample.cathodic_current_density = value
            else:
                return False
        self.dataChanged.emit(index, index)
        return True

    def flags(self, index):
        if not index.isValid() or index.column() in (5, 7, 8, 9):
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index) |
                            Qt.ItemIsEditable)

    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        for row in range(rows):
            self._samples.append(SoilCorrosion())
        self.endInsertRows()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)

        del self._samples[position:position + rows]

        self.endRemoveRows()
        return True

    # def add_sample(self):
    #     self._samples.append(SoilCorrosion())
    #     self.layoutChanged.emit()
    #
    # def remove_sample(self):
    #     # self._samples.
    #     self.layoutChanged.emit()
