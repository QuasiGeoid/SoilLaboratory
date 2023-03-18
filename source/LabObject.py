from PySide6.QtCore import QDate


class LabObject:
    def __init__(self, name=None, date=QDate().currentDate()):
        self._name = name
        self._date = date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date
