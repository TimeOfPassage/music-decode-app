# _*_ coding:utf-8 _*_
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QListWidget

from widgets.clickable_label import ClickableLabel


class BatchConvertMusicView(QWidget):
    """
    秒表构造函数
    """

    def __init__(self):
        """
        构造函数
        """
        super().__init__()
        self.setWindowTitle("批量转换网易云ncm文件")
        self.setMinimumSize(800, 600)
        # self.setWindowIcon(QIcon(r"res/time04.ico"))
        self.setup_ui()

    def setup_ui(self):
        """
        初始化界面
        """

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
        drop_layout = QVBoxLayout()
        drop_layout.addWidget(self.drop_area)
        main_layout.addLayout(drop_layout)

        # 水平布局
        settings_layout = QHBoxLayout()
        # 输出路径
        self.output_path = QLineEdit("")
        self.output_path.setReadOnly(True)
        settings_layout.addWidget(QLabel("输出路径"))
        settings_layout.addWidget(self.output_path)
        # 浏览按钮
        self.browse_btn = QPushButton("浏览")
        self.browse_btn.setFixedWidth(60)
        settings_layout.addWidget(self.browse_btn)
        # 开始解码按钮
        self.start_btn = QPushButton("开始解码")
        self.start_btn.setStyleSheet("background-color: #4CAF50; color: white;")
        settings_layout.addWidget(self.start_btn)
        # 添加到主布局
        main_layout.addLayout(settings_layout)
        # 垂直布局  label --> filelist --> clear btn
        # 文件列表框
        self.file_list = QListWidget()
        self.clear_btn = QPushButton("清空列表")
        file_list_layout = QVBoxLayout()
        file_list_layout.addWidget(QLabel("文件列表"))
        file_list_layout.addWidget(self.file_list)
        file_list_layout.addWidget(self.clear_btn, 0, Qt.AlignmentFlag.AlignRight)
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

        # 统计信息添加到主布局
        main_layout.addLayout(stats_layout)

        # 设置整体布局
        self.setLayout(main_layout)
