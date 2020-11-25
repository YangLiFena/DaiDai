#coding=gbk
import sys
import time
import os
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


class AdministratorPage(QWidget):
    def __init__(self, info):
        super().__init__()
        self.info = info
        self.focus = 0
        self.initUI()

    def initUI(self):
        # 标题栏
        self.titleBar = QWidget()
        self.titleBar.setFixedSize(1250, 50)
        self.setTitleBar()

        # 分割
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

    # 设置标题栏
    def setTitleBar(self):
        self.title = QLabel()
        self.title.setText('欢迎使用带代后台管理系统')
        self.title.setFixedHeight(30)

        self.account = QToolButton()
        self.account.setIcon(QIcon('icon/person.png'))
        self.account.setText(self.info['AID'])
        self.account.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.account.setFixedHeight(20)
        self.account.setEnabled(False)

        self.out = QToolButton()
        self.out.setText('退出')
        self.out.setFixedHeight(30)

        titleLayout = QHBoxLayout()
        titleLayout.addSpacing(100)
        titleLayout.addWidget(self.title)
        titleLayout.addWidget(self.account)
        titleLayout.addWidget(self.out)
        self.titleBar.setLayout(titleLayout)

    # 左侧菜单栏
    def setLeftMunu(self):
        # 订单管理
        self.orderManage = QToolButton()
        self.orderManage.setText('订单管理')
        self.orderManage.setFixedSize(160, 50)
        self.orderManage.setIcon(QIcon('icon/book.png'))
        self.orderManage.setIconSize(QSize(30, 30))
        self.orderManage.clicked.connect(lambda: self.switch(0, self.orderManage))
        self.orderManage.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 用户管理
        self.userManage = QToolButton()
        self.userManage.setText('用户管理')
        self.userManage.setFixedSize(160, 50)
        self.userManage.setIcon(QIcon('icon/borrowing.png'))
        self.userManage.setIconSize(QSize(30, 30))
        self.userManage.clicked.connect(lambda: self.switch(1, self.userManage))
        self.userManage.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 认证审核
        self.auditManage = QToolButton()
        self.auditManage.setText('认证审核')
        self.auditManage.setFixedSize(160, 50)
        self.auditManage.setIcon(QIcon('icon/borrowing.png'))
        self.auditManage.setIconSize(QSize(30, 30))
        self.auditManage.clicked.connect(lambda: self.switch(2, self.auditManage))
        self.auditManage.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.btnList = [self.orderManage, self.userManage,
                        self.auditManage]

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.orderManage)
        self.layout.addWidget(self.userManage)
        self.layout.addWidget(self.auditManage)
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

    # 设置右侧信息页
    def setContent(self):
        if self.content is not None:
            self.content.deleteLater()
        if self.focus == 0:
            self.content = OrderManage()
        elif self.focus == 1:
            self.content = UserManage()
        else:
            self.content = AuditManage()
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
            font-family: 微软雅黑;
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
            font-family: 微软雅黑;
            font-size: 25px;
            border: 0px;
        }
        ''')
        self.account.setStyleSheet('''
        *{
            color: white;
            font-weight: 微软雅黑;
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

    # 标题栏
    def setTitleBar(self):
        self.title = QLabel()
        self.title.setText('订单管理')
        self.title.setFixedHeight(25)
        titleLayout = QHBoxLayout()
        titleLayout.addSpacing(50)
        titleLayout.addWidget(self.title)
        self.titleBar = QWidget()
        self.titleBar.setFixedSize(1000, 50)
        self.titleBar.setLayout(titleLayout)
        self.body.addWidget(self.titleBar)

    # 设置搜索框
    def setSearchBar(self):
        self.searchTitle = QLabel()
        self.searchTitle.setText('搜索学号/商家号')
        self.searchInput = QLineEdit()
        self.searchInput.setText('')
        self.searchInput.setClearButtonEnabled(True)
        self.searchInput.setFixedSize(400, 40)
        self.searchButton = QToolButton()
        self.searchButton.setFixedSize(100, 40)
        self.searchButton.setText('搜索')
        self.searchButton.clicked.connect(self.searchFunction)
        searchLayout = QHBoxLayout()
        searchLayout.addStretch()
        searchLayout.addWidget(self.searchTitle)
        searchLayout.addWidget(self.searchInput)
        searchLayout.addWidget(self.searchButton)
        searchLayout.addStretch()
        self.searchWidget = QWidget()
        self.searchWidget.setLayout(searchLayout)
        self.body.addWidget(self.searchWidget)

    # 搜索方法
    # def searchFunction(self):
    #     convert = {'书号': 'BID', '分类': 'CLASSIFICATION', '出版社': 'PRESS', '作者': 'AUTHOR', '书名': 'BNAME', '': 'BNAME'}
    #     self.book_list = database.search_book(self.searchInput.text(), convert[self.selectBox.currentText()])
    #     if self.book_list == []:
    #         print('未找到')
    #     if self.table is not None:
    #         self.table.deleteLater()
    #     self.setTable()

    def searchFunction(self):
        # print('111点击搜索，待添加')
        self.good_list, self.good_info = DataBase.search_order(self.searchInput.text())
        if self.good_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        self.searchInput.setText('')
        self.setTable()

    # 设置表格
    def setTable(self):
        self.table = QTableWidget(1, 6)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setColumnWidth(0, 160)
        self.table.setColumnWidth(1, 160)
        self.table.setColumnWidth(2, 220)
        self.table.setColumnWidth(3, 160)
        self.table.setColumnWidth(4, 140)
        self.table.setColumnWidth(5, 160)

        self.table.setItem(0, 0, QTableWidgetItem('订单号'))
        self.table.setItem(0, 1, QTableWidgetItem('发单人学号'))
        self.table.setItem(0, 2, QTableWidgetItem('接单人学号/商家号'))
        self.table.setItem(0, 3, QTableWidgetItem('订单类型'))
        self.table.setItem(0, 4, QTableWidgetItem('订单状态'))
        self.table.setItem(0, 5, QTableWidgetItem('操作'))

        for i in range(6):
            self.table.item(0, i).setTextAlignment(Qt.AlignCenter)
            self.table.item(0, i).setFont(QFont('微软雅黑', 15))

        # 显示订单详情
        for i in self.good_list:
            self.insertRow(i)
        self.body.addWidget(self.table)

    # 插入行
    def insertRow(self, val: list):
        itemORDERID = QTableWidgetItem(val[0])
        itemORDERID.setTextAlignment(Qt.AlignCenter)

        itemPUTSNO = QTableWidgetItem(val[1])
        itemPUTSNO.setTextAlignment(Qt.AlignCenter)

        itemGETSNO = QTableWidgetItem(val[2])
        itemGETSNO.setTextAlignment(Qt.AlignCenter)

        itemTYPE = QTableWidgetItem(val[3])
        itemTYPE.setTextAlignment(Qt.AlignCenter)

        itemSTATUS = QTableWidgetItem(val[4])
        itemSTATUS.setTextAlignment(Qt.AlignCenter)


        itemModify = QToolButton(self.table)
        itemModify.setFixedSize(50, 25)
        itemModify.setText('详情')
        itemModify.clicked.connect(lambda: self.detailOrderFunction(val[0]))
        itemModify.setStyleSheet('''
        *{
            color: white;
            font-family: 微软雅黑;
            background: rgba(38, 175, 217, 1);
            border: 0;
            border-radius: 10px;
        }
        ''')
        itemDelete = QToolButton(self.table)
        itemDelete.setFixedSize(50, 25)
        itemDelete.setText('删除')
        itemDelete.clicked.connect(lambda: self.deleteOrderFunction(val[0]))
        itemDelete.setStyleSheet('''
        *{
            color: white;
                font-family: 微软雅黑;
                background: rgba(222, 52, 65, 1);
                border: 0;
                border-radius: 10px;
        }
        ''')

        itemLayout = QHBoxLayout()
        itemLayout.setContentsMargins(0, 0, 0, 0)
        itemLayout.addWidget(itemModify)
        itemLayout.addWidget(itemDelete)
        itemWidget = QWidget()
        itemWidget.setLayout(itemLayout)

        self.table.insertRow(1)
        self.table.setItem(1, 0, itemORDERID)
        self.table.setItem(1, 1, itemPUTSNO)
        self.table.setItem(1, 2, itemGETSNO)
        self.table.setItem(1, 3, itemTYPE)
        self.table.setItem(1, 4, itemSTATUS)
        self.table.setCellWidget(1, 5, itemWidget)

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
    #     # 书本减少的数量不能大于未借出的书本数
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
        order_type = ''
        for item in self.good_list:
            if item[0] == orderId:
                order_type = item[3]
                break
            else:
                index = index + 1
        # print('$$$$$$$$$$$$$')
        # print(self.good_info)
        temp = {}
        # print('------------')
        # print(order_type)
        if order_type == '带货':
            temp['GOOD'] = self.good_info[index][0]
            temp['GETADDR'] = self.good_info[index][1]
            temp['PUTADDR'] = self.good_info[index][2]
            temp['DATE'] = self.good_info[index][3]
            temp['MONEY'] = self.good_info[index][4]
            temp['CREDIT'] = self.good_info[index][5]
            temp['MESSAGE'] = self.good_info[index][6]
            temp['EVALUATE'] = self.good_info[index][7]
            temp['SCORE'] = self.good_info[index][8]
            self.detailOrder = GoodOrderInfo(temp)
            # print(temp)
        elif order_type == '带人':
            temp['GETADDR'] = self.good_info[index][0]
            temp['PUTADDR'] = self.good_info[index][1]
            temp['DATE'] = self.good_info[index][2]
            temp['MONEY'] = self.good_info[index][3]
            temp['CREDIT'] = self.good_info[index][4]
            temp['MESSAGE'] = self.good_info[index][5]
            temp['EVALUATE'] = self.good_info[index][6]
            temp['SCORE'] = self.good_info[index][7]
            self.detailOrder = PersonOrderInfo(temp)
        else:
            temp['SIZE'] = self.good_info[index][0]
            temp['COLOR'] = self.good_info[index][1]
            temp['WAY'] = self.good_info[index][2]
            temp['NUM'] = self.good_info[index][3]
            temp['MESSAGE'] = self.good_info[index][4]
            self.detailOrder = PrintOrderInfo(temp)
        self.detailOrder.show()
        # print("点击修改，待添加")

    # def deleteBookFunction(self, BID: str):
    #     msgBox = QMessageBox(QMessageBox.Warning, "警告!", '您将会永久删除这本书以及相关信息!',
    #                          QMessageBox.NoButton, self)
    #     msgBox.addButton("确认", QMessageBox.AcceptRole)
    #     msgBox.addButton("取消", QMessageBox.RejectRole)
    #     if msgBox.exec_() == QMessageBox.AcceptRole:
    #         ans = database.delete_book(BID)
    #         if ans:
    #             self.searchFunction()

    def deleteOrderFunction(self, orderId):
        msgBox = QMessageBox(QMessageBox.Warning, "请确认!", '请确认是否删除该订单!',
                             QMessageBox.NoButton, self)
        msgBox.addButton("确认", QMessageBox.AcceptRole)
        msgBox.addButton("取消", QMessageBox.RejectRole)
        if msgBox.exec_() == QMessageBox.AcceptRole:
            ans = DataBase.delete_order(orderId)
            if ans:
                reply = QMessageBox.about(self, "删除成功", "删除成功")
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
            font-family: 微软雅黑;
        }
        ''')
        self.searchTitle.setStyleSheet('''
            QLabel{
                font-size:25px;
                color: black;
                font-family: 微软雅黑;
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
                font-family: 微软雅黑;
            }
        ''')

class UserManage(QGroupBox):
    def __init__(self):
        super().__init__()
        self.user_list = []
        self.body = QVBoxLayout()
        self.table = None
        self.setTitleBar()
        self.setSearchBar()
        self.searchFunction()

        self.setLayout(self.body)
        self.initUI()

    # 标题栏
    def setTitleBar(self):
        self.title = QLabel()
        self.title.setText('用户管理')
        self.title.setFixedHeight(25)
        titleLayout = QHBoxLayout()
        titleLayout.addSpacing(50)
        titleLayout.addWidget(self.title)
        self.titleBar = QWidget()
        self.titleBar.setFixedSize(1000, 50)
        self.titleBar.setLayout(titleLayout)
        self.body.addWidget(self.titleBar)

    # 设置搜索框
    def setSearchBar(self):
        self.searchTitle = QLabel()
        self.searchTitle.setText('搜索学号/商家号')
        self.searchInput = QLineEdit()
        self.searchInput.setText('')
        self.searchInput.setClearButtonEnabled(True)
        self.searchInput.setFixedSize(400, 40)
        self.searchButton = QToolButton()
        self.searchButton.setFixedSize(100, 40)
        self.searchButton.setText('搜索')
        self.searchButton.clicked.connect(self.searchFunction)
        searchLayout = QHBoxLayout()
        searchLayout.addStretch()
        searchLayout.addWidget(self.searchTitle)
        searchLayout.addWidget(self.searchInput)
        searchLayout.addWidget(self.searchButton)
        searchLayout.addStretch()
        self.searchWidget = QWidget()
        self.searchWidget.setLayout(searchLayout)
        self.body.addWidget(self.searchWidget)

    # 搜索方法
    # def searchFunction(self):
    #     convert = {'书号': 'BID', '分类': 'CLASSIFICATION', '出版社': 'PRESS', '作者': 'AUTHOR', '书名': 'BNAME', '': 'BNAME'}
    #     self.book_list = database.search_book(self.searchInput.text(), convert[self.selectBox.currentText()])
    #     if self.book_list == []:
    #         print('未找到')
    #     if self.table is not None:
    #         self.table.deleteLater()
    #     self.setTable()

    def searchFunction(self):
        print('点击搜索，待添加')
        self.user_list = DataBase.search_user(self.searchInput.text())
        if self.user_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        self.searchInput.setText('')
        self.setTable()

    # 设置表格
    def setTable(self):
        self.table = QTableWidget(1, 6)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setColumnWidth(0, 160)
        self.table.setColumnWidth(1, 160)
        self.table.setColumnWidth(2, 160)
        self.table.setColumnWidth(3, 160)
        self.table.setColumnWidth(4, 160)
        self.table.setColumnWidth(5, 160)

        self.table.setItem(0, 0, QTableWidgetItem('学号/商家号'))
        self.table.setItem(0, 1, QTableWidgetItem('姓名'))
        self.table.setItem(0, 2, QTableWidgetItem('性别'))
        self.table.setItem(0, 3, QTableWidgetItem('昵称'))
        self.table.setItem(0, 4, QTableWidgetItem('信誉积分'))
        self.table.setItem(0, 5, QTableWidgetItem('操作'))

        for i in range(6):
            self.table.item(0, i).setTextAlignment(Qt.AlignCenter)
            self.table.item(0, i).setFont(QFont('微软雅黑', 15))

        # 显示订单详情
        for i in self.user_list:
            self.insertRow(i)
        self.body.addWidget(self.table)

    # 插入行
    def insertRow(self, val: list):
        itemSNO = QTableWidgetItem(val[0])
        itemSNO.setTextAlignment(Qt.AlignCenter)

        itemNAME = QTableWidgetItem(val[1])
        itemNAME.setTextAlignment(Qt.AlignCenter)

        itemGENDER = QTableWidgetItem(val[2])
        itemGENDER.setTextAlignment(Qt.AlignCenter)

        itemNICKNAME = QTableWidgetItem(val[3])
        itemNICKNAME.setTextAlignment(Qt.AlignCenter)

        itemCREDIT = QTableWidgetItem(str(val[4]))
        itemCREDIT.setTextAlignment(Qt.AlignCenter)

        itemModify = QToolButton(self.table)
        itemModify.setFixedSize(50, 25)
        itemModify.setText('修改')
        itemModify.clicked.connect(lambda: self.updateUserFunction(val[0]))
        itemModify.setStyleSheet('''
        *{
            color: white;
            font-family: 微软雅黑;
            background: rgba(38, 175, 217, 1);
            border: 0;
            border-radius: 10px;
        }
        ''')
        itemDelete = QToolButton(self.table)
        itemDelete.setFixedSize(50, 25)
        itemDelete.setText('删除')
        itemDelete.clicked.connect(lambda: self.deleteUserFunction(val[0]))
        itemDelete.setStyleSheet('''
        *{
            color: white;
                font-family: 微软雅黑;
                background: rgba(222, 52, 65, 1);
                border: 0;
                border-radius: 10px;
        }
        ''')

        itemLayout = QHBoxLayout()
        itemLayout.setContentsMargins(0, 0, 0, 0)
        itemLayout.addWidget(itemModify)
        itemLayout.addWidget(itemDelete)
        itemWidget = QWidget()
        itemWidget.setLayout(itemLayout)

        self.table.insertRow(1)
        self.table.setItem(1, 0, itemSNO)
        self.table.setItem(1, 1, itemNAME)
        self.table.setItem(1, 2, itemGENDER)
        self.table.setItem(1, 3, itemNICKNAME)
        self.table.setItem(1, 4, itemCREDIT)
        self.table.setCellWidget(1, 5, itemWidget)

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
    #     # 书本减少的数量不能大于未借出的书本数
    #     if change > book_info['NUM']:
    #         book_info['SUM'] = self.sum - book_info['NUM']
    #         book_info['NUM'] = 0
    #     else:
    #         book_info['NUM'] -= change
    #     ans = database.update_book(book_info)
    #     if ans:
    #         self.searchFunction()

    def updateUserFunction(self, sno):
        # print("点击修改，待添加")
        index = 0
        for item in self.user_list:
            if item[0] == sno:
                break
            else:
                index = index + 1
        temp = {}
        temp['ID'] = self.user_list[index][0]
        temp['NAME'] = self.user_list[index][1]
        temp['GENDER'] = self.user_list[index][2]
        temp['NICKNAME'] = self.user_list[index][3]
        temp['CREDIT'] = self.user_list[index][4]
        # self.credit = self.user_list[index][4]
        self.detailUser = UserInfo(temp)
        self.detailUser.after_close.connect(self.updateCredit)
        self.detailUser.show()

    def updateCredit(self, user_info: dict):
        print('update:  ', user_info['CREDIT'])
        ans = DataBase.update_credit(user_info)
        if ans:
            reply = QMessageBox.about(self, "更改成功", "更改成功")
            self.searchFunction()


    # def addNewBookFunction(self):
    #     self.newBookDialog = book_information.BookInfo()
    #     self.newBookDialog.show()
    #     self.newBookDialog.after_close.connect(self.addNewBook)
    #
    # def addNewBook(self, book_info: dict):
    #     ans = database.new_book(book_info)
    #     if ans:
    #         self.searchFunction()

    # def deleteBookFunction(self, BID: str):
    #     msgBox = QMessageBox(QMessageBox.Warning, "警告!", '您将会永久删除这本书以及相关信息!',
    #                          QMessageBox.NoButton, self)
    #     msgBox.addButton("确认", QMessageBox.AcceptRole)
    #     msgBox.addButton("取消", QMessageBox.RejectRole)
    #     if msgBox.exec_() == QMessageBox.AcceptRole:
    #         ans = database.delete_book(BID)
    #         if ans:
    #             self.searchFunction()

    def deleteUserFunction(self, sno):
        msgBox = QMessageBox(QMessageBox.Warning, "请确认!", '请确认是否删除该用户!',
                             QMessageBox.NoButton, self)
        msgBox.addButton("确认", QMessageBox.AcceptRole)
        msgBox.addButton("取消", QMessageBox.RejectRole)
        if msgBox.exec_() == QMessageBox.AcceptRole:
            ans = DataBase.delete_user(sno)
            if ans:
                reply = QMessageBox.about(self, "删除成功", "删除成功")
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
            font-family: 微软雅黑;
        }
        ''')
        self.searchTitle.setStyleSheet('''
            QLabel{
                font-size:25px;
                color: black;
                font-family: 微软雅黑;
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
                font-family: 微软雅黑;
            }
        ''')



class AuditManage(QWidget):
    def __init__(self):
        super().__init__()
        self.audit_list = []
        self.body = QVBoxLayout()
        self.table = None
        self.setTitleBar()
        self.setSearchBar()
        self.searchFunction()

        self.setLayout(self.body)
        self.initUI()

    # 标题栏
    def setTitleBar(self):
        self.title = QLabel()
        self.title.setText('认证审核')
        self.title.setFixedHeight(25)
        titleLayout = QHBoxLayout()
        titleLayout.addSpacing(50)
        titleLayout.addWidget(self.title)
        self.titleBar = QWidget()
        self.titleBar.setFixedSize(1000, 50)
        self.titleBar.setLayout(titleLayout)
        self.body.addWidget(self.titleBar)

    # 设置搜索框
    def setSearchBar(self):
        self.searchTitle = QLabel()
        self.searchTitle.setText('搜索学号/商家号')
        self.searchInput = QLineEdit()
        self.searchInput.setText('')
        self.searchInput.setClearButtonEnabled(True)
        self.searchInput.setFixedSize(400, 40)
        self.searchButton = QToolButton()
        self.searchButton.setFixedSize(100, 40)
        self.searchButton.setText('搜索')
        self.searchButton.clicked.connect(self.searchFunction)
        searchLayout = QHBoxLayout()
        searchLayout.addStretch()
        searchLayout.addWidget(self.searchTitle)
        searchLayout.addWidget(self.searchInput)
        searchLayout.addWidget(self.searchButton)
        searchLayout.addStretch()
        self.searchWidget = QWidget()
        self.searchWidget.setLayout(searchLayout)
        self.body.addWidget(self.searchWidget)

    # 搜索方法
    # def searchFunction(self):
    #     convert = {'书号': 'BID', '分类': 'CLASSIFICATION', '出版社': 'PRESS', '作者': 'AUTHOR', '书名': 'BNAME', '': 'BNAME'}
    #     self.book_list = database.search_book(self.searchInput.text(), convert[self.selectBox.currentText()])
    #     if self.book_list == []:
    #         print('未找到')
    #     if self.table is not None:
    #         self.table.deleteLater()
    #     self.setTable()

    def searchFunction(self):
        print('点击搜索，待添加')
        self.audit_list = DataBase.search_audit(self.searchInput.text())
        if self.audit_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        self.searchInput.setText('')
        self.setTable()

    # 设置表格
    def setTable(self):
        self.table = QTableWidget(1, 3)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setColumnWidth(0, 300)
        self.table.setColumnWidth(1, 300)
        self.table.setColumnWidth(2, 300)

        self.table.setItem(0, 0, QTableWidgetItem('学号/商家号'))
        self.table.setItem(0, 1, QTableWidgetItem('姓名'))
        self.table.setItem(0, 2, QTableWidgetItem('操作'))

        for i in range(3):
            self.table.item(0, i).setTextAlignment(Qt.AlignCenter)
            self.table.item(0, i).setFont(QFont('微软雅黑', 15))

        # 显示订单详情
        for i in self.audit_list:
            self.insertRow(i)
        self.body.addWidget(self.table)

    # 插入行
    def insertRow(self, val: list):
        itemNO = QTableWidgetItem(val[0])
        itemNO.setTextAlignment(Qt.AlignCenter)

        itemNAME = QTableWidgetItem(val[1])
        itemNAME.setTextAlignment(Qt.AlignCenter)

        itemShow = QToolButton(self.table)
        itemShow.setFixedSize(100, 30)
        itemShow.setText('查看图片')
        itemShow.clicked.connect(lambda: self.showImageFunction(val[0]))
        itemShow.setStyleSheet('''
        *{
            color: white;
            font-family: 微软雅黑;
            background: rgba(38, 175, 217, 1);
            border: 0;
            border-radius: 10px;
        }
        ''')
        itemAccess = QToolButton(self.table)
        itemAccess.setFixedSize(100, 30)
        itemAccess.setText('同意认证')
        itemAccess.clicked.connect(lambda: self.accessFunction(val))
        itemAccess.setStyleSheet('''
        *{
            color: white;
            font-family: 微软雅黑;
            background: rgba(222, 52, 65, 1);
            border: 0;
            border-radius: 10px;
        }
        ''')

        itemLayout = QHBoxLayout()
        itemLayout.setContentsMargins(0, 0, 0, 0)
        itemLayout.addWidget(itemShow)
        itemLayout.addWidget(itemAccess)
        itemWidget = QWidget()
        itemWidget.setLayout(itemLayout)

        self.table.insertRow(1)
        self.table.setItem(1, 0, itemNO)
        self.table.setItem(1, 1, itemNAME)
        self.table.setCellWidget(1, 2, itemWidget)

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
    #     # 书本减少的数量不能大于未借出的书本数
    #     if change > book_info['NUM']:
    #         book_info['SUM'] = self.sum - book_info['NUM']
    #         book_info['NUM'] = 0
    #     else:
    #         book_info['NUM'] -= change
    #     ans = database.update_book(book_info)
    #     if ans:
    #         self.searchFunction()

    def showImageFunction(self, sno):
        index = 0
        for item in self.audit_list:
            if item[0] == sno:
                break
            else:
                index = index + 1
        img_src = self.audit_list[index][2]
        self.showImage = ShowImage(img_src)
        self.showImage.show()

    # def addNewBookFunction(self):
    #     self.newBookDialog = book_information.BookInfo()
    #     self.newBookDialog.show()
    #     self.newBookDialog.after_close.connect(self.addNewBook)
    #
    # def addNewBook(self, book_info: dict):
    #     ans = database.new_book(book_info)
    #     if ans:
    #         self.searchFunction()

    # def deleteBookFunction(self, BID: str):
    #     msgBox = QMessageBox(QMessageBox.Warning, "警告!", '您将会永久删除这本书以及相关信息!',
    #                          QMessageBox.NoButton, self)
    #     msgBox.addButton("确认", QMessageBox.AcceptRole)
    #     msgBox.addButton("取消", QMessageBox.RejectRole)
    #     if msgBox.exec_() == QMessageBox.AcceptRole:
    #         ans = database.delete_book(BID)
    #         if ans:
    #             self.searchFunction()

    def accessFunction(self, val):
        msgBox = QMessageBox(QMessageBox.Warning, "请确认!", '请确认该用户是否通过审核!',
                             QMessageBox.NoButton, self)
        msgBox.addButton("确认", QMessageBox.AcceptRole)
        msgBox.addButton("取消", QMessageBox.RejectRole)
        if msgBox.exec_() == QMessageBox.AcceptRole:
            ans = DataBase.user_access(val[0])
            if ans:
                print(val[3])
                DataBase.call_cloud_function(val[3])
                reply = QMessageBox.about(self, "更改成功", "更改成功")
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
            font-family: 微软雅黑;
        }
        ''')
        self.searchTitle.setStyleSheet('''
            QLabel{
                font-size:25px;
                color: black;
                font-family: 微软雅黑;
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
                font-family: 微软雅黑;
            }
        ''')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_message = {
        'class': 'admin',
        'AID': 'admin'
    }
    ex = AdministratorPage(user_message)
    ex.show()
    sys.exit(app.exec_())
