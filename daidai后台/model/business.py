#coding=gbk
import sys
import time
import os
import pandas as pd
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QGroupBox,
                             QToolButton, QSplitter, QVBoxLayout, QHBoxLayout,
                             QLabel, QTableWidget, QTableWidgetItem, QAbstractItemView,
                             QLineEdit, QFileDialog, QMessageBox, QComboBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize

from model.database import DataBase
from model.good_order_information import GoodOrderInfo
from model.person_order_information import PersonOrderInfo
from model.print_order_information import PrintOrderInfo
from model.user_information import UserInfo
from model.show_image import ShowImage


class BusinesePage(QWidget):
    def __init__(self, info):
        super().__init__()
        self.info = info
        self.focus = 0
        self.initUI()

    def initUI(self):
        # ������
        self.titleBar = QWidget()
        self.titleBar.setFixedSize(1250, 50)
        self.setTitleBar()

        # �ָ�
        self.body = QSplitter()
        self.setLeftMunu()
        self.content = None
        self.setContent()

        self.bodyLayout = QGridLayout()
        self.bodyLayout.addWidget(self.titleBar, 0, 0, 1, 7)
        self.bodyLayout.addWidget(self.body, 1, 0, 7, 7)
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.bodyLayout)
        self.setFixedSize(1280, 720)
        self.setMyStyle()

    # ���ñ�����
    def setTitleBar(self):
        self.title = QLabel()
        self.title.setText('��ӭʹ�ô�����̨����ϵͳ�����̼Ҷ�')
        self.title.setFixedHeight(30)

        self.account = QToolButton()
        self.account.setIcon(QIcon('icon/person.png'))
        self.account.setText(self.info['AID'])
        self.account.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.account.setFixedHeight(20)
        self.account.setEnabled(False)

        self.out = QToolButton()
        self.out.setText('�˳�')
        self.out.setFixedHeight(30)

        titleLayout = QHBoxLayout()
        titleLayout.addSpacing(100)
        titleLayout.addWidget(self.title)
        titleLayout.addWidget(self.account)
        titleLayout.addWidget(self.out)
        self.titleBar.setLayout(titleLayout)

    # ���˵���
    def setLeftMunu(self):
        # ��������
        self.orderManage = QToolButton()
        self.orderManage.setText('��������')
        self.orderManage.setFixedSize(160, 50)
        self.orderManage.setIcon(QIcon('icon/book.png'))
        self.orderManage.setIconSize(QSize(30, 30))
        self.orderManage.clicked.connect(lambda: self.switch(0, self.orderManage))
        self.orderManage.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)


        self.btnList = [self.orderManage]

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.orderManage)
        self.layout.addStretch()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.menu = QGroupBox()
        self.menu.setFixedSize(160, 500)
        self.menu.setLayout(self.layout)
        self.menu.setContentsMargins(0, 0, 0, 0)
        self.body.addWidget(self.menu)

    def switch(self, index, btn):
        self.focus = index
        for i in self.btnList:
            i.setStyleSheet('''
            *{
                background: white;
            }
            QToolButton:hover{
                background-color: rgba(230, 230, 230, 0.3);
            }
            ''')

        btn.setStyleSheet('''
        QToolButton{
            background-color: rgba(230, 230, 230, 0.7);
        }
        ''')
        self.setContent()

    # �����Ҳ���Ϣҳ
    def setContent(self):
        if self.content is not None:
            self.content.deleteLater()
        if self.focus == 0:
            self.content = OrderManage()
        self.body.addWidget(self.content)

    def setMyStyle(self):
        self.setStyleSheet('''
        QWidget{
            background-color: white;
        }
        ''')
        self.titleBar.setStyleSheet('''
        QWidget{
            background-color: rgba(44,44,44,1);
            border:1px solid black;
            border-radius: 10px;
        }
        ''')
        self.menu.setStyleSheet('''
        QWidget{
            border: 0px;
            border-right: 1px solid rgba(227, 227, 227, 1);
        }
        QToolButton{
            color: rgba(51, 90, 129, 1);
            font-family: ΢���ź�;
            font-size: 25px;
            border-right: 1px solid rgba(227, 227, 227, 1);
        }
        QToolButton:hover{
            background-color: rgba(230, 230, 230, 0.3);
        }
        ''')
        self.title.setStyleSheet('''
        *{
            color: white;
            font-family: ΢���ź�;
            font-size: 25px;
            border: 0px;
        }
        ''')
        self.account.setStyleSheet('''
        *{
            color: white;
            font-weight: ΢���ź�;
            font-size: 25px;
            border: 0px;
        }
        ''')
        self.out.setStyleSheet('''
        QToolButton{
            color: white;
            border:0px;
            font-size: 12px;
        }
        QToolButton:hover{
            color: rgba(11, 145, 255, 1);
        }
        ''')


class OrderManage(QGroupBox):
    def __init__(self):
        super().__init__()
        self.good_list = []
        self.good_info = []
        self.body = QVBoxLayout()
        self.table = None
        self.setTitleBar()
        self.setSearchBar()
        self.searchFunction()

        self.setLayout(self.body)
        self.initUI()

    # ������
    def setTitleBar(self):
        self.title = QLabel()
        self.title.setText('��������')
        self.title.setFixedHeight(25)
        titleLayout = QHBoxLayout()
        titleLayout.addSpacing(50)
        titleLayout.addWidget(self.title)
        self.titleBar = QWidget()
        self.titleBar.setFixedSize(1000, 50)
        self.titleBar.setLayout(titleLayout)
        self.body.addWidget(self.titleBar)

    # ����������
    def setSearchBar(self):
        self.searchTitle = QLabel()
        self.searchTitle.setText('����ѧ��')
        self.searchInput = QLineEdit()
        self.searchInput.setText('')
        self.searchInput.setClearButtonEnabled(True)
        self.searchInput.setFixedSize(400, 40)
        self.searchButton = QToolButton()
        self.searchButton.setFixedSize(100, 40)
        self.searchButton.setText('����')
        self.searchButton.clicked.connect(self.searchFunction)
        self.toCsvButton = QToolButton()
        self.toCsvButton.setFixedSize(100, 40)
        self.toCsvButton.setText('����')
        self.toCsvButton.clicked.connect(self.toCsvFunction)
        searchLayout = QHBoxLayout()
        searchLayout.addStretch()
        searchLayout.addWidget(self.searchTitle)
        searchLayout.addWidget(self.searchInput)
        searchLayout.addWidget(self.searchButton)
        searchLayout.addWidget(self.toCsvButton)
        searchLayout.addStretch()
        self.searchWidget = QWidget()
        self.searchWidget.setLayout(searchLayout)
        self.body.addWidget(self.searchWidget)


    def searchFunction(self):
        # print('111��������������')
        self.good_list, self.good_info = DataBase.search_order_business(self.searchInput.text())
        if self.good_list == []:
            print('δ�ҵ�')
        if self.table is not None:
            self.table.deleteLater()
        self.searchInput.setText('')
        self.setTable()

    def toCsvFunction(self):
        data = []
        for i in range(len(self.good_list)):
            temp = []
            for j in range((len(self.good_list[i]) - 1)):
                temp.append(self.good_list[i][j])
            for j in range(len(self.good_info[i])):
                temp.append(self.good_info[i][j])
            temp.append(self.good_list[i][0][:5] + '_' + self.good_list[i][1])
            data.append(temp)
        print(data)
        new_data = pd.DataFrame(data=data, columns=['������', '������ѧ��', '����״̬', 'ֽ������', '��ӡ��ɫ', '��ӡ��ʽ', '��ӡ����', '��ע', '�ļ�λ��'])
        new_data.to_csv('�̼Ҷ���.csv', index=False, encoding='GBK')

    # ���ñ��
    def setTable(self):
        self.table = QTableWidget(1, 4)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setColumnWidth(0, 220)
        self.table.setColumnWidth(1, 220)
        self.table.setColumnWidth(2, 220)
        self.table.setColumnWidth(3, 300)

        self.table.setItem(0, 0, QTableWidgetItem('������'))
        self.table.setItem(0, 1, QTableWidgetItem('������ѧ��'))
        self.table.setItem(0, 2, QTableWidgetItem('����״̬'))
        self.table.setItem(0, 3, QTableWidgetItem('����'))

        for i in range(4):
            self.table.item(0, i).setTextAlignment(Qt.AlignCenter)
            self.table.item(0, i).setFont(QFont('΢���ź�', 15))

        # ��ʾ��������
        for i in self.good_list:
            self.insertRow(i)
        self.body.addWidget(self.table)

    # ������
    def insertRow(self, val: list):
        itemORDERID = QTableWidgetItem(val[0])
        itemORDERID.setTextAlignment(Qt.AlignCenter)

        itemPUTSNO = QTableWidgetItem(val[1])
        itemPUTSNO.setTextAlignment(Qt.AlignCenter)

        itemSTATUS = QTableWidgetItem(val[2])
        itemSTATUS.setTextAlignment(Qt.AlignCenter)

        itemModify = QToolButton(self.table)
        itemModify.setFixedSize(80, 30)
        itemModify.setText('����')
        itemModify.clicked.connect(lambda: self.detailOrderFunction(val[0]))
        itemModify.setStyleSheet('''
        *{
            color: white;
            font-family: ΢���ź�;
            background: rgba(38, 175, 217, 1);
            border: 0;
            border-radius: 10px;
        }
        ''')
        itemUpload = QToolButton(self.table)
        itemUpload.setFixedSize(80, 30)
        itemUpload.setText('�����ļ�')
        itemUpload.clicked.connect(lambda: self.downLoadFunction(val))
        itemUpload.setStyleSheet('''
        *{
            color: white;
                font-family: ΢���ź�;
                background: rgba(51, 153, 0, 1);
                border: 0;
                border-radius: 10px;
        }
        ''')

        itemFinish = QToolButton(self.table)
        itemFinish.setFixedSize(80, 30)
        itemFinish.setText('��ɶ���')
        itemFinish.clicked.connect(lambda: self.finishFunction(val[0]))
        itemFinish.setStyleSheet('''
                *{
                    color: white;
                        font-family: ΢���ź�;
                        background: rgba(222, 52, 65, 1);
                        border: 0;
                        border-radius: 10px;
                }
                ''')

        itemLayout = QHBoxLayout()
        itemLayout.setContentsMargins(0, 0, 0, 0)
        itemLayout.addWidget(itemModify)
        itemLayout.addWidget(itemUpload)
        itemLayout.addWidget(itemFinish)
        itemWidget = QWidget()
        itemWidget.setLayout(itemLayout)

        self.table.insertRow(1)
        self.table.setItem(1, 0, itemORDERID)
        self.table.setItem(1, 1, itemPUTSNO)
        self.table.setItem(1, 2, itemSTATUS)
        self.table.setCellWidget(1, 3, itemWidget)

    # def updateBookFunction(self, BID: str):
    #     book_info = database.get_book_info(BID)
    #     if book_info is None:
    #         return
    #     self.sum = book_info['SUM']
    #     self.updateBookDialog = book_information.BookInfo(book_info)
    #     self.updateBookDialog.after_close.connect(self.updateBook)
    #     self.updateBookDialog.show()

    # def updateBook(self, book_info: dict):
    #     change = self.sum - book_info['SUM']
    #     # �鱾���ٵ��������ܴ���δ������鱾��
    #     if change > book_info['NUM']:
    #         book_info['SUM'] = self.sum - book_info['NUM']
    #         book_info['NUM'] = 0
    #     else:
    #         book_info['NUM'] -= change
    #     ans = database.update_book(book_info)
    #     if ans:
    #         self.searchFunction()

    def detailOrderFunction(self, orderId):
        index = 0
        for item in self.good_list:
            if item[0] == orderId:
                break
            else:
                index = index + 1
        # print('$$$$$$$$$$$$$')
        # print(self.good_info)
        temp = {}
        # print('------------')
        # print(order_type)
        temp['SIZE'] = self.good_info[index][0]
        temp['COLOR'] = self.good_info[index][1]
        temp['WAY'] = self.good_info[index][2]
        temp['NUM'] = self.good_info[index][3]
        temp['MESSAGE'] = self.good_info[index][4]
        self.detailOrder = PrintOrderInfo(temp)
        self.detailOrder.show()
        # print("����޸ģ������")

    # def deleteBookFunction(self, BID: str):
    #     msgBox = QMessageBox(QMessageBox.Warning, "����!", '����������ɾ���Ȿ���Լ������Ϣ!',
    #                          QMessageBox.NoButton, self)
    #     msgBox.addButton("ȷ��", QMessageBox.AcceptRole)
    #     msgBox.addButton("ȡ��", QMessageBox.RejectRole)
    #     if msgBox.exec_() == QMessageBox.AcceptRole:
    #         ans = database.delete_book(BID)
    #         if ans:
    #             self.searchFunction()

    def downLoadFunction(self, val):
        print('click')
        index = 0
        print(self.good_list)
        for item in self.good_list:
            if item[0] == val[0]:
                break
            else:
                index = index + 1
        list = self.good_list[index][3]
        src_list = DataBase.get_file(list)
        print(src_list)
        msgBox = QMessageBox(QMessageBox.Warning, "��ȷ��!", '������' + str(len(src_list)) + '���ļ�!',
                             QMessageBox.NoButton, self)
        msgBox.addButton("ȷ��", QMessageBox.AcceptRole)
        msgBox.addButton("ȡ��", QMessageBox.RejectRole)
        if msgBox.exec_() == QMessageBox.AcceptRole:
            path = val[0][:5] + '_' + val[1]
            isExists = os.path.exists(path)
            if not isExists:
                os.makedirs(path)
            for i in range(0, len(src_list), 1):
                f = requests.get(src_list[i])
                # �����ļ�
                with open('./' + path + '/' + str(i) + '.doc', "wb") as code:
                    code.write(f.content)
                    code.close()
            reply = QMessageBox.about(self, "�������", "�������")

    def finishFunction(self, orderId):
        msgBox = QMessageBox(QMessageBox.Warning, "��ȷ��!", '��ȷ���Ƿ���ɶ���!',
                             QMessageBox.NoButton, self)
        msgBox.addButton("ȷ��", QMessageBox.AcceptRole)
        msgBox.addButton("ȡ��", QMessageBox.RejectRole)
        if msgBox.exec_() == QMessageBox.AcceptRole:
            ans = DataBase.print_finish(orderId)
            if ans:
                reply = QMessageBox.about(self, "���ĳɹ�", "���ĳɹ�")
                self.searchFunction()

    def initUI(self):
        self.setFixedSize(1100, 600)
        self.setStyleSheet('''
        *{
            background-color: white;
            border:0px;
        }
        ''')
        self.titleBar.setStyleSheet('''
        QWidget {
            border:0;
            background-color: rgba(216, 216, 216, 1);
            border-radius: 20px;
            color: rgba(113, 118, 121, 1);
        }
        QLabel{
            font-size: 25px;
            font-family: ΢���ź�;
        }
        ''')
        self.searchTitle.setStyleSheet('''
            QLabel{
                font-size:25px;
                color: black;
                font-family: ΢���ź�;
            }
        ''')
        self.searchInput.setStyleSheet('''
            QLineEdit{
                border: 1px solid rgba(201, 201, 201, 1);
                border-radius: 5px;
                color: rgba(120, 120, 120, 1)
            }
        ''')
        self.searchButton.setStyleSheet('''
            QToolButton{
                border-radius: 10px;
                background-color:rgba(52, 118, 176, 1);
                color: white;
                font-size: 25px;
                font-family: ΢���ź�;
            }
        ''')
        self.toCsvButton.setStyleSheet('''
                    QToolButton{
                        border-radius: 10px;
                        background-color:rgba(52, 118, 176, 1);
                        color: white;
                        font-size: 25px;
                        font-family: ΢���ź�;
                    }
                ''')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_message = {
        'class': 'admin',
        'AID': 'admin'
    }
    ex = BusinesePage(user_message)
    ex.show()
    sys.exit(app.exec_())
