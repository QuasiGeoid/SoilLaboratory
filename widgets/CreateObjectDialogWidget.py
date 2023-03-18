from PySide6.QtCore import (Qt, QDate)

from PySide6.QtWidgets import (QLabel, QDialog, QDateEdit, QDialogButtonBox, QLineEdit, QGridLayout, QVBoxLayout)


class CreateObjectDialogWidget(QDialog):
    """ A dialog to create a laboratory research object. """
    def __init__(self, parent=None):
        super().__init__(parent)
        name_label = QLabel("Наименование")
        date_label = QLabel("Дата")
        button_box = QDialogButtonBox(QDialogButtonBox.Ok |
                                      QDialogButtonBox.Cancel)
        self._name_text = QLineEdit()
        self._date_text = QDateEdit(QDate.currentDate())

        grid = QGridLayout()
        grid.setColumnStretch(1, 2)
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self._name_text, 0, 1)
        grid.addWidget(date_label, 1, 0)
        grid.addWidget(self._date_text, 1, 1)

        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addWidget(button_box)

        self.setLayout(layout)
        self.setWindowTitle("Создание объекта лабораторных исследований")

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

    @property
    def name(self):
        return self._name_text

    @property
    def date(self):
        return self._date_text


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    dialog = CreateObjectDialogWidget()
    if dialog.exec():
        name = dialog.name
        date = dialog.date
