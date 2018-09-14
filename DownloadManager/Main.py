# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 530)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 761, 481))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(50, 40, 111, 31))
        self.label_4.setStyleSheet("QLabel{\n"
"    color: rgb(255, 85, 0);\n"
"font: 13pt \"MS Shell Dlg 2\";}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(50, 90, 121, 31))
        self.label_5.setStyleSheet("QLabel{\n"
"    color: rgb(255, 85, 0);\n"
"font: 13pt \"MS Shell Dlg 2\";}")
        self.label_5.setObjectName("label_5")
        self.LE_insertvideourl = QtWidgets.QLineEdit(self.tab)
        self.LE_insertvideourl.setGeometry(QtCore.QRect(180, 40, 431, 31))
        self.LE_insertvideourl.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 10pt \"Century Gothic\";")
        self.LE_insertvideourl.setText("")
        self.LE_insertvideourl.setObjectName("LE_insertvideourl")
        self.LE_savelocation_2 = QtWidgets.QLineEdit(self.tab)
        self.LE_savelocation_2.setGeometry(QtCore.QRect(180, 90, 481, 31))
        self.LE_savelocation_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 10pt \"Century Gothic\";")
        self.LE_savelocation_2.setObjectName("LE_savelocation_2")
        self.btn_Browse_2 = QtWidgets.QPushButton(self.tab)
        self.btn_Browse_2.setGeometry(QtCore.QRect(670, 90, 71, 31))
        self.btn_Browse_2.setStyleSheet("QPushButton{\n"
"border-color: rgb(0, 170, 127);\n"
"    font: 10pt \"Century Gothic\"; \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    \n"
"    color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{background-color: rgb(255, 85, 127);\n"
"\n"
"}")
        self.btn_Browse_2.setObjectName("btn_Browse_2")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 161, 31))
        self.label_6.setStyleSheet("QLabel{\n"
"    \n"
"    \n"
"    color: rgb(0, 255, 0);\n"
"font: 12pt \"Century Gothic\";}")
        self.label_6.setObjectName("label_6")
        self.btn_download_video = QtWidgets.QPushButton(self.tab)
        self.btn_download_video.setGeometry(QtCore.QRect(300, 420, 171, 31))
        self.btn_download_video.setStyleSheet("QPushButton{ border-color: rgb(0, 170, 127); font: 12pt \"Century Gothic\"; border-radius: 50px; color: rgb(85, 255, 255); background-color: rgb(0, 85, 127); \n"
"border-radius:10px}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"  \n"
"    background-color: rgb(255, 85, 127);\n"
"}")
        self.btn_download_video.setObjectName("btn_download_video")
        self.cmb_videoinfo = QtWidgets.QComboBox(self.tab)
        self.cmb_videoinfo.setGeometry(QtCore.QRect(210, 150, 511, 31))
        self.cmb_videoinfo.setStyleSheet("font: 11pt \"Century Gothic\";")
        self.cmb_videoinfo.setObjectName("cmb_videoinfo")
        self.btn_videoinfo = QtWidgets.QPushButton(self.tab)
        self.btn_videoinfo.setGeometry(QtCore.QRect(620, 40, 121, 31))
        self.btn_videoinfo.setStyleSheet("QPushButton{\n"
"border-color: rgb(0, 170, 127);\n"
"    font: 10pt \"Century Gothic\"; \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    \n"
"    color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{background-color: rgb(255, 85, 127);\n"
"\n"
"}")
        self.btn_videoinfo.setObjectName("btn_videoinfo")
        self.progressBar_4 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_4.setGeometry(QtCore.QRect(30, 300, 701, 31))
        self.progressBar_4.setStyleSheet("QProgressBar{\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:2px solid;\n"
"    border-color: rgb(85, 85, 255);\n"
"    border-color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"text-align:center;\n"
"    color: rgb(221, 0, 166);\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
" \n"
"background-color: rgb(255, 255, 0);\n"
"width:5px;\n"
"margin:0.5px;\n"
"}")
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(30, 250, 231, 31))
        self.label_25.setStyleSheet("QLabel{\n"
"    color: rgb(255, 0, 127);\n"
"font: 13pt \"MS Shell Dlg 2\";}\n"
"")
        self.label_25.setObjectName("label_25")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 200, 161, 31))
        self.label_9.setStyleSheet("QLabel{\n"
"    \n"
"    \n"
"    color: rgb(0, 255, 0);\n"
"font: 12pt \"Century Gothic\";}")
        self.label_9.setObjectName("label_9")
        self.cmb_videoinfo_2 = QtWidgets.QComboBox(self.tab)
        self.cmb_videoinfo_2.setGeometry(QtCore.QRect(200, 200, 521, 31))
        self.cmb_videoinfo_2.setStyleSheet("font: 11pt \"Century Gothic\";")
        self.cmb_videoinfo_2.setObjectName("cmb_videoinfo_2")
        self.label_28 = QtWidgets.QLabel(self.tab)
        self.label_28.setGeometry(QtCore.QRect(30, 340, 171, 31))
        self.label_28.setStyleSheet("QLabel{\n"
"    color: rgb(255, 0, 127);\n"
"font: 13pt \"MS Shell Dlg 2\";}\n"
"")
        self.label_28.setObjectName("label_28")
        self.progressBar_5 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_5.setGeometry(QtCore.QRect(30, 380, 701, 31))
        self.progressBar_5.setStyleSheet("QProgressBar{\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:2px solid;\n"
"    border-color: rgb(85, 85, 255);\n"
"    border-color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"text-align:center;\n"
"    color: rgb(221, 0, 166);\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
" \n"
"background-color: rgb(255, 255, 0);\n"
"width:5px;\n"
"margin:0.5px;\n"
"}")
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setObjectName("progressBar_5")
        self.tabWidget.addTab(self.tab, "")
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.label_7 = QtWidgets.QLabel(self.page3)
        self.label_7.setGeometry(QtCore.QRect(40, 40, 121, 31))
        self.label_7.setStyleSheet("QLabel{\n"
"color: rgb(0, 255, 0);\n"
"font: 13pt \"MS Shell Dlg 2\";}")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page3)
        self.label_8.setGeometry(QtCore.QRect(40, 90, 121, 31))
        self.label_8.setStyleSheet("QLabel{\n"
"color: rgb(0, 255, 0);\n"
"font: 13pt \"MS Shell Dlg 2\";}")
        self.label_8.setObjectName("label_8")
        self.LE_inserturl_3 = QtWidgets.QLineEdit(self.page3)
        self.LE_inserturl_3.setGeometry(QtCore.QRect(170, 40, 551, 31))
        self.LE_inserturl_3.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 10pt \"Century Gothic\";")
        self.LE_inserturl_3.setText("")
        self.LE_inserturl_3.setObjectName("LE_inserturl_3")
        self.btn_Browse_3 = QtWidgets.QPushButton(self.page3)
        self.btn_Browse_3.setGeometry(QtCore.QRect(660, 90, 61, 31))
        self.btn_Browse_3.setStyleSheet("QPushButton{\n"
"border-color: rgb(0, 170, 127);\n"
"    font: 10pt \"Century Gothic\"; \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    \n"
"    color: rgb(0, 85, 0);\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{background-color: rgb(255, 85, 127);\n"
"\n"
"}")
        self.btn_Browse_3.setObjectName("btn_Browse_3")
        self.LE_savelocation_3 = QtWidgets.QLineEdit(self.page3)
        self.LE_savelocation_3.setGeometry(QtCore.QRect(170, 90, 481, 31))
        self.LE_savelocation_3.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 10pt \"Century Gothic\";")
        self.LE_savelocation_3.setObjectName("LE_savelocation_3")
        self.btn_Download_5 = QtWidgets.QPushButton(self.page3)
        self.btn_Download_5.setGeometry(QtCore.QRect(290, 290, 171, 31))
        self.btn_Download_5.setStyleSheet("QPushButton{ border-color: rgb(0, 170, 127); font: 12pt \"Century Gothic\"; border-radius: 50px; color: rgb(85, 255, 255); background-color: rgb(0, 85, 127); \n"
"border-radius:10px}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"  \n"
"    background-color: rgb(255, 85, 127);\n"
"}")
        self.btn_Download_5.setObjectName("btn_Download_5")
        self.tabWidget.addTab(self.page3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.LE_savelocation = QtWidgets.QLineEdit(self.tab_2)
        self.LE_savelocation.setGeometry(QtCore.QRect(150, 110, 481, 31))
        self.LE_savelocation.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 10pt \"Century Gothic\";")
        self.LE_savelocation.setObjectName("LE_savelocation")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(30, 230, 171, 31))
        self.label_3.setStyleSheet("QLabel{color: rgb(0, 138, 202);\n"
"font: 13pt \"MS Shell Dlg 2\";}\n"
"")
        self.label_3.setObjectName("label_3")
        self.btn_Browse = QtWidgets.QPushButton(self.tab_2)
        self.btn_Browse.setGeometry(QtCore.QRect(640, 110, 61, 31))
        self.btn_Browse.setStyleSheet("QPushButton{\n"
"border-color: rgb(0, 170, 127);\n"
"    font: 10pt \"Century Gothic\"; \n"
"    background-color: rgb(170, 255, 255);\n"
"    color: rgb(0, 85, 0);\n"
"    color: rgb(113, 0, 85);\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{background-color: rgb(255, 85, 127);\n"
"\n"
"}")
        self.btn_Browse.setObjectName("btn_Browse")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(40, 60, 111, 31))
        self.label.setStyleSheet("QLabel{color: rgb(0, 138, 202);\n"
"font: 13pt \"MS Shell Dlg 2\";}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 111, 31))
        self.label_2.setStyleSheet("QLabel{color: rgb(0, 138, 202);\n"
"font: 13pt \"MS Shell Dlg 2\";}")
        self.label_2.setObjectName("label_2")
        self.LE_inserturl = QtWidgets.QLineEdit(self.tab_2)
        self.LE_inserturl.setGeometry(QtCore.QRect(152, 60, 551, 31))
        self.LE_inserturl.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 10pt \"Century Gothic\";")
        self.LE_inserturl.setText("")
        self.LE_inserturl.setObjectName("LE_inserturl")
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setGeometry(QtCore.QRect(30, 270, 701, 31))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:2px solid;\n"
"    border-color: rgb(85, 85, 255);\n"
"    border-color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"text-align:center;\n"
"    color: rgb(221, 0, 166);\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
" \n"
"background-color: rgb(255, 255, 0);\n"
"width:5px;\n"
"margin:0.5px;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.btn_Download = QtWidgets.QPushButton(self.tab_2)
        self.btn_Download.setGeometry(QtCore.QRect(270, 330, 171, 31))
        self.btn_Download.setStyleSheet("QPushButton{ border-color: rgb(0, 170, 127); font: 12pt \"Century Gothic\"; border-radius: 50px; color: rgb(85, 255, 255); background-color: rgb(0, 85, 127); \n"
"border-radius:10px}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"  \n"
"    background-color: rgb(255, 85, 127);\n"
"}")
        self.btn_Download.setObjectName("btn_Download")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_26 = QtWidgets.QLabel(self.tab_5)
        self.label_26.setGeometry(QtCore.QRect(10, 20, 721, 161))
        self.label_26.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_26.setFrameShape(QtWidgets.QFrame.Box)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_5)
        self.label_27.setGeometry(QtCore.QRect(10, 190, 721, 111))
        self.label_27.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_27.setFrameShape(QtWidgets.QFrame.Box)
        self.label_27.setObjectName("label_27")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DownLoad Manager"))
        self.label_4.setText(_translate("MainWindow", "Video URL"))
        self.label_5.setText(_translate("MainWindow", "Save Location"))
        self.btn_Browse_2.setText(_translate("MainWindow", "Browser"))
        self.label_6.setText(_translate("MainWindow", "Video information"))
        self.btn_download_video.setText(_translate("MainWindow", "Start Download "))
        self.btn_videoinfo.setText(_translate("MainWindow", "Find Video info"))
        self.label_25.setText(_translate("MainWindow", "Video Download Percentage"))
        self.label_9.setText(_translate("MainWindow", "audio information"))
        self.label_28.setText(_translate("MainWindow", "audio Download Percentage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Download Youtube Video"))
        self.label_7.setText(_translate("MainWindow", "Play List URL"))
        self.label_8.setText(_translate("MainWindow", "Save Location"))
        self.btn_Browse_3.setText(_translate("MainWindow", "Browser"))
        self.btn_Download_5.setText(_translate("MainWindow", "Start Download "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page3), _translate("MainWindow", "Download Youtube playlist"))
        self.label_3.setText(_translate("MainWindow", "Download Percentage"))
        self.btn_Browse.setText(_translate("MainWindow", "Browser"))
        self.label.setText(_translate("MainWindow", "insert URL"))
        self.label_2.setText(_translate("MainWindow", "Save Location"))
        self.btn_Download.setText(_translate("MainWindow", "Start Download "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Download Files"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; text-decoration: underline; color:#00ff00;\">To Download Youtube Video plaese follow instructions: </span></p><p><span style=\" font-size:10pt;\">1- insert correct Youtube video URL</span></p><p><span style=\" font-size:10pt;\">2-Click on Find Video info and wait untill the list with different qualities and sizes to be</span></p><p><span style=\" font-size:10pt;\"> available and Choose from the video info that you want </span></p><p><span style=\" font-size:10pt;\">3- Browse to find place to save your video</span></p><p><span style=\" font-size:10pt;\">4-Click on Start Download</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; text-decoration: underline; color:#00ff00;\">To Download Youtube playlis plaese follow instructions: </span></p><p><span style=\" font-size:10pt;\">1- insert correct Youtube video URL</span></p><p><span style=\" font-size:10pt;\">3- Browse to find place to save your video</span></p><p><span style=\" font-size:10pt;\">4-Click on Start Download</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Help"))

