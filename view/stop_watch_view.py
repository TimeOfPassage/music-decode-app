# _*_ coding:utf-8 _*_


from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QLCDNumber, QPushButton, QVBoxLayout


class StopWatchView(QWidget):
    """
    秒表构造函数
    """

    def __init__(self):
        """
        构造函数
        """

        super().__init__()

        self.setWindowTitle("Stop Watch")
        self.setWindowIcon(QIcon(r"res/time04.ico"))

        self.initUI()

    def initUI(self):
        """
        初始化界面
        """

        # Set window location and size.
        self.setGeometry(400, 300, 300, 200)

        # 显示时间
        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(6)
        self.lcd.display('0.00')

        # Show button.
        self.btn = QPushButton('Start')
        self.btn.setStyleSheet('background-color:darkgray')

        # Set layout.
        vboxlayout = QVBoxLayout()
        self.setLayout(vboxlayout)

        vboxlayout.addWidget(self.lcd)
        vboxlayout.addSpacing(5)
        vboxlayout.addWidget(self.btn)
