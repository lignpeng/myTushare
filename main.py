#-*- coding:utf-8 -*-
from __future__ import print_function
import os,sys,sip,time
from datetime import datetime,timedelta
from qtpy.QtWidgets import QTreeWidgetItem,QMenu,QApplication,QAction,QMainWindow
from qtpy import QtGui,QtWidgets
from qtpy.QtCore import Qt,QUrl,QDate,QUrlQuery
from Graph import graphpage
import layout
from pandas import DataFrame as df
import pandas as pd
import tushare as ts
import cPickle
import numpy as np
import warnings
import re
import time
import json

warnings.filterwarnings("ignore")
list1 = []

def printInfo(infoStr = None):
    if (not infoStr is None) and len(infoStr)>0:
        print('输出：' + infoStr + '-----')

class MyUi(QMainWindow):
    def __init__(self):
        super(MyUi, self).__init__()
        self.ui = layout.Ui_MainWindow()
        self.ui.setupUi(self)
        self.initStockBasic()
        curdate = time.strftime("%Y/%m/%d")  # gets current time to put into dateedit
        curdateQ = QDate.fromString(curdate,"yyyy/MM/dd")
        dateobj = datetime.strptime(curdate, "%Y/%m/%d")#converts to datetime object
        past = dateobj - timedelta(days = 7)  #minus a week to start date
        pasttime = datetime.strftime(past, "%Y/%m/%d")
        pastQ = QDate.fromString(pasttime,"yyyy/MM/dd") #convert to qtime so that widget accepts the values
        pastL = dateobj - timedelta(days=30)  # minus a month to start date
        pasttimeL = datetime.strftime(pastL, "%Y/%m/%d")
        pastQL = QDate.fromString(pasttimeL, "yyyy/MM/dd")

        self.updateStockList()
        self.ui.treeWidget.itemDoubleClicked.connect(self.addStockClickAction)
        self.ui.update_stocklist_btn.clicked.connect(self.updateStockList)
        self.ui.refreshButton.clicked.connect(self.refreshWeb)

        try:
            retain_size = self.ui.dateEdit_2.sizePolicy()
            retain_size.setRetainSizeWhenHidden(True)
            self.ui.dateEdit_2.setSizePolicy(retain_size)
            retain_size = self.ui.comboBox.sizePolicy()
            retain_size.setRetainSizeWhenHidden(True)
            self.ui.comboBox.setSizePolicy(retain_size)
            retain_size = self.ui.label_2.sizePolicy()
            retain_size.setRetainSizeWhenHidden(True)
            self.ui.label_2.setSizePolicy(retain_size)
        except AttributeError:
            print("No PYQT5 Binding! Widgets might be deformed")
        self.ui.dateEdit.setDate(pastQL)
        self.ui.dateEdit_2.setDate(curdateQ)#populate widgets
        self.ui.dateEdit.setCalendarPopup(True)
        self.ui.dateEdit_2.setCalendarPopup(True)
        self.ui.comboBox.addItems(["D", "W", "M", "5", "15", "30", "60"])
        self.ui.treeWidget_2.setDragDropMode(self.ui.treeWidget_2.InternalMove)
        self.ui.treeWidget_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.treeWidget_2.customContextMenuRequested.connect(self.openWidgetMenu)
        #双击事件
        self.ui.treeWidget_2.itemDoubleClicked.connect(self.showGraph)
        self.ui.combobox.currentIndexChanged.connect(lambda: self.modifycombo(pastQL,pastQ))

    def init_treeWidget(self, dic):
        self.ui.treeWidget.clear()
        if dic is None or not dic:
            return#校验传参是否正确
# 枚举字典，key，值
        for title,list1 in dic.items():
            parent = QTreeWidgetItem(self.ui.treeWidget)
            parent.setText(0,title)
            print(title)
            print(type(list1))
            for index,name in enumerate(list1):
                child = QTreeWidgetItem(parent)
                # print(index)
                # print(name)
                child.setText(0,name)
    #获取股票列表
    def initStockBasic(useNet=True):
        global stock_dic
        # stock_name_list,stock_index
        dataInfoName = "data/stockinfo.csv"
        dataInfoPath = os.path.abspath(os.path.join(os.path.dirname(__file__), dataInfoName))
        print(dataInfoPath)
        if os.path.exists(dataInfoPath):
            print('-------读取本地--------')
            stockBasicInfo = pd.read_csv(dataInfoPath)
            stock_name_list = stockBasicInfo['name']
            stock_index = stockBasicInfo['code'].apply(str)
        else:
            print('------下载列表-------')
            stockBasicInfo = ts.get_stock_basics()
            print(stockBasicInfo)
            stock_name_list=stockBasicInfo['name']
            stock_index = stockBasicInfo.index
            # stockBasicInfo.to_sql('tick_data',self.connection)
            stockBasicInfo.to_csv(dataInfoPath,encoding="utf8")
        list1 = []
        for i in range(len(stock_index)):
            list1.append(stock_name_list[i] +'-'+ str(stock_index[i]).zfill(6))
        stock_dic = {}
        stock_dic['所有'] = list1
        # print(stock_dic)
#更新列表，即收起来
    def updateStockList(self):
        printInfo('更新')
        self.init_treeWidget(stock_dic)
    def code_sort_tree(self, companies):
        self.ui.treeWidget.clear()
        sorted_comps = companies.sort_values(["code"])
        code_list = sorted_comps["code"].tolist()
        name_list = sorted_comps["name"].tolist()
        shares_parent = QTreeWidgetItem(self.ui.treeWidget)
        shares_parent.setText(0, "个股行情")
        for idx, val in enumerate(code_list):
            child = QTreeWidgetItem(shares_parent)
            child.setText(0, name_list[idx] + "-" + str(val))
        self.ui.treeWidget.expandToDepth(0)

    def search_comp(self, companies):
        self.ui.treeWidget.clear()
        text = self.ui.search_lineEdit.text()
        filtered_codes = companies[companies['code'].str.contains(text)]
        filtered_names = companies[companies['name'].str.contains(text)]
        filtered_comps = filtered_codes.append(filtered_names)
        code_list = filtered_comps["code"].tolist()
        name_list = filtered_comps["name"].tolist()
        parent = QTreeWidgetItem(self.ui.treeWidget)
        parent.setText(0, "搜索结果")
        for idx, val in enumerate(code_list):
            child = QTreeWidgetItem(parent)
            child.setText(0, name_list[idx] + "-" + str(val))
        self.ui.treeWidget.expandToDepth(0)


    def modifycombo(self,pastQL,pastQ):
        if self.ui.combobox.currentText()==u"复权": #if 复权 is selected, clear all existing queries to avoid value conflict
            self.ui.label_2.show()
            self.ui.dateEdit_2.show()
            self.ui.dateEdit.setDate(pastQL)
            self.ui.interval_label.show()
            self.ui.comboBox.show()
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(["hfq", "qfq"])
            self.ui.treeWidget_2.clear()
        if self.ui.combobox.currentText()==u"K线":
            self.ui.label_2.show()
            self.ui.dateEdit_2.show()
            self.ui.dateEdit.setDate(pastQL)
            self.ui.interval_label.show()
            self.ui.comboBox.show()
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(["D", "W", "M", "5", "15", "30", "60"])#same as above
            self.ui.treeWidget_2.clear()
        if self.ui.combobox.currentText()==u"分笔数据":
            self.ui.interval_label.hide()
            self.ui.comboBox.hide()
            self.ui.label_2.hide()
            self.ui.dateEdit_2.hide()
            self.ui.dateEdit.setDate(pastQ)
            self.ui.treeWidget_2.clear()
        if self.ui.combobox.currentText()==u"历史分钟":
            self.ui.interval_label.hide()
            self.ui.comboBox.show()
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(["1min","5min","15min","30min","60min"])
            self.ui.label_2.hide()
            self.ui.dateEdit_2.hide()
            self.ui.dateEdit.setDate(pastQ)
            self.ui.treeWidget_2.clear()
        if self.ui.combobox.currentText()==u"十大股东":
            self.ui.interval_label.hide()
            self.ui.comboBox.hide()
            self.ui.label_2.hide()
            self.ui.dateEdit_2.hide()
            self.ui.treeWidget_2.clear()
#第一栏的列表事件
    def methodSelected(self, action, collec):
        Choice = action.text()
        Stock = collec
        parent = QTreeWidgetItem(self.ui.treeWidget_2)
        parent.setText(0, Stock.decode("utf-8") + "-" + Choice)
    def addStockClickAction(self,item,column):
        if item is None:
            return
        text = item.text(0)
        print('text = ' + text)
        db_origin = ""
        stock = str(item.text(0).encode("utf-8"))
        action = ''
        if self.ui.combobox.currentText()==u"K线":
            action="Kline"
        if self.ui.combobox.currentText()==u"复权":
            action="Kline"
        if self.ui.combobox.currentText()==u"分笔数据":
            action="分笔"
        if self.ui.combobox.currentText()==u"历史分钟":
            action="Kline"
        if self.ui.combobox.currentText()==u"十大股东":
            action="季度饼图"
        parent = QTreeWidgetItem(self.ui.treeWidget_2)
        parent.setText(0, stock + "-" + action)

    def showGraph(self,item,column):
        if item is None:
            return
        startdate = self.ui.dateEdit.date()
        startdate = startdate.toPyDate()
        startdate = startdate.strftime("%Y/%m/%d")#转换成tushare 能识别的日期
        enddate = self.ui.dateEdit_2.date()
        enddate = enddate.toPyDate()
        enddate = enddate.strftime("%Y/%m/%d")
        option = self.ui.comboBox.currentText()
        option = str(option)
        width = self.ui.webView.width()#give width and height of user's screen so that graphs can be generated with dynamic size
        height = self.ui.webView.height()
        # print('------labels------')
        # print(labels)
        # print('-------ption------')
        print(option)
        print(startdate)
        text = item.text(0)
        arr = re.split('-',text)
        code = arr[1]
        self.downloadData(code,startdate,enddate,option)
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "index/kshape/index.html")) #path to read html file
        local_url = QUrl.fromLocalFile(file_path)
        print(type(local_url))
        query = QUrlQuery()#添加参数code=号码
        query.addQueryItem('code',code)
        query.addQueryItem('ktype',option)
        local_url.setQuery(query)
        # local_url = local_url
        print(local_url)
        self.ui.webView.load(local_url)
#第二个列表右击栏
    def openWidgetMenu(self,position):
        indexes = self.ui.treeWidget_2.selectedIndexes()
        item = self.ui.treeWidget_2.itemAt(position)
        if item == None:
            return
        #item = self.ui.listWidget.itemAt(position)
        if len(indexes) > 0:
            menu = QMenu()
            menu.addAction(QAction("Delete", menu,checkable = True))#This function is perhaps useless
            #menu.triggered.connect(self.eraseItem)
            item = self.ui.treeWidget_2.itemAt(position)
            #collec = str(item.text())
            menu.triggered.connect(lambda action: self.ListMethodSelected(action, item))
        menu.exec_(self.ui.treeWidget_2.viewport().mapToGlobal(position))
#检讨选择事件
    def ListMethodSelected(self, action, item):
        if action.text() == "Delete":
            self.eraseItem()
        if action.text() == "Combine":
            global CombineKeyword
            collec = str(item.text())
            CombineKeyword.append(collec)#Useless function(maybe?)
            list1 = [self.tr(collec)]
            self.ui.listwidget.addItems(list1)
            self.eraseItem()
#删除选择项
    def eraseItem(self):
        for x in self.ui.treeWidget_2.selectedItems():#delete with write click menu
            #item = self.ui.treewidget.takeItem(self.ui.treewidget.currentRow())
            sip.delete(x)
            #item.delete
#刷新web
    def refreshWeb(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "test.html")) 
#path to read html file "index/kshape/index.html"
        local_url = QUrl.fromLocalFile(file_path)
        self.ui.webView.load(local_url)
        # self.ui.webView.reload()
#下载K线数据，json格式保存
    def downloadData(self,stocknumber,startdate,enddate,type='D'):
        startdata = startdate.encode("ascii").replace("/","-").replace("\n","")
        print(startdata)
#convert to tushare readable date
# j = re.split("-",i)
        enddata = enddate.encode("ascii").replace("/","-").replace("\n","")
        print(enddata)
        print(stocknumber)

        array = ts.get_k_data(stocknumber, start=startdata, end=enddata, ktype=type)
        if array is None or array.empty:
            return
        print(array)
        array = array.sort_index()
        # Date = array.index.format()
        Date = array['date'].tolist()
        Open = array["open"].tolist()
        Close = array["close"].tolist()
        High = array["high"].tolist()
        Low = array["low"].tolist()
        Candlestick = zip(*[Date, Open, Close, Low, High])
        fileName = 'index/kshape/data/' + stocknumber + '-' + type + '.json'
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), fileName))
        print(file_path)
        if not os.path.exists(file_path):
            os.system(r'touch {}'.format(file_path))
        with open(file_path,"w") as f:
            json.dump(Candlestick,f)
            printInfo('下载数据保存成功')

    def graphmerge(self, combineKeyword):
        sth = ""
        for i in combineKeyword:
            if sth == "":
                sth = sth + i
            else :
                sth = sth + "\n" + "&"+ "-"+i
        list1 = sth
        return sth
        global CombineKeyword
        CombineKeyword = []
        self.ui.listwidget.clear()  #combine stuff so that different graphs can be drawn together


app = QApplication(sys.argv)
w = MyUi()
w.show()
sys.exit(app.exec_())
