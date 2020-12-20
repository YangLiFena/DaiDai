import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import requests

from model.database import DataBase

class ShowImage(QWidget):
    def __init__(self, image):
        super().__init__()
        self.initUI(image)

    def initUI(self, image):
        # 设置窗口位置和大小
        hbox = QHBoxLayout(self)
        url = DataBase.get_image(image)
        res = requests.get(url)
        img = QImage.fromData(res.content)

        label = QLabel(self)
        label.setPixmap(QPixmap.fromImage(img))
        label.setScaledContents(True)
        # l1.move(10, 10)
        hbox.addWidget(label)
        self.setLayout(hbox)
        # self.setGeometry(100, 100, 620, 500)
        # self.show()

        # self.setGeometry(300, 300, 300, 220)
        # self.setWindowTitle('Icon')
        # # 设置窗口图标，引用图片
        # self.setWindowIcon(QIcon('icon_test1.png'))
        # self.show()


if __name__ == '__main__':
    # 创建应用程序
    app = QApplication(sys.argv)
    ex = ShowImage()
    ex.show()
    sys.exit(app.exec_())