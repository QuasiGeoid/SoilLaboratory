from PySide6.QtCore import Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QMainWindow, QApplication, QFileDialog)

from widgets.SoilLabWidget import SoilLabWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._soil_lab_widget = SoilLabWidget()
        self.setCentralWidget(self._soil_lab_widget)
        self.create_menus()
        self.setWindowTitle("Грунтовая лаборатория")

    def create_menus(self):
        file_menu = self.menuBar().addMenu("&Файл")

        open_action = self.create_action("&Открыть лаб объект...", file_menu, self.open_lab_object)
        save_action = self.create_action("&Сохранить лаб объект...", file_menu, self.save_lab_object)

    def create_action(self, text, menu, slot):
        action = QAction(text, self)
        menu.addAction(action)
        action.triggered.connect(slot)
        return action

    @Slot()
    def open_lab_object(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Выберите лабораторный объект", "c://", "XLSX Files (*.xlsx)")
        self._soil_lab_widget.import_from_excel(filename)
        # dialog.setFileMode(QFileDialog.Directory)
        # dir = QFileDialog.getExistingDirectory(self, "Выберите папку")
        # # dir = dir.replace("/", "\\")
        # if dir:
        #     filenames = [f for f in glob.glob(dir + "/*.xlsx")]
        #     for f in filenames:
        #         self._soil_lab_widget.read_from_file(f)

    def save_lab_object(self):
        filename, _ = QFileDialog.getSaveFileName(self, filter=".xlsx")
        if filename:
            self._soil_lab_widget.export_to_excel(filename)


if __name__ == "__main__":
    """ Run the application. """
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.resize(1000, 500)
    mw.show()
    sys.exit(app.exec())
