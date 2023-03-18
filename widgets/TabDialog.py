import sys

from PySide6.QtWidgets import (QDialog, QWidget, QTabWidget, QVBoxLayout)
from GeneralInfo import GeneralInfo


class TabDialog(QDialog):
    def __init__(self, parent: QWidget = None):
        super.__init__(parent)
        tab_widget = QTabWidget()
        # Add all tabs for each table
        tab_widget.addTab(GeneralInfo(self), "Лабораторный Объект")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)