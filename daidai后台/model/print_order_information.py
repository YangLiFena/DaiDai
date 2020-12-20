#coding=gbk
import sys
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QLineEdit, QToolButton, QGroupBox, QMessageBox)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon

# ֽ�Ŵ�С
# ��ӡ��ɫ
# ��ӡ����
# ��ӡ����
# �û���ע



class PrintOrderInfo(QGroupBox):
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
        self.title.setText('��ӡ����ҳ')

        self.subTitle = QLabel()
        self.subTitle.setText('��ӡ����')

        self.sizeInput = QLineEdit()
        self.sizeInput.setFixedSize(400, 40)
        self.sizeInput.setText('ֽ�Ŵ�С��' + self.good_info['SIZE'])
        self.sizeInput.setEnabled(False)

        self.colorInput = QLineEdit()
        self.colorInput.setFixedSize(400, 40)
        self.colorInput.setText('��ӡ��ɫ��' + self.good_info['COLOR'])
        self.colorInput.setEnabled(False)

        self.wayInput = QLineEdit()
        self.wayInput.setFixedSize(400, 40)
        self.wayInput.setText('��ӡ���ͣ�' + self.good_info['WAY'])
        self.wayInput.setEnabled(False)

        self.numInput = QLineEdit()
        self.numInput.setFixedSize(400, 40)
        self.numInput.setText('��ӡ������' + self.good_info['NUM'])
        self.numInput.setEnabled(False)

        self.messageInput = QLineEdit()
        self.messageInput.setFixedSize(400, 40)
        self.messageInput.setText('��ע��' + self.good_info['MESSAGE'])
        self.messageInput.setEnabled(False)


        # �˳�
        self.back = QToolButton()
        self.back.setText('�˳�')
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
        self.setWindowTitle('��ӡ��������')
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
        'SIZE': 'A4',
        'COLOR': '�ڰ״�ӡ',
        'WAY': '�����ӡ',
        'NUM': '2',
        'MESSAGE': '1111111111111111211122111111111121111111',
    }
    app = QApplication(sys.argv)
    ex = PrintOrderInfo(good_msg)
    ex.show()
    sys.exit(app.exec_())
