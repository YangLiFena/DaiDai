#coding=gbk
import sys
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QLineEdit, QToolButton, QGroupBox, QMessageBox)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon

# �������
# ȡ���ص�
# �ʹ�ص�
# ����ʱ��
# �����ͽ�
# ��������Ҫ��
# �û���ע
# �û�����
# �û�����


class GoodOrderInfo(QGroupBox):
    '''
    �༭�鱾��Ϣ�Ľ���
    ����{
        'SID': str,
        'SNAME': str,
        'DEPARTMENT': str,
        'MAJOR': str,
        'MAX': int
    }
    ����{
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
        self.title.setText('��������ҳ')

        self.subTitle = QLabel()
        self.subTitle.setText('��������')

        # ���������
        self.goodInput = QLineEdit()
        self.goodInput.setFixedSize(400, 40)
        self.goodInput.setText('�����飺' + self.good_info['GOOD'])
        self.goodInput.setEnabled(False)


        self.getAddrInput = QLineEdit()
        self.getAddrInput.setFixedSize(400, 40)
        self.getAddrInput.setText('ȡ���ص㣺' + self.good_info['GETADDR'])
        self.getAddrInput.setEnabled(False)

        self.putAddrInput = QLineEdit()
        self.putAddrInput.setFixedSize(400, 40)
        self.putAddrInput.setText('�ʹ�ص㣺' + self.good_info['PUTADDR'])
        self.putAddrInput.setEnabled(False)

        self.dateInput = QLineEdit()
        self.dateInput.setFixedSize(400, 40)
        self.dateInput.setText('����ʱ�䣺' + self.good_info['DATE'])
        self.dateInput.setEnabled(False)

        self.moneyInput = QLineEdit()
        self.moneyInput.setFixedSize(400, 40)
        self.moneyInput.setText('�����ͽ�' + self.good_info['MONEY'])
        self.moneyInput.setEnabled(False)

        self.creditInput = QLineEdit()
        self.creditInput.setFixedSize(400, 40)
        self.creditInput.setText('���������Ҫ��' + str(self.good_info['CREDIT']))
        self.creditInput.setEnabled(False)

        self.messageInput = QLineEdit()
        self.messageInput.setFixedSize(400, 40)
        self.messageInput.setText('��ע��' + self.good_info['MESSAGE'])
        self.messageInput.setEnabled(False)

        self.evaluateInput = QLineEdit()
        self.evaluateInput.setFixedSize(400, 40)
        self.evaluateInput.setText('�û����ۣ�' + self.good_info['EVALUATE'])
        self.evaluateInput.setEnabled(False)

        self.scoreInput = QLineEdit()
        self.scoreInput.setFixedSize(400, 40)
        self.scoreInput.setText('�û����֣�' + self.good_info['SCORE'])
        self.scoreInput.setEnabled(False)



        # ���������
        # self.nameInput = QLineEdit()
        # self.nameInput.setFixedSize(400, 40)
        # self.nameInput.setText(self.user_info['NAME'])
        # self.nameInput.initText = '����������'
        # self.nameInput.setTextMargins(5, 5, 5, 5)
        # self.nameInput.mousePressEvent = lambda x: self.inputClick(self.nameInput)
        #
        # # �Ա������
        # self.genderInput = QLineEdit()
        # self.genderInput.setFixedSize(400, 40)
        # self.genderInput.setText(self.user_info['GENDER'])
        # self.genderInput.initText = '�������Ա�'
        # self.genderInput.setTextMargins(5, 5, 5, 5)
        # self.genderInput.mousePressEvent = lambda x: self.inputClick(self.genderInput)

        # ����
        # self.passwordInput = QLineEdit()
        # self.passwordInput.setFixedSize(400, 40)
        # self.passwordInput.setText('����������')
        # self.passwordInput.initText = '����������'
        # self.passwordInput.setTextMargins(5, 5, 5, 5)
        # self.passwordInput.mousePressEvent = lambda x: self.inputClick(self.passwordInput)
        #
        # # �ظ�����
        # self.repPasswordInput = QLineEdit()
        # self.repPasswordInput.setFixedSize(400, 40)
        # self.repPasswordInput.setText('���ظ���������')
        # self.repPasswordInput.initText = '���ظ���������'
        # self.repPasswordInput.setTextMargins(5, 5, 5, 5)
        # self.repPasswordInput.mousePressEvent = lambda x: self.inputClick(self.repPasswordInput)

        # # ��������
        # self.maxNumInput = QLineEdit()
        # self.maxNumInput.setFixedSize(400, 40)
        # self.maxNumInput.setText(str(self.stu_info['MAX']))
        # self.maxNumInput.initText = '��������������'
        # self.maxNumInput.setTextMargins(5, 5, 5, 5)
        # self.maxNumInput.mousePressEvent = lambda x: self.inputClick(self.maxNumInput)

        # �ǳ�
        # self.nickInput = QLineEdit()
        # self.nickInput.setFixedSize(400, 40)
        # self.nickInput.setText(self.user_info['NICKNAME'])
        # self.nickInput.initText = '�������ǳ�'
        # self.nickInput.setTextMargins(5, 5, 5, 5)
        # self.nickInput.mousePressEvent = lambda x: self.inputClick(self.nickInput)

        # ��������
        # self.creditInput = QLineEdit()
        # self.creditInput.setFixedSize(400, 40)
        # self.creditInput.setText(str(self.user_info['CREDIT']))
        # self.creditInput.initText = '��������������'
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

        # �ύ
        # self.submit = QToolButton()
        # self.submit.setText('�ύ')
        # self.submit.setFixedSize(400, 40)
        # self.submit.clicked.connect(self.submitFunction)

        # �˳�
        self.back = QToolButton()
        self.back.setText('�˳�')
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
    #         print('��������������')
    #         return
    #     if self.passwordInput.text() != self.passwordInput.initText:
    #         if self.passwordInput.text() != self.repPasswordInput.text():
    #             msgBox = QMessageBox(QMessageBox.Warning, "����!", '�����������벻һ��!', QMessageBox.NoButton, self)
    #             msgBox.addButton("ȷ��", QMessageBox.AcceptRole)
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
    #         print('���������������')
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
        self.setWindowTitle('������������')
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
            font-family: ΢���ź�;
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
            font-family: ΢���ź�;
        }
        ''')
        self.subTitle.setStyleSheet('''
        *{
            color: rgba(184, 184, 184, 1);
        }
        ''')


if __name__ == '__main__':
    good_msg = temp = {
        'GOOD': '��',
        'GETADDR': '������������',
        'PUTADDR': 'õ��԰',
        'DATE': '2020-12-12 12��00',
        'MONEY': '1',
        'CREDIT': 95,
        'MESSAGE': '1111111111111111211122111111111121111111',
        'EVALUATE': '����',
        'SCORE': '5'
    }
    app = QApplication(sys.argv)
    ex = GoodOrderInfo(good_msg)
    ex.show()
    sys.exit(app.exec_())
