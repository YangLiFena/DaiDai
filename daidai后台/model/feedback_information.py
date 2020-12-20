#coding=gbk
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon


class FeedbackInfo(QGroupBox):
    # after_close = pyqtSignal(dict)

    def __init__(self, feedback_info: dict):
        super().__init__()
        self.feedback_info = feedback_info

        self.title = QLabel()
        self.title.setText('�û�����ҳ')

        self.subTitle = QLabel()
        self.subTitle.setText('��������')

        self.getFeedbackInput = QLabel()
        self.getFeedbackInput.setFixedSize(400, 250)
        self.getFeedbackInput.setText(self.feedback_info['FEEDBACK'] + '\n\n\n\n')
        self.getFeedbackInput.setWordWrap(True)
        # self.getFeedbackInput.setEnabled(False)

        # �˳�
        self.back = QToolButton()
        self.back.setText('�˳�')
        self.back.setFixedSize(400, 40)
        self.back.clicked.connect(self.close)

        self.btnList = [
            self.getFeedbackInput
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
        self.setFixedSize(422, 370)
        self.setWindowTitle('�û���������')
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
        'FEEDBACK': '��Ҷ�ʲô�Ǽ��������Ψһ��׼�����۷׷ף����㼺���������в��������κ�����'
                    '�����������Ҫһ������ı�׼�����׼����ʵ�������������Ψһ�ı�׼������ë'
                    '��ϯ����˵����ֻ���پ����˹������Ⱥ�ڵ�ʵ�������ܵó�������'
                    '���������׼��������ʵ����ͳһ�������˼ʵ����ʶ����ѧ�Ļ���ԭ����'
                    '��˼����֮����ӵ��ǿ�������������Ϊ�������������������ε�ʵ�����飬���Ƕ�'
                    '��Щʵ�����̡�ʵ�������Ũ���ܽᣬ�پ������ϵط�չ�봴��'
    }
    app = QApplication(sys.argv)
    ex = FeedbackInfo(good_msg)
    ex.show()
    sys.exit(app.exec_())
