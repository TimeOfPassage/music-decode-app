# _*_ coding:utf-8 _*_

import time

from PyQt6.QtCore import QObject, pyqtSignal


class ClockServer(QObject):
    """Clock server"""

    update_time = pyqtSignal(str)  # 时间更新信号
    __isrun = False  # Running flag.

    @property
    def isrun(self):
        """get run flag."""
        return self.__isrun

    @isrun.setter
    def isrun(self, value):
        """set run flag."""
        if type(value) is bool:
            self.__isrun = value

    def run(self):
        """start server"""
        while True:
            start_time = time.time()
            while self.isrun:
                self.update_time.emit("{0:.2f}".format(time.time() - start_time))
                time.sleep(0.01)
