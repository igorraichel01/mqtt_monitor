from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE,MEDIUM_FONT_SIZE,SMALL_FONT_SIZE,MINIMUM_WIDTH,MAXIMUM_WIDTH


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle() 

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')    
        self.setMinimumHeight(SMALL_FONT_SIZE * 2)  
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setMaximumWidth(MAXIMUM_WIDTH)
        self.setStyleSheet("color: white;")