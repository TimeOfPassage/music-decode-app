# _*_ coding:utf-8 _*_
import os
import time

from PyQt6.QtCore import QObject, pyqtSignal

from utils.ncm_helper import NCMHelper


class ConvertMusic(QObject):
    refresh_signal = pyqtSignal(int)  # 信号

    def __init__(self):
        super().__init__()
        self.__output_dir = ""  # 输出目录
        self.__files = []  # 总文件数
        self.__success = 0  # 成功数
        self.__error = 0  # 失败数
        self.__success_map = {}  # 成功文件映射

    @property
    def success_map(self):
        return self.__success_map

    @property
    def output_dir(self):
        return self.__output_dir

    @output_dir.setter
    def output_dir(self, output_dir: str):
        self.__output_dir = output_dir

    @property
    def total(self):
        return len(self.files)

    @property
    def success_count(self):
        return self.__success

    @property
    def fail_count(self):
        return self.__error

    @property
    def files(self):
        return self.__files

    @files.setter
    def files(self, files: []):
        self.__files = files

    def run(self):
        if self.total <= 0:
            return
        for file in self.files:
            print(f"file: {file}")
            t = time.time()
            try:
                NCMHelper.start(file, self.output_dir)
                self.__success += 1
                self.__success_map[t] = file
            except Exception as e:
                print(f"convert fail: {file}, {e}")
                self.__error += 1
            finally:
                self.refresh_signal.emit(t)
