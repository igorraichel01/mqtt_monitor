from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMainWindow, QGridLayout, QLabel, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.cw = QWidget()
        self.g_layout = QGridLayout()

        self.cw.setLayout(self.g_layout)
        self.setCentralWidget(self.cw)
        self.setWindowTitle('Madruga MQTT Monitor')
        self.adjustSize()
        self.setMaximumSize(600, 400)
        
        self.log_display = QLabel()
        self.log_display.setStyleSheet("color: white;")
        self.log_display.setAlignment(Qt.AlignLeft)
        self.addWToVlayout(self.log_display, 4, 1)

    def addWToVlayout(self, widget: QWidget, row: int, col: int):
        self.g_layout.addWidget(widget, row, col)

    def showInfo(self, message: str):
        self.log_display.setText(f"INFO: {message}")

    def showWarning(self, message: str):
        self.log_display.setText(f"WARNING: {message}")

    def showError(self, message: str):
        self.log_display.setText(f"ERROR: {message}")
