from PySide6.QtWidgets import (QLabel, QWidget, QPushButton, QVBoxLayout)

from source.LabResearchesList import lab_researches


class MainTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._title = 'Список исследований'
        self._layout = QVBoxLayout()
        self._lab_research_push_buttons = None
        self.add_buttons()
        self.setLayout(self._layout)

    @property
    def title(self):
        return self._title

    def add_buttons(self):
        self._lab_research_push_buttons = [QPushButton(lab_researches[i]) for i in range(len(lab_researches))]
        for push_button in self._lab_research_push_buttons:
            push_button.setFixedSize(300, 50)
            self._layout.addWidget(push_button)
