from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QLabel


class ClickableLabel(QLabel):
    clicked = pyqtSignal()  # 定义点击信号

    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()  # 发射点击信号
        super().mousePressEvent(event)
