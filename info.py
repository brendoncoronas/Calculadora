from PySide6.QtCore import Qt
from PySide6.QtWidgets import
from

class Info(QLabel):
    def (self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')

        # para ficar a direita
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
