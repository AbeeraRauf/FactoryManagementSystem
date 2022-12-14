from stockrecordgenerator import generate_stock_record
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QMessageBox
import pandas as pd 
from PyQt5.QtCore import QDate
import openpyxl
from openpyxl import load_workbook
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from datetime import datetime 
from datetime import date
import datetime
 
stock_out_rolls = pd.read_excel(r'book.xlsx', index_col=None, usecols=['date','details','item_type','size','quantity','quantity_in_stock'],sheet_name='rolls_stock_in_out')
stock_out_reels = pd.read_excel(r'book.xlsx', index_col=None, usecols=['date','details','item_type','size','weight','rate'],sheet_name='reels_stock_in_out')
stock_out_totay = pd.read_excel(r'book.xlsx', index_col=None, usecols=['date','details','item_type','size','weight','rate'],sheet_name='tota_stock_in_out')


class Ui_Form3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1360, 850)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setEnabled(False)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 1360, 75))
        self.textBrowser.setStyleSheet("background-color:rgb(0, 0, 81) ;\n"
"gridline-color: rgb(0, 0, 127);\n"
"color:rgb(255,255, 255) ;")
        self.textBrowser.setObjectName("textBrowser")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(530, 100, 800, 731))
        self.tableWidget.setMaximumSize(QtCore.QSize(800, 16777215))
        font = QtGui.QFont()
         
        self.tableWidget.setFont(font)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashDotDotLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
         
        self.search_3 = QtWidgets.QGroupBox(Form)
        self.search_3.setGeometry(QtCore.QRect(30, 120, 461, 301))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_3.setFont(font)
        self.search_3.setStyleSheet("background-color: rgb(126, 255, 247);\n"
"color:rgb(0,0,81) ;")
        self.search_3.setObjectName("search_3")
        self.RollsStockbutton = QtWidgets.QRadioButton(self.search_3)
        self.RollsStockbutton.setGeometry(QtCore.QRect(160, 40, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RollsStockbutton.setFont(font)
        self.RollsStockbutton.setChecked(True)
        self.RollsStockbutton.setObjectName("RollsStockbutton")
        self.ReelsStockbutton = QtWidgets.QRadioButton(self.search_3)
        self.ReelsStockbutton.setGeometry(QtCore.QRect(160, 90, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ReelsStockbutton.setFont(font)
        self.ReelsStockbutton.setObjectName("ReelsStockbutton")
        self.Show_stock = QtWidgets.QPushButton(self.search_3)
        self.Show_stock.setGeometry(QtCore.QRect(70, 210, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Show_stock.setFont(font)
        self.Show_stock.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(0, 0, 81);"
                             "color:rgb(255,255, 255) ;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             )
        self.Show_stock.setObjectName("Show_stock")
        self.TotaStock = QtWidgets.QRadioButton(self.search_3)
        self.TotaStock.setGeometry(QtCore.QRect(160, 140, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.TotaStock.setFont(font)
        self.TotaStock.setObjectName("TotaStock")
        self.print_btn = QtWidgets.QPushButton(self.search_3)
        self.print_btn.setGeometry(QtCore.QRect(230, 210, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.print_btn.setFont(font)
        self.print_btn.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(0, 0, 81);"
                             "color:rgb(255,255, 255) ;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             )
        self.print_btn.setObjectName("print_btn")
        self.search_2 = QtWidgets.QGroupBox(Form)
        self.search_2.setGeometry(QtCore.QRect(30, 470, 461, 331))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_2.setFont(font)
        self.search_2.setStyleSheet("background-color: rgb(126, 255, 247);\n"
"color:rgb(0,0,81) ;")
        self.search_2.setObjectName("search_2")
        self.label_3 = QtWidgets.QLabel(self.search_2)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.search_stock = QtWidgets.QPushButton(self.search_2)
        self.search_stock.setGeometry(QtCore.QRect(150, 260, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.search_stock.setFont(font)
        self.search_stock.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(0, 0, 81);"
                             "color:rgb(255,255, 255) ;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             )
        self.search_stock.setObjectName("search_stock")
        self.label_2 = QtWidgets.QLabel(self.search_2)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.search_item = QtWidgets.QComboBox(self.search_2)
        self.search_item.setGeometry(QtCore.QRect(250, 70, 181, 31))
        self.search_item.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_item.setObjectName("search_item")
        self.search_item.addItem("")
        self.comboBox_size_2 = QtWidgets.QComboBox(self.search_2)
        self.comboBox_size_2.setGeometry(QtCore.QRect(250, 130, 181, 31))
        self.comboBox_size_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_size_2.setObjectName("comboBox_size_2")
        self.comboBox_size_2.addItem("")
        self.label_4 = QtWidgets.QLabel(self.search_2)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(self.search_2)
        self.dateEdit.setGeometry(QtCore.QRect(249, 190, 181, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())  
        self.dateEdit.setObjectName("dateTimeEdit") 
        self.dateEdit.setDisplayFormat("dd-MM-yyyy")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:50pt; font-weight:600;\">  Ahmed Corrugation Machines</span></p></body></html>"))
         
        
        self.search_3.setTitle(_translate("Form", "Stocks"))
        self.RollsStockbutton.setText(_translate("Form", "Rolls Stock"))
        self.ReelsStockbutton.setText(_translate("Form", "Reels Stock"))
        self.Show_stock.setText(_translate("Form", "show"))
        self.TotaStock.setText(_translate("Form", "Tota Stock"))
        self.print_btn.setText(_translate("Form", "Print"))
        self.search_2.setTitle(_translate("Form", "Search"))
        self.label_3.setText(_translate("Form", "Search By Item Type :"))
        self.search_stock.setText(_translate("Form", "Search"))
        self.label_2.setText(_translate("Form", "Search By Size:"))
        self.search_item.setItemText(0, _translate("Form", "Select from Drop Down"))
        
        self.comboBox_size_2.setItemText(0, _translate("Form", "Select from Drop Down"))
        self.label_4.setText(_translate("Form", "Search By Date:"))

        for i in range(17,53):
                 self.comboBox_size_2.addItem(str(i))
                
        def reelstable():
            global stock_out_reels
             
            df = pd.read_excel(r'book.xlsx', index_col=None, usecols=['date','details','item_type','size','weight','rate'],sheet_name='reels_stock_in_out')
            stock_out_reels=df.copy()

            self.tableWidget.clear()
            self.tableWidget.setObjectName("tableWidget")
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setRowCount(0) 
            self.tableWidget.setHorizontalHeaderLabels(('Date', 'Details','Item_type','Size','Weight','Rate'))  # set header text  
            header = self.tableWidget.horizontalHeader()       
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
            self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            rowPosition =0
            font= QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            header.setFont(font)
            stock_out_reels['date']= pd.to_datetime(stock_out_reels['date'],dayfirst=True ) .dt .strftime('%d-%m-%y')
            stock_out_reels= stock_out_reels.sort_values(by=['date' ] ,ascending=False)
            for row in stock_out_reels.iterrows():
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(row[1][0])))
                self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(row[1][1])))
                self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(row[1][2])))
                self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(row[1][3])))
                self.tableWidget.setItem(rowPosition,4, QtWidgets.QTableWidgetItem(str(row[1][4])))
                self.tableWidget.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(row[1][5])))
                rowPosition +=1  
        def totatable():
            global stock_out_totay
             
            df = pd.read_excel(r'book.xlsx', index_col=None, usecols=['date','details','item_type','size','weight','rate'],sheet_name='tota_stock_in_out')
            stock_out_totay=df.copy()

            self.tableWidget.clear()
            self.tableWidget.setObjectName("tableWidget")
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setRowCount(0) 
            self.tableWidget.setHorizontalHeaderLabels(('Date', 'Details','Item_type','Size','Weight','Rate'))  # set header text  
            header = self.tableWidget.horizontalHeader()       
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
            self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            font= QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            header.setFont(font)
            rowPosition =0
            stock_out_totay['date']= pd.to_datetime(stock_out_totay['date'],dayfirst=True ) .dt. strftime('%d-%m-%y')
            stock_out_totay= stock_out_totay.sort_values(by=['date' ] ,ascending=False)
            for row in stock_out_totay.iterrows():
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(row[1][0])))
                self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(row[1][1])))
                self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(row[1][2])))
                self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(row[1][3])))
                self.tableWidget.setItem(rowPosition,4, QtWidgets.QTableWidgetItem(str(row[1][4])))
                self.tableWidget.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(row[1][5])))
                rowPosition +=1    
                
             
        def rollstable():
            global stock_out_rolls
             
            df= pd.read_excel(r'book.xlsx', index_col=None, usecols=['date','details','item_type','size','quantity','quantity_in_stock'],sheet_name='rolls_stock_in_out')
            stock_out_rolls =df.copy()
            self.tableWidget.clear()
            self.tableWidget.setObjectName("tableWidget")
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setRowCount(0) 
            self.tableWidget.setHorizontalHeaderLabels(('Date', 'Details','Item_type','Size','Quantity','Quantity_in_stock'))  # set header text  
            header = self.tableWidget.horizontalHeader()       
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
            self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            
            font= QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setWeight(75)
            header.setFont(font)  
             
            
            stock_out_rolls['date']= pd.to_datetime(stock_out_rolls['date'] ,dayfirst=True) .dt. strftime('%d-%m-%y')
            stock_out_rolls= stock_out_rolls.sort_values(by=['date' ] ,ascending=False)
            rowPosition=0 
            
            for row in stock_out_rolls.iterrows():
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(row[1][0])))
                self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(row[1][1])))
                self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(row[1][2])))
                self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(row[1][3])))
                self.tableWidget.setItem(rowPosition,4, QtWidgets.QTableWidgetItem(str(row[1][4])))
                self.tableWidget.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(str(row[1][5])))
                rowPosition +=1    
                
                
        def itemtype_box():
            if (self.RollsStockbutton.isChecked()==True):
                rollstable()
                self.search_item.clear()
                self.search_item.addItem( "Select from Drop Down") 
                self.search_item.addItem( "Fluting") 
                self.search_item.addItem( "Fluting Bareek") 
                self.search_item.addItem( "L1") 
                self.search_item.addItem( ( "L1 Bareek"))
                self.search_item.addItem(  ( "L2"))
                self.search_item.addItem(  ( "L2 Bareek"))
                self.search_item.addItem(  ( "Test Liner"))
                self.search_item.addItem(  ( "Test Liner Bareek"))
                self.search_item.addItem(  ( "Boxboard 2.5 No"))
                self.search_item.addItem(  ( "Boxboard 2.5 Bareek"))
                self.search_item.addItem(   ( "Boxboard 3 No"))
                self.search_item.addItem(   ( "Boxboard 3 Bareek"))
                self.search_item.addItem(   ( "Local Kraft"))
                self.search_item.addItem(   ( "Local Kraft Bareek"))
                self.search_item.addItem(   ( "Imported Kraft"))
                self.search_item.addItem(   ( "Imported Kraft Bareek"))
                self.search_item.addItem(   ( "Super Fluting"))
                self.search_item.addItem(   ( "Super Fluting Bareek"))
                
            if (self.ReelsStockbutton.isChecked()==True ): 
                reelstable()
                self.search_item.clear()
                self.search_item.addItem( "Select From Drop Down") 
                self.search_item.addItem(  ( "Fluting"))
                self.search_item.addItem(  ( "L1"))
                self.search_item.addItem( ( "L2"))
                self.search_item.addItem(  ( "TL"))
                self.search_item.addItem(  ( "Kraft"))
                self.search_item.addItem( ( "Super Fluting"))
                self.search_item.addItem(  ( "BB 2.5 No"))
                self.search_item.addItem( ( "BB Coated"))
                self.search_item.addItem(  ( "BB 3 No"))
                
            if (self.TotaStock.isChecked()==True):   
                totatable()
                self.search_item.clear()
                self.search_item.addItem( "Select From Drop Down") 
                self.search_item.addItem(  ( "Fluting"))
                self.search_item.addItem(  ( "L1"))
                self.search_item.addItem( ( "L2"))
                self.search_item.addItem(  ( "TL"))
                self.search_item.addItem(  ( "Kraft"))
                self.search_item.addItem( ( "Super Fluting"))
                self.search_item.addItem(  ( "BB 2.5 No"))
                self.search_item.addItem( ( "BB Coated"))
                self.search_item.addItem(  ( "BB 3 No"))
        
        def generate_stock_pdf():
            rowscount=self.tableWidget.rowCount()
            headercount =  self.tableWidget.columnCount()
            mylist=[]
            for i in range(headercount):
                if(self.tableWidget.horizontalHeaderItem(i).text()=='Description'):
                    pass
                else:
                    mylist.append(self.tableWidget.horizontalHeaderItem(i).text())
            
            table=pd.DataFrame(columns=[self.tableWidget.horizontalHeaderItem(i).text() for i in range(headercount) if 
                            (self.tableWidget.horizontalHeaderItem(i).text()!='Description')],
                            index=[x for x in range(rowscount) if (self.tableWidget.isRowHidden(x)==False)])
            
            for row in range(rowscount):
                for col in range(headercount):
                    headertext =  self.tableWidget.horizontalHeaderItem(col).text()
                    cell =  self.tableWidget.item(row, col).text()  # get cell at row, col
                    table[headertext][row]=cell
            
            list3 = []
            list3.append(mylist)
            list2 = table.values.tolist()
            mylist = list3 + list2
            
            generate_stock_record(mylist)
                
        def searches():
            name=self.search_item.currentText().strip().lower()
            sizes=self.comboBox_size_2.currentText().strip().lower()
            dates=    self.dateEdit.date().toPyDate().strftime(  "%d-%m-%y")
             
            if( ((sizes!= "Select from Drop Down".lower()) and (name== "Select from Drop Down".lower()))): #if size is selected and name is not selected this will search enteries in sizes and return result acc to that
                columnOfInterest =3 # or whatever
                valueOfInterest =sizes 
                for rowIndex in range(self.tableWidget.rowCount()):
                    twItem1 = self.tableWidget.item(rowIndex, columnOfInterest)
                    if (int(float(valueOfInterest)) ==int(float(twItem1.text().strip()))  ):
                        self.tableWidget.setRowHidden(rowIndex, False)
                    else:
                        self.tableWidget.setRowHidden(rowIndex, True)
                    
            if( ((sizes== "Select from Drop Down".lower()) and (name!= "Select from Drop Down".lower()))): #if name/itemtype is selected and sizes is not selected this will search enteries in name/itemtype and return result acc to that
                columnOfInterest =2 # or whatever
                valueOfInterest =name 
                for rowIndex in range(self.tableWidget.rowCount()):
                    twItem1 = self.tableWidget.item(rowIndex, columnOfInterest)
                    if (  (valueOfInterest)) == (twItem1.text().strip().lower()) :
                        self.tableWidget.setRowHidden(rowIndex, False)
                    else:
                        self.tableWidget.setRowHidden(rowIndex, True)
                    

            if (name== "Select from Drop Down".lower()) and (sizes== "Select from Drop Down".lower()): #search only according to date
                
                columnOfInterest =0 # or whatever
                valueOfInterest = dates 
                for rowIndex in range(self.tableWidget.rowCount()):
                    twItem = self.tableWidget.item(rowIndex, columnOfInterest)
                    if (valueOfInterest) == twItem.text().strip() :
                        self.tableWidget.setRowHidden(rowIndex, False)
                    else:
                        self.tableWidget.setRowHidden(rowIndex, True)
             
            if( ((sizes!= "Select from Drop Down".lower()) and (name!= "Select from Drop Down".lower()))):
                                    columnOfInterest =3 # or whatever
                                    valueOfInterest =sizes 
                                    columnOfInterest2 =2# or whatever
                                    valueOfInterest2 =name 
                                    for rowIndex in range(self.tableWidget.rowCount()):
                                        twItem1 = self.tableWidget.item(rowIndex, columnOfInterest)
                                        twItem2 = self.tableWidget.item(rowIndex, columnOfInterest2)

                                        if  (int(float(valueOfInterest)) ==int(float(twItem1.text().strip()))  )and((  (valueOfInterest2)) == (twItem2.text().strip().lower())  )  :
                                            self.tableWidget.setRowHidden(rowIndex, False)
                                        else:
                                            self.tableWidget.setRowHidden(rowIndex, True)          
        self.Show_stock.clicked.connect(itemtype_box)  
        self.search_stock.clicked.connect(searches)
        self.print_btn.clicked.connect(generate_stock_pdf)
 
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form3()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
 