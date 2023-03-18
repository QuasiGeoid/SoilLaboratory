from PySide6.QtCore import (Qt, QAbstractTableModel, QModelIndex)

from source.LabObject import LabObject


class GeneralInfoTableModel(QAbstractTableModel):
    def __init__(self, lab_object=None, parent=None):
        super().__init__(parent)

        if lab_object is None:
            self._lab_object = LabObject()
        else:
            self._lab_object = lab_object

    def rowCount(self, index=QModelIndex()):
        """ Returns the number of rows the model holds. """
        return 1

    def columnCount(self, index=QModelIndex()):
        """ Returns the number of columns the model holds. """
        return 2

    def data(self, index, role=Qt.DisplayRole):
        """ Depending on the index and role given, return data. If not
            returning data, return None (PySide equivalent of QT's
            "invalid QVariant").
        """
        if not index.isValid():
            return None

        if not index.row() == 0:
            return None

        if role == Qt.DisplayRole or role == Qt.EditRole:
            name = self._lab_object.name
            date = self._lab_object.date

            if index.column() == 0:
                return name
            elif index.column() == 1:
                return date

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            if section == 0:
                return "Наименование"
            if section == 1:
                return "Дата"

    def setData(self, index, value, role=Qt.EditRole):
        """ Adjust the data (set it to <value>) depending on the given
            index and role.
        """
        if role != Qt.EditRole:
            return False

        if index.isValid() and index.row() == 0:
            if index.column() == 0:
                self._lab_object.name = value
            elif index.column() == 1:
                self._lab_object.date = value
            else:
                return False

        self.dataChanged.emit(index, index)
        return True

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index) |
                            Qt.ItemIsEditable)
