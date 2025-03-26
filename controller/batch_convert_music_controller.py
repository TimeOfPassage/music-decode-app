# _*_ coding:utf-8 _*_
from PyQt6.QtCore import QThread, Qt
from PyQt6.QtWidgets import QFileDialog, QListWidgetItem

from model.convert_music import ConvertMusic
from view.batch_convert_music_view import BatchConvertMusicView


class BatchConvertMusicController:
    """View controller"""

    def __init__(self):
        self.view = BatchConvertMusicView()
        self.view.drop_area.clicked.connect(self.select_files)
        self.view.browse_btn.clicked.connect(self.select_output_path)
        self.view.clear_btn.clicked.connect(self.clear_filelist)
        self.view.start_btn.clicked.connect(self.start_convert)
        self.view.show()
        self.convert_music = ConvertMusic()
        self.convert_music.refresh_signal.connect(self.refresh_view)
        self.thread = QThread()
        self.convert_music.moveToThread(self.thread)
        self.thread.started.connect(self.convert_music.run)

    def refresh_view(self, key):
        self.view.success_label.setText(f"成功处理\n{self.convert_music.success_count}")
        self.view.fail_label.setText(f"处理失败\n{self.convert_music.fail_count}")
        print(f"refresh view: {key}")
        # 移除列表中的file
        # f = self.convert_music.success_map[key]
        # match: list[QListWidgetItem] = self.view.file_list.findItems(f, Qt.MatchFlag.MatchExactly)
        # if match:
        #     self.view.file_list.takeItem(self.view.file_list.row(match[0]))

    def start_convert(self):
        if self.convert_music.total <= 0:
            return
        self.thread.start()

    def select_files(self):
        self.view.drop_area.hide()
        files, _ = QFileDialog.getOpenFileNames(self.view, "选择文件")
        if files:
            self.view.file_list.addItems(files)
            self.convert_music.files = files
            self.view.total_label.setText(f"总文件数\n{self.convert_music.total}")
        else:
            self.view.drop_area.show()

    def select_output_path(self):
        path = QFileDialog.getExistingDirectory(self.view, "选择输出目录")
        if path:
            self.view.output_path.setText(path)
            self.convert_music.output_dir = path

    def clear_filelist(self):
        self.view.drop_area.show()
        self.view.file_list.clear()
        self.view.total_label.setText(f"总文件数\n0")
