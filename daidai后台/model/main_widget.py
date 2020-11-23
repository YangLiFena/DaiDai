#coding=gbk
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from model import login
from model import database
from model import administrator


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setLogin()

        self.setGeometry(200, 200, 1280, 720)
        self.setFixedSize(1280, 720)
        self.setMyStyle()

    # 创建登录菜单
    def setLogin(self):
        self.login = login.Login()
        self.login.setParent(self)
        self.login.move(390, 120)
        self.login.loginButton.clicked.connect(self.loginFunction)

    # # 登录按钮按下
    # def loginFunction(self):
    #     user_mes = {
    #         'ID': self.login.accountInput.text(),
    #         'PASSWORD': database.encrypt(self.login.passwordInput.text())
    #     }
    #     self.user = database.signin(user_mes)
    #     if self.user is not None:
    #         self.login.setVisible(False)
    #         self.display()
    #     else:
    #         print('登录失败!')

    def loginFunction(self):
        self.display()


    def logout(self):
        self.body.close()
        self.login.setVisible(True)

    def display(self):
        self.user = {
            'class': 'admin',
            'AID': 'admin'
        }
        self.body = administrator.AdministratorPage(self.user)
        self.body.setParent(self)
        self.body.setVisible(True)
        self.body.out.clicked.connect(self.logout)

    def setMyStyle(self):
        self.setStyleSheet('''
        QWidget{
            background-color: white;
        }
        ''')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
