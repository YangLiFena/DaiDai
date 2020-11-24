#coding=gbk
import sys
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QLineEdit, QToolButton, QGroupBox, QMessageBox)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon

# 出发地
# 目的地
# 期望时间
# 期望赏金
# 信誉积分要求
# 用户备注
# 用户评价
# 用户评分


class PersonOrderInfo(QGroupBox):
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
        self.title.setText('带人详情页')

        self.subTitle = QLabel()
        self.subTitle.setText('带人详情')

        self.getAddrInput = QLineEdit()
        self.getAddrInput.setFixedSize(400, 40)
        self.getAddrInput.setText('出发地点：' + self.good_info['GETADDR'])
        self.getAddrInput.setEnabled(False)

        self.putAddrInput = QLineEdit()
        self.putAddrInput.setFixedSize(400, 40)
        self.putAddrInput.setText('目的地点：' + self.good_info['PUTADDR'])
        self.putAddrInput.setEnabled(False)

        self.dateInput = QLineEdit()
        self.dateInput.setFixedSize(400, 40)
        self.dateInput.setText('出发时间：' + self.good_info['DATE'])
        self.dateInput.setEnabled(False)

        self.moneyInput = QLineEdit()
        self.moneyInput.setFixedSize(400, 40)
        self.moneyInput.setText('期望赏金：' + self.good_info['MONEY'])
        self.moneyInput.setEnabled(False)

        self.creditInput = QLineEdit()
        self.creditInput.setFixedSize(400, 40)
        self.creditInput.setText('信誉分最低要求：' + str(self.good_info['CREDIT']))
        self.creditInput.setEnabled(False)

        self.messageInput = QLineEdit()
        self.messageInput.setFixedSize(400, 40)
        self.messageInput.setText('备注：' + self.good_info['MESSAGE'])
        self.messageInput.setEnabled(False)

        self.evaluateInput = QLineEdit()
        self.evaluateInput.setFixedSize(400, 40)
        self.evaluateInput.setText('用户评价：' + self.good_info['EVALUATE'])
        self.evaluateInput.setEnabled(False)

        self.scoreInput = QLineEdit()
        self.scoreInput.setFixedSize(400, 40)
        self.scoreInput.setText('用户评分：' + self.good_info['SCORE'])
        self.scoreInput.setEnabled(False)


        # 退出
        self.back = QToolButton()
        self.back.setText('退出')
        self.back.setFixedSize(400, 40)
        self.back.clicked.connect(self.close)

        self.btnList = [
            self.getAddrInput,
            self.putAddrInput,
            self.dateInput,
            self.moneyInput,
            self.creditInput,
            self.messageInput,
            self.evaluateInput,
            self.scoreInput
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
        self.setFixedSize(422, 510)
        self.setWindowTitle('带货订单详情')
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
        'GETADDR': '福大生活三区',
        'PUTADDR': '玫瑰园',
        'DATE': '2020-12-12 12：00',
        'MONEY': '1',
        'CREDIT': 95,
        'MESSAGE': '1111111111111111211122111111111121111111',
        'EVALUATE': '还行',
        'SCORE': '5'
    }
    app = QApplication(sys.argv)
    ex = PersonOrderInfo(good_msg)
    ex.show()
    sys.exit(app.exec_())
