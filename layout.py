# -*- coding: utf-8 -*-
#coding=utf-8

# Form implementation generated from reading ui file 'advanced_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtWidgets,QtGui
from qtpy.QtWebEngineWidgets import QWebEngineView

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

# '''
# 界面布局
# '''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 396)#设置界面大小
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
#'''1、第一行的控件，combobox：选择类型'''
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.combobox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox.sizePolicy().hasHeightForWidth())

        self.combobox.setSizePolicy(sizePolicy)
        self.combobox.setObjectName("combobox")
        self.combobox.addItems(["K线", "复权", "分笔数据", "历史分钟", "十大股东"])

        self.horizontalLayout_3.addWidget(self.combobox)
        spacerItem = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        marginWidth = 90
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
# '''2、第二行的控件，label_4：搜索，search_lineEdit：输入框，search_btn：搜索按钮'''
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(48, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.search_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_lineEdit.sizePolicy().hasHeightForWidth())
        self.search_lineEdit.setSizePolicy(sizePolicy)
        self.search_lineEdit.setMinimumSize(QtCore.QSize(75, 0))
        self.search_lineEdit.setMaximumSize(QtCore.QSize(marginWidth, 16777215))
        self.search_lineEdit.setMaxLength(20)
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.horizontalLayout.addWidget(self.search_lineEdit)
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy)
        self.search_btn.setMinimumSize(QtCore.QSize(40, 0))
        self.search_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
# '''3、第三行的控件，init_category_btn：分类、init_code_btn：编号'''
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.init_category_btn = QtWidgets.QPushButton(self.centralwidget)
        self.init_category_btn.setMaximumSize(QtCore.QSize(marginWidth, 16777215))
        self.init_category_btn.setObjectName("init_category_btn")
        self.horizontalLayout_5.addWidget(self.init_category_btn)
        self.init_code_btn = QtWidgets.QPushButton(self.centralwidget)
        self.init_code_btn.setMinimumSize(QtCore.QSize(marginWidth, 0))
        self.init_code_btn.setMaximumSize(QtCore.QSize(marginWidth, 16777215))
        self.init_code_btn.setObjectName("init_code_btn")
        self.horizontalLayout_5.addWidget(self.init_code_btn)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
# '''4、展示栏，历史数据，选择类型comboBox'''
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(160, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "历史数据---右键菜单选择")
        self.gridLayout.addWidget(self.treeWidget, 3, 0, 1, 1)
# '''5、每条线时间间隔：interval_label，选择类型comboBox'''
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.interval_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.interval_label.sizePolicy().hasHeightForWidth())
        self.interval_label.setSizePolicy(sizePolicy)
        self.interval_label.setMinimumSize(QtCore.QSize(0, 0))
        self.interval_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.interval_label.setObjectName("interval_label")
        self.horizontalLayout_8.addWidget(self.interval_label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 0, 1, 1)
# '''6、时间，开始时间：staDate_label，结束时间：label_2'''
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.staDate_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.staDate_label.sizePolicy().hasHeightForWidth())
        self.staDate_label.setSizePolicy(sizePolicy)
        self.staDate_label.setMinimumSize(QtCore.QSize(80, 0))
        self.staDate_label.setMaximumSize(QtCore.QSize(marginWidth, 16777215))
        self.staDate_label.setObjectName("staDate_label")
        self.horizontalLayout_4.addWidget(self.staDate_label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
# '''7、日期选择项，dateEdit：开始时间，dateEdit_2：结束时间'''
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.dateEdit.setMaximumSize(QtCore.QSize(marginWidth, 16777215))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)#结束日期
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_2.sizePolicy().hasHeightForWidth())
        self.dateEdit_2.setSizePolicy(sizePolicy)
        self.dateEdit_2.setMinimumSize(QtCore.QSize(85, 0))
        self.dateEdit_2.setMaximumSize(QtCore.QSize(marginWidth, 16777215))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_2.addWidget(self.dateEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 1)

# '''8、执行，commandLinkButton:开始绘图'''
        self.horizontalLayout_action = QtWidgets.QHBoxLayout()
        self.horizontalLayout_action.setObjectName("horizontalLayout_action")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy)
        self.commandLinkButton.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.horizontalLayout_action.addWidget(self.commandLinkButton)

        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshButton.sizePolicy().hasHeightForWidth())
        self.refreshButton.setSizePolicy(sizePolicy)
        self.refreshButton.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.refreshButton.setFont(font)
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_action.addWidget(self.refreshButton)
        self.gridLayout.addLayout(self.horizontalLayout_action, 7, 0, 1, 1)
# '''9、绘图项：treeWidget_2'''
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_2.sizePolicy().hasHeightForWidth())
        self.treeWidget_2.setSizePolicy(sizePolicy)
        self.treeWidget_2.setMinimumSize(QtCore.QSize(160, 0))
        self.treeWidget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeWidget_2.setObjectName("treeWidget_2")
        font = QtGui.QFont("Times", 12, QtGui.QFont.Bold)
        self.treeWidget_2.setFont(font)
        self.gridLayout.addWidget(self.treeWidget_2, 8, 0, 1, 1)
# '''右边浏览web'''
        self.webView = QWebEngineView(self.centralwidget)
        self.webView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setMinimumSize(QtCore.QSize(500, 309))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.gridLayout.addWidget(self.webView, 0, 1, 9, 1)
# '''---------------'''
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1105, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action123 = QtWidgets.QAction(MainWindow)
        self.action123.setObjectName("action123")
        MainWindow.setWindowTitle("Tuchart")
        self.init_category_btn.setText("分类")
        self.init_code_btn.setText("按编号")
        self.interval_label.setText("每条线时间间隔")
        self.label_4.setText("搜索")
        self.search_btn.setText("搜索")
        self.staDate_label.setText("开始时间")
        self.label_2.setText("结束时间")
        self.treeWidget_2.headerItem().setText(0,"绘图项")
        self.commandLinkButton.setText("开始绘图")
        self.refreshButton.setText('刷新')
        self.action123.setText("123")
