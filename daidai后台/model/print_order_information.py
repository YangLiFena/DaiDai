#coding=gbk
import sys
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QLineEdit, QToolButton, QGroupBox, QMessageBox)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon

# 纸张大小
# 打印颜色
# 打印类型
# 打印份数
# 用户备注



class PrintOrderInfo(QGroupBox):
    '''
    编辑书本信息的界面
    传入{
        'SID': str,
        'SNAME': str,
        'DEPARTMENT': str,
        'MAJOR': str,
        'MAX': int
    }
    返回{
        'SID': str,
        'SNAME': str,
        'PASSWORD': str,
        'DEPARTMENT': str,
        'MAJOR': str,
        'MAX': int
    }
    '''
    # after_close = pyqtSignal(dict)

    def __init__(self, good_info: dict):
        super().__init__()
        self.good_info = good_info

        self.title = QLabel()
        self.title.setText('打印详情页')

        self.subTitle = QLabel()
        self.subTitle.setText('打印详情')

        self.sizeInput = QLineEdit()
        self.sizeInput.setFixedSize(400, 40)
        self.sizeInput.setText('纸张大小：' + self.good_info['SIZE'])
        self.sizeInput.setEnabled(False)

        self.colorInput = QLineEdit()
        self.colorInput.setFixedSize(400, 40)
        self.colorInput.setText('打印颜色：' + self.good_info['COLOR'])
        self.colorInput.setEnabled(False)

        self.wayInput = QLineEdit()
        self.wayInput.setFixedSize(400, 40)
        self.wayInput.setText('打印类型：' + self.good_info['WAY'])
        self.wayInput.setEnabled(False)

        self.numInput = QLineEdit()
        self.numInput.setFixedSize(400, 40)
        self.numInput.setText('打印份数：' + self.good_info['NUM'])
        self.numInput.setEnabled(False)

        self.messageInput = QLineEdit()
        self.messageInput.setFixedSize(400, 40)
        self.messageInput.setText('备注：' + self.good_info['MESSAGE'])
        self.messageInput.setEnabled(False)


        # 退出
        self.back = QToolButton()
        self.back.setText('退出')
        self.back.setFixedSize(400, 40)
        self.back.clicked.connect(self.close)

        self.btnList = [
            self.sizeInput,
            self.colorInput,
            self.wayInput,
            self.numInput,
            self.messageInput,
        ]

        self.bodyLayout = QVBoxLayout()
        self.bodyLayout.addWidget(self.title)
        self.bodyLayout.addWidget(self.subTitle)
        for i in self.btnList:
            self.bodyLayout.addWidget(i)
        # self.bodyLayout.addWidget(self.submit)
        self.bodyLayout.addWidget(self.back)

        self.setLayout(self.bodyLayout)
        self.initUI()


    def initUI(self):
        self.setFixedSize(422, 360)
        self.setWindowTitle('打印订单详情')
        self.setWindowIcon(QIcon('icon/person.png'))
        self.setMyStyle()

    def setMyStyle(self):
        self.setStyleSheet('''
        QWidget{
            background-color: white;
        }
        QLineEdit{
            border:0px;
            border-bottom: 1px solid rgba(229, 229, 229, 1);
            color: grey;
        }
        QToolButton{
            border: 0px;
            background-color:rgba(52, 118, 176, 1);
            color: white;
            font-size: 25px;
            font-family: 微软雅黑;
        }
        QGroupBox{
            border: 1px solid rgba(229, 229, 229, 1);
            border-radius: 5px;
        }
        ''')
        self.title.setStyleSheet('''
        *{
            color: rgba(113, 118, 121, 1);
            font-size: 30px;
            font-family: 微软雅黑;
        }
        ''')
        self.subTitle.setStyleSheet('''
        *{
            color: rgba(184, 184, 184, 1);
        }
        ''')


if __name__ == '__main__':
    good_msg = temp = {
        'SIZE': 'A4',
        'COLOR': '黑白打印',
        'WAY': '单面打印',
        'NUM': '2',
        'MESSAGE': '1111111111111111211122111111111121111111',
    }
    app = QApplication(sys.argv)
    ex = PrintOrderInfo(good_msg)
    ex.show()
    sys.exit(app.exec_())
