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
        self.title.setText('用户反馈页')

        self.subTitle = QLabel()
        self.subTitle.setText('反馈详情')

        self.getFeedbackInput = QLabel()
        self.getFeedbackInput.setFixedSize(400, 250)
        self.getFeedbackInput.setText(self.feedback_info['FEEDBACK'] + '\n\n\n\n')
        self.getFeedbackInput.setWordWrap(True)
        # self.getFeedbackInput.setEnabled(False)

        # 退出
        self.back = QToolButton()
        self.back.setText('退出')
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
        self.setWindowTitle('用户反馈详情')
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
        'FEEDBACK': '大家对什么是检验真理的唯一标准，议论纷纷，各抒己见。文章中阐述道：任何真理'
                    '的提出，都需要一个检验的标准，其标准就是实践活动，而且这是唯一的标准。正如毛'
                    '主席曾经说过，只有再经过了广大人民群众的实践，才能得出衡量真'
                    '理的真正标准。真理与实践的统一，是马克思实践认识观哲学的基本原则，马'
                    '克思主义之所以拥有强大的力量，是因为它经受了世界上无数次的实践检验，它是对'
                    '这些实践过程、实践经验的浓缩总结，再经过不断地发展与创新'
    }
    app = QApplication(sys.argv)
    ex = FeedbackInfo(good_msg)
    ex.show()
    sys.exit(app.exec_())
