# _*_ coding:utf-8 _*_

import sys

from PyQt6.QtWidgets import QApplication

from controller.batch_convert_music_controller import BatchConvertMusicController

if __name__ == "__main__":
    """main"""
    app = QApplication(sys.argv)
    # stopwatch = StopWatchController()
    batch_convert_music = BatchConvertMusicController()
    sys.exit(app.exec())
