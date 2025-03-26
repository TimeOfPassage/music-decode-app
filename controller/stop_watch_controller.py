# _*_ coding:utf-8 _*_

from PyQt6.QtCore import QThread
from model.clock_server import ClockServer
from view.stop_watch_view import StopWatchView


class StopWatchController:
    """View controller"""

    def __init__(self):
        self.view = StopWatchView()
        self.view.btn.clicked.connect(self.btn_onclick)
        self.view.show()

        self.timeserver = ClockServer()
        self.timeserver.update_time.connect(self.view.lcd.display)

        self.thread = QThread()
        self.timeserver.moveToThread(self.thread)
        self.thread.started.connect(self.timeserver.run)
        self.thread.start()

    def btn_onclick(self):
        """按键响应事件"""
        if self.view.btn.text() == "Start":
            self.timeserver.isrun = True
            self.view.btn.setText("Stop")
        else:
            self.timeserver.isrun = False
            self.view.btn.setText("Start")
