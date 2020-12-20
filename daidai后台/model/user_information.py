import sys
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QLineEdit, QToolButton, QGroupBox, QMessageBox)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon


class UserInfo(QGroupBox):
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
    after_close = pyqtSignal(dict)

    def __init__(self, user_info: dict):
        super().__init__()
        self.user_info = user_info

        self.title = QLabel()
        self.title.setText('用户信息')

        self.subTitle = QLabel()
        self.subTitle.setText('修改用户信息')

        # ID输入框
        self.idInput = QLineEdit()
        self.idInput.setFixedSize(400, 40)
        self.idInput.setText('学号/商家号：' + self.user_info['ID'])
        # self.idInput.initText = '请输入学号/商家号'
        self.idInput.setEnabled(False)

        # 姓名输入框
        self.nameInput = QLineEdit()
        self.nameInput.setFixedSize(400, 40)
        self.nameInput.setText('姓名：' + self.user_info['NAME'])
        self.nameInput.setEnabled(False)
        # self.nameInput.initText = '请输入姓名'
        # self.nameInput.setTextMargins(5, 5, 5, 5)
        # self.nameInput.mousePressEvent = lambda x: self.inputClick(self.nameInput)

        # 性别输入框
        self.genderInput = QLineEdit()
        self.genderInput.setFixedSize(400, 40)
        self.genderInput.setText('性别：' + self.user_info['GENDER'])
        self.genderInput.setEnabled(False)
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
        self.nickInput = QLineEdit()
        self.nickInput.setFixedSize(400, 40)
        self.nickInput.setText('昵称：' + self.user_info['NICKNAME'])
        self.nickInput.setEnabled(False)
        # self.nickInput.initText = '请输入昵称'
        # self.nickInput.setTextMargins(5, 5, 5, 5)
        # self.nickInput.mousePressEvent = lambda x: self.inputClick(self.nickInput)

        # 信誉积分
        self.creditInput = QLineEdit()
        self.creditInput.setFixedSize(400, 40)
        self.creditInput.setText(str(self.user_info['CREDIT']))
        self.creditInput.initText = '请输入信誉积分'
        self.creditInput.setTextMargins(5, 5, 5, 5)
        self.creditInput.mousePressEvent = lambda x: self.inputClick(self.creditInput)


        # 提交
        self.submit = QToolButton()
        self.submit.setText('提交')
        self.submit.setFixedSize(400, 40)
        self.submit.clicked.connect(self.submitFunction)

        # 退出
        self.back = QToolButton()
        self.back.setText('退出')
        self.back.setFixedSize(400, 40)
        self.back.clicked.connect(self.close)

        self.btnList = [
            self.idInput,
            self.nameInput,
            self.genderInput,
            self.nickInput,
            self.creditInput,
        ]

        self.bodyLayout = QVBoxLayout()
        self.bodyLayout.addWidget(self.title)
        self.bodyLayout.addWidget(self.subTitle)
        for i in self.btnList:
            self.bodyLayout.addWidget(i)
        self.bodyLayout.addWidget(self.submit)
        self.bodyLayout.addWidget(self.back)

        self.setLayout(self.bodyLayout)
        self.initUI()

    def inputClick(self, e):
        for i in range(2, 7):
            item = self.bodyLayout.itemAt(i).widget()
            if item.text() == '':
                item.setText(item.initText)
                # if item is self.passwordInput or item is self.repPasswordInput:
                #     item.setEchoMode(QLineEdit.Normal)

        if e.text() == e.initText:
            e.setText('')
        # if e is self.passwordInput or e is self.repPasswordInput:
        #     e.setEchoMode(QLineEdit.Password)

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

    def submitFunction(self):
        self.user_info['CREDIT'] = int(self.creditInput.text())
        self.close()
        self.after_close.emit(self.user_info)

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
        self.setFixedSize(422, 400)
        self.setWindowTitle('修改用户信息')
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
    user_msg = temp = {
        'ID': '031802318',
        'NAME': 'lrs',
        'GENDER': '男',
        'NICKNAME': 'lrs',
        'CREDIT': 100
    }
    app = QApplication(sys.argv)
    ex = UserInfo(user_msg)
    ex.show()
    sys.exit(app.exec_())
