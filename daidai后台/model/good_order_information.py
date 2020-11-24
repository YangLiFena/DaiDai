#coding=gbk
import sys
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QLineEdit, QToolButton, QGroupBox, QMessageBox)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon

# 货物介绍
# 取货地点
# 送达地点
# 期望时间
# 期望赏金
# 信誉积分要求
# 用户备注
# 用户评价
# 用户评分


class GoodOrderInfo(QGroupBox):
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
        self.title.setText('带货详情页')

        self.subTitle = QLabel()
        self.subTitle.setText('带货详情')

        # 货物输入框
        self.goodInput = QLineEdit()
        self.goodInput.setFixedSize(400, 40)
        self.goodInput.setText('货物简介：' + self.good_info['GOOD'])
        self.goodInput.setEnabled(False)


        self.getAddrInput = QLineEdit()
        self.getAddrInput.setFixedSize(400, 40)
        self.getAddrInput.setText('取货地点：' + self.good_info['GETADDR'])
        self.getAddrInput.setEnabled(False)

        self.putAddrInput = QLineEdit()
        self.putAddrInput.setFixedSize(400, 40)
        self.putAddrInput.setText('送达地点：' + self.good_info['PUTADDR'])
        self.putAddrInput.setEnabled(False)

        self.dateInput = QLineEdit()
        self.dateInput.setFixedSize(400, 40)
        self.dateInput.setText('期望时间：' + self.good_info['DATE'])
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



        # 姓名输入框
        # self.nameInput = QLineEdit()
        # self.nameInput.setFixedSize(400, 40)
        # self.nameInput.setText(self.user_info['NAME'])
        # self.nameInput.initText = '请输入姓名'
        # self.nameInput.setTextMargins(5, 5, 5, 5)
        # self.nameInput.mousePressEvent = lambda x: self.inputClick(self.nameInput)
        #
        # # 性别输入框
        # self.genderInput = QLineEdit()
        # self.genderInput.setFixedSize(400, 40)
        # self.genderInput.setText(self.user_info['GENDER'])
        # self.genderInput.initText = '请输入性别'
        # self.genderInput.setTextMargins(5, 5, 5, 5)
        # self.genderInput.mousePressEvent = lambda x: self.inputClick(self.genderInput)

        # 密码
        # self.passwordInput = QLineEdit()
        # self.passwordInput.setFixedSize(400, 40)
        # self.passwordInput.setText('请输入密码')
        # self.passwordInput.initText = '请输入密码'
        # self.passwordInput.setTextMargins(5, 5, 5, 5)
        # self.passwordInput.mousePressEvent = lambda x: self.inputClick(self.passwordInput)
        #
        # # 重复密码
        # self.repPasswordInput = QLineEdit()
        # self.repPasswordInput.setFixedSize(400, 40)
        # self.repPasswordInput.setText('请重复输入密码')
        # self.repPasswordInput.initText = '请重复输入密码'
        # self.repPasswordInput.setTextMargins(5, 5, 5, 5)
        # self.repPasswordInput.mousePressEvent = lambda x: self.inputClick(self.repPasswordInput)

        # # 最大借书数
        # self.maxNumInput = QLineEdit()
        # self.maxNumInput.setFixedSize(400, 40)
        # self.maxNumInput.setText(str(self.stu_info['MAX']))
        # self.maxNumInput.initText = '请输入最大借书数'
        # self.maxNumInput.setTextMargins(5, 5, 5, 5)
        # self.maxNumInput.mousePressEvent = lambda x: self.inputClick(self.maxNumInput)

        # 昵称
        # self.nickInput = QLineEdit()
        # self.nickInput.setFixedSize(400, 40)
        # self.nickInput.setText(self.user_info['NICKNAME'])
        # self.nickInput.initText = '请输入昵称'
        # self.nickInput.setTextMargins(5, 5, 5, 5)
        # self.nickInput.mousePressEvent = lambda x: self.inputClick(self.nickInput)

        # 信誉积分
        # self.creditInput = QLineEdit()
        # self.creditInput.setFixedSize(400, 40)
        # self.creditInput.setText(str(self.user_info['CREDIT']))
        # self.creditInput.initText = '请输入信誉积分'
        # self.creditInput.setTextMargins(5, 5, 5, 5)
        # self.creditInput.mousePressEvent = lambda x: self.inputClick(self.creditInput)
        #
        # self.temp1Input = QLineEdit()
        # self.temp1Input.setFixedSize(400, 40)
        # # self.temp1Input.setText(str(self.stu_info['MAX']))
        # self.temp1Input.initText = ''
        # self.temp1Input.setTextMargins(5, 5, 5, 5)
        # # self.temo1Input.mousePressEvent = lambda x: self.inputClick(self.maxNumInput)
        #
        # self.temp2Input = QLineEdit()
        # self.temp2Input.setFixedSize(400, 40)
        # # self.maxNumInput.setText(str(self.stu_info['MAX']))
        # self.temp2Input.initText = ''
        # self.temp2Input.setTextMargins(5, 5, 5, 5)
        # self.maxNumInput.mousePressEvent = lambda x: self.inputClick(self.maxNumInput)

        # 提交
        # self.submit = QToolButton()
        # self.submit.setText('提交')
        # self.submit.setFixedSize(400, 40)
        # self.submit.clicked.connect(self.submitFunction)

        # 退出
        self.back = QToolButton()
        self.back.setText('退出')
        self.back.setFixedSize(400, 40)
        self.back.clicked.connect(self.close)

        self.btnList = [
            self.goodInput,
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

    # def inputClick(self, e):
    #     for i in range(2, 9):
    #         item = self.bodyLayout.itemAt(i).widget()
    #         if item.text() == '':
    #             item.setText(item.initText)
    #             # if item is self.passwordInput or item is self.repPasswordInput:
    #             #     item.setEchoMode(QLineEdit.Normal)
    #
    #     if e.text() == e.initText:
    #         e.setText('')
    #     # if e is self.passwordInput or e is self.repPasswordInput:
    #     #     e.setEchoMode(QLineEdit.Password)

    # def submitFunction(self):
    #     if not self.maxNumInput.text().isalnum():
    #         print('最大数量输入错误')
    #         return
    #     if self.passwordInput.text() != self.passwordInput.initText:
    #         if self.passwordInput.text() != self.repPasswordInput.text():
    #             msgBox = QMessageBox(QMessageBox.Warning, "错误!", '两次输入密码不一致!', QMessageBox.NoButton, self)
    #             msgBox.addButton("确认", QMessageBox.AcceptRole)
    #             msgBox.exec_()
    #             return
    #         self.stu_info['PASSWORD'] = database.encrypt(self.passwordInput.text())
    #     self.stu_info['SNAME'] = self.nameInput.text()
    #     self.stu_info['DEPARTMENT'] = self.deptInput.text()
    #     self.stu_info['MAJOR'] = self.majorInput.text()
    #     self.stu_info['MAX'] = int(self.maxNumInput.text())
    #     self.close()
    #     self.after_close.emit(self.stu_info)

    # def submitFunction(self):
    #     if not self.creditInput.text().isalnum():
    #         print('信誉积分输入错误')
    #         return
    #     self.user_info['ID'] = self.idInput.text()
    #     self.user_info['NAME'] = self.nameInput.text()
    #     self.user_info['GENDER'] = self.genderInput.text()
    #     self.user_info['NICK'] = self.nickInput.text()
    #     self.user_info['CREDIT'] = int(self.creditInput.text())
    #     self.close()
    #     self.after_close.emit(self.user_info)

    def initUI(self):
        self.setFixedSize(422, 560)
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
        'GOOD': '饭',
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
    ex = GoodOrderInfo(good_msg)
    ex.show()
    sys.exit(app.exec_())
