import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QComboBox, QLineEdit, QListWidget, QFileDialog, QSizePolicy
)
from PyQt6.QtCore import Qt, pyqtSignal


class ClickableLabel(QLabel):
    clicked = pyqtSignal()  # 定义点击信号

    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()  # 发射点击信号
        super().mousePressEvent(event)

class BatchDecoderUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 主布局
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # 标题部分
        title = QLabel("批量文件解码工具")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        subtitle = QLabel("支持多种编码格式转换，快速批量处理")
        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # 文件拖拽区域
        self.drop_area = ClickableLabel("拖拽文件到此处或点击选择文件")
        self.drop_area.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.drop_area.setStyleSheet(
            "border: 2px dashed #aaa; padding: 30px;"
            "background-color: #f9f9f9;"
        )
        self.drop_area.setAcceptDrops(True)
        self.drop_area.setMinimumHeight(180)

        # select_btn = QPushButton("选择文件")
        # select_btn.setFixedWidth(100)

        drop_layout = QVBoxLayout()
        drop_layout.addWidget(self.drop_area)
        # drop_layout.addWidget(select_btn, 0, Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(drop_layout)

        # 水平布局
        settings_layout = QHBoxLayout()
        # 输出路径
        self.output_path = QLineEdit("")
        self.output_path.setReadOnly(True)
        settings_layout.addWidget(QLabel("输出路径"))
        settings_layout.addWidget(self.output_path)
        # 浏览按钮
        browse_btn = QPushButton("浏览")
        browse_btn.setFixedWidth(60)
        settings_layout.addWidget(browse_btn)
        # 开始解码按钮
        start_btn = QPushButton("开始解码")
        start_btn.setStyleSheet("background-color: #4CAF50; color: white;")
        settings_layout.addWidget(start_btn)
        # 添加到主布局
        main_layout.addLayout(settings_layout)
        # 垂直布局  label --> filelist --> clear btn
        # 文件列表框
        self.file_list = QListWidget()
        clear_btn = QPushButton("清空列表")
        file_list_layout = QVBoxLayout()
        file_list_layout.addWidget(QLabel("文件列表"))
        file_list_layout.addWidget(self.file_list)
        file_list_layout.addWidget(clear_btn, 0, Qt.AlignmentFlag.AlignRight)
        # 添加到主布局
        main_layout.addLayout(file_list_layout)
        # 统计信息
        stats_layout = QHBoxLayout()
        self.success_label = QLabel("成功处理\n0")
        self.fail_label = QLabel("处理失败\n0")
        self.total_label = QLabel("总文件数\n0")

        for label in [self.success_label, self.fail_label, self.total_label]:
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("border: 1px solid #ddd; padding: 10px;")
            stats_layout.addWidget(label)

        main_layout.addLayout(stats_layout)

        # 连接信号
        self.drop_area.clicked.connect(self.select_files)
        browse_btn.clicked.connect(self.select_output_path)
        clear_btn.clicked.connect(self.file_list.clear)

        self.setLayout(main_layout)
        self.setWindowTitle("文件解码工具")
        self.setMinimumSize(800, 600)

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "选择文件")
        if files:
            self.file_list.addItems(files)

    def select_output_path(self):
        path = QFileDialog.getExistingDirectory(self, "选择输出目录")
        if path:
            self.output_path.setText(path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BatchDecoderUI()
    window.show()
    sys.exit(app.exec())