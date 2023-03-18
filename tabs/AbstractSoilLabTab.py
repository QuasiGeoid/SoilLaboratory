from PySide6.QtCore import (Qt, QSysInfo, QDate, Slot, QModelIndex)
from PySide6.QtWidgets import (QWidget, QTableView, QVBoxLayout, QAbstractItemView, QHeaderView, QPushButton)

from abc import ABC, abstractmethod


class AbstractSoilLabTab(QWidget):
    @abstractmethod
    def __init__(self, table_model, parent=None):
        super().__init__(parent)

        self._title = ''
        self._model = table_model

        self._table_view = QTableView()
        self._table_view.setModel(self._model)
        self._table_view.setEditTriggers(QAbstractItemView.DoubleClicked |
                                         QAbstractItemView.SelectedClicked)

        self._horizontal_header = self._table_view.horizontalHeader()
        self._horizontal_header.setDefaultAlignment(Qt.AlignHCenter | Qt.Alignment(Qt.TextWordWrap))
        self._horizontal_header.setMinimumHeight(150)
        if QSysInfo.productType() == "windows" and QSysInfo.productVersion().startswith("10"):
            self._horizontal_header.setStyleSheet(
                "QHeaderView::section{"
                "border-top:0px solid #D8D8D8;"
                "border-left:0px solid #D8D8D8;"
                "border-right:1px solid #D8D8D8;"
                "border-bottom: 1px solid #D8D8D8;"
                "background-color:white;"
                "padding:4px;"
                "}"
                "QTableCornerButton::section{"
                "border-top:0px solid #D8D8D8;"
                "border-left:0px solid #D8D8D8;"
                "border-right:1px solid #D8D8D8;"
                "border-bottom: 1px solid #D8D8D8;"
                "background-color:white;"
                "}")

        self._vertical_header = self._table_view.verticalHeader()

        self._layout = QVBoxLayout()
        self._layout.addWidget(self._table_view)
        self.setLayout(self._layout)

    @property
    def title(self):
        return self._title

    def get_headers_to_write_in_file(self):
        headers = []
        for i in range(self._model.columnCount()):
            headers.append(self._model.headerData(i, Qt.Horizontal))
        return headers

    def get_values_to_write_in_file(self):
        values = []
        for j in range(self._model.rowCount()):
            row = []
            for i in range(self._model.columnCount()):
                index = self._model.index(j, i)
                value = self._model.data(index)
                if isinstance(value, QDate):
                    value = value.toString('yyyy-MM-dd')
                row.append(value)
            values.append(row)
        return values

    def load_data_to_model(self, dict_table):
        for i,  (key, values) in enumerate(dict_table.items()):
            for j, value in enumerate(values):
                index = self._model.createIndex(j, i)
                self._model.setData(index, value)




class AbstractSoilLabTabSoilSamples(AbstractSoilLabTab):
    @abstractmethod
    def __init__(self, table_model, parent=None):
        super().__init__(table_model, parent)

        add_button = QPushButton("Добавить пробу")
        remove_button = QPushButton("Удалить пробу")

        add_button.clicked.connect(self.add_sample)
        self._layout.addWidget(add_button, 0, Qt.AlignCenter)
        remove_button.clicked.connect(self.remove_sample)
        self._layout.addWidget(remove_button, 0, Qt.AlignCenter)

    def load_data_to_model(self, dict_table):
        for i,  (key, values) in enumerate(dict_table.items()):
            while self._model.rowCount() < len(values):
                self.add_sample()
            for j, value in enumerate(values):
                index = self._model.createIndex(j, i)
                self._model.setData(index, value)

    @Slot()
    def add_sample(self):
        rows = self._model.rowCount()
        self._model.insertRows(rows)

    @Slot()
    def remove_sample(self):
        indexes = self._table_view.selectionModel().selectedRows()
        for index in indexes:
            self._model.removeRow(index.row())
