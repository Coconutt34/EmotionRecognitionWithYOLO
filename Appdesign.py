# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Appdesign.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 730)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setToolTipDuration(0)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	padding:10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(40, 450, 931, 192))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(192)
        sizePolicy1.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy1)
        self.textBrowser.setMinimumSize(QSize(0, 192))
        self.textBrowser.setMaximumSize(QSize(16777215, 192))
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"    border: 2px solid rgba(80, 80, 80, 0.13); /* \u0426\u0432\u0435\u0442 \u0438 \u0442\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0430\u043c\u043a\u0438 */\n"
"    border-radius: 20px;       /* \u0420\u0430\u0434\u0438\u0443\u0441 \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f */\n"
"    background-color: white;   /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    padding: 8px;              /* \u041e\u0442\u0441\u0442\u0443\u043f \u0442\u0435\u043a\u0441\u0442\u0430 \u043e\u0442 \u043a\u0440\u0430\u0435\u0432 */\n"
"	background-color: rgba(90, 90, 90, 0.13);  /*\u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 (\u0442\u0435\u043c\u043d\u0435\u0435) */\n"
"	color: rgba(20, 20, 18, 0.4);     /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 (\u0447\u0442\u043e\u0431\u044b \u043e\u043d \u0431\u044b\u043b \u0432\u0438\u0434\u0435\u043d \u043d\u0430 \u0442\u0435\u043c\u043d\u043e\u043c \u0444\u043e\u043d\u0435)*/\n"
"	/*layoutTopMargin: 10px;/* \u0412"
                        "\u043d\u0435\u0448\u043d\u0438\u0435 \u043e\u0441\u0442\u0443\u043f\u044b*/\n"
"	/*layoutBottomMargin: 10px;\n"
"	\n"
"	\n"
"	\n"
"}")
        self.textBrowser.setOpenExternalLinks(False)
        self.camButton = QPushButton(self.centralwidget)
        self.camButton.setObjectName(u"camButton")
        self.camButton.setGeometry(QRect(160, 560, 60, 60))
        self.camButton.setMinimumSize(QSize(60, 60))
        self.camButton.setMaximumSize(QSize(60, 60))
        self.camButton.setStyleSheet(u"QPushButton {\n"
"    /* \u041e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u0437\u0430\u0434\u0430\u0435\u043c \u0440\u0430\u043c\u043a\u0443 \u0438\u043b\u0438 \u0444\u043e\u043d, \u0438\u043d\u0430\u0447\u0435 \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043c\u043e\u0436\u0435\u0442 \u043d\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c\u0441\u044f */\n"
"    border: 2px solid #8f8f91; \n"
"    background-color: #d1d1d1;\n"
"\n"
"    border-image: url('C:\\Users\\INTEL\\Desktop\\webcam.png');\n"
"    /* \u0420\u0430\u0434\u0438\u0443\u0441 = \u041f\u043e\u043b\u043e\u0432\u0438\u043d\u0430 \u0448\u0438\u0440\u0438\u043d\u044b/\u0432\u044b\u0441\u043e\u0442\u044b */\n"
"    border-radius: 30px; \n"
"}\n"
"\n"
"/* \u042d\u0444\u0444\u0435\u043a\u0442 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 (\u043f\u043e \u0436\u0435\u043b\u0430\u043d\u0438\u044e) */\n"
"QPushButton:pressed {\n"
"    background-color: #aaaaaa;\n"
"}")
        icon = QIcon()
        icon.addFile(u"webcam.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camButton.setIcon(icon)
        self.camButton.setIconSize(QSize(36, 36))
        self.videoButton = QPushButton(self.centralwidget)
        self.videoButton.setObjectName(u"videoButton")
        self.videoButton.setGeometry(QRect(60, 560, 60, 60))
        self.videoButton.setMinimumSize(QSize(60, 60))
        self.videoButton.setMaximumSize(QSize(60, 60))
        self.videoButton.setToolTipDuration(0)
        self.videoButton.setStyleSheet(u"QPushButton {\n"
"    /* \u041e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u0437\u0430\u0434\u0430\u0435\u043c \u0440\u0430\u043c\u043a\u0443 \u0438\u043b\u0438 \u0444\u043e\u043d, \u0438\u043d\u0430\u0447\u0435 \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043c\u043e\u0436\u0435\u0442 \u043d\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c\u0441\u044f */\n"
"    border: 2px solid #8f8f91; \n"
"    background-color: #d1d1d1;\n"
"\n"
"    border-image: url('C:\\Users\\INTEL\\Desktop\\webcam.png');\n"
"    /* \u0420\u0430\u0434\u0438\u0443\u0441 = \u041f\u043e\u043b\u043e\u0432\u0438\u043d\u0430 \u0448\u0438\u0440\u0438\u043d\u044b/\u0432\u044b\u0441\u043e\u0442\u044b */\n"
"    border-radius: 30px; \n"
"}\n"
"\n"
"/* \u042d\u0444\u0444\u0435\u043a\u0442 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 (\u043f\u043e \u0436\u0435\u043b\u0430\u043d\u0438\u044e) */\n"
"QPushButton:pressed {\n"
"    background-color: #aaaaaa;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"videoicon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.videoButton.setIcon(icon1)
        self.videoButton.setIconSize(QSize(36, 36))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:16pt; font-style:italic;\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0442\u043a\u0443\u0434\u0430 \u0431\u0443\u0434\u0435\u0442 \u0438\u0434\u0442\u0438 \u0432\u0438\u0434\u0435\u043e\u043f\u043e\u0442\u043e\u043a.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:16pt; font-style:italic;\">\u041f\u0440\u0438 \u0432\u044b\u0431\u043e\u0440\u0435 \u0432\u0435\u0431"
                        "-\u043a\u0430\u043c\u0435\u0440\u044b \u0441\u0434\u0435\u043b\u0430\u0439\u0442\u0435 \u0434\u0432\u043e\u0439\u043d\u043e\u0439 \u0449\u0435\u043b\u0447\u043e\u043a</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.camButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0440\u0430\u0431\u043e\u0442\u0443\u044e\u0449\u0443\u044e \u0432\u0435\u0431-\u043a\u0430\u043c\u0435\u0440\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.camButton.setText("")
#if QT_CONFIG(tooltip)
        self.videoButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0432\u0438\u0434\u0435\u043e\u0444\u0430\u0439\u043b", None))
#endif // QT_CONFIG(tooltip)
        self.videoButton.setText("")
    # retranslateUi

