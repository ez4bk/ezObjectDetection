# Form implementation generated from reading ui file 'detection_view.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_objectdetectionWindow(object):
    def setupUi(self, objectdetectionWindow):
        objectdetectionWindow.setObjectName("objectdetectionWindow")
        objectdetectionWindow.resize(1200, 800)
        objectdetectionWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.centralWidget = QtWidgets.QWidget(parent=objectdetectionWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.backgroundFrame = QtWidgets.QFrame(parent=self.centralWidget)
        self.backgroundFrame.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"border:0px solid red;\n"
"border-radius:15px\n"
"}")
        self.backgroundFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.backgroundFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.backgroundFrame.setObjectName("backgroundFrame")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.backgroundFrame)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(12)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.leftFrame = QtWidgets.QFrame(parent=self.backgroundFrame)
        self.leftFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.leftFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.leftFrame.setObjectName("leftFrame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.leftFrame)
        self.verticalLayout_12.setContentsMargins(-1, 24, -1, 24)
        self.verticalLayout_12.setSpacing(36)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.menuFrame = QtWidgets.QFrame(parent=self.leftFrame)
        self.menuFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menuFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menuFrame.setObjectName("menuFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menuFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menuList = QtWidgets.QListWidget(parent=self.menuFrame)
        self.menuList.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuList.sizePolicy().hasHeightForWidth())
        self.menuList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.menuList.setFont(font)
        self.menuList.setStyleSheet("QListView {\n"
"font: bold;\n"
"}\n"
"QListView::item{\n"
"background-color: transparent;\n"
"color: black;\n"
"padding:8px;\n"
"padding-left:4px;\n"
"margin-bottom:8px;\n"
"}\n"
"QListView::item:hover {\n"
"border-radius:8px;\n"
"background-color: rgb(240, 240, 240)\n"
"\n"
"}\n"
"QListView::item:selected {\n"
"background-color: rgb(239, 239, 239);\n"
"color: rgb(12, 20, 36);\n"
"border-radius:8px;\n"
"}\n"
"QListView::item:disabled{\n"
"color:gray\n"
"}\n"
"")
        self.menuList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.menuList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.menuList.setObjectName("menuList")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../../.designer/resources/button/首页_home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        item.setIcon(icon)
        self.menuList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(17)
        item.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../../../.designer/resources/button/设置_setting-two.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        item.setIcon(icon1)
        self.menuList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../../../../.designer/resources/button/导出_export.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        item.setIcon(icon2)
        self.menuList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../resources/button/终端_terminal.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        item.setIcon(icon3)
        self.menuList.addItem(item)
        self.verticalLayout.addWidget(self.menuList)
        self.verticalLayout_12.addWidget(self.menuFrame)
        self.verticalLayout_12.setStretch(0, 2)
        self.horizontalLayout_18.addWidget(self.leftFrame)
        self.rightFrame = QtWidgets.QFrame(parent=self.backgroundFrame)
        self.rightFrame.setStyleSheet("QFrame{\n"
"background-color: rgb(237, 235, 235);\n"
"border:0px solid red;\n"
"border-radius:15px\n"
"}\n"
"")
        self.rightFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.rightFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.rightFrame.setObjectName("rightFrame")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.rightFrame)
        self.verticalLayout_13.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_13.setSpacing(12)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.rightFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.homePage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.upperLayout = QtWidgets.QHBoxLayout()
        self.upperLayout.setContentsMargins(12, -1, 12, -1)
        self.upperLayout.setSpacing(15)
        self.upperLayout.setObjectName("upperLayout")
        self.videoFrame = QtWidgets.QFrame(parent=self.homePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoFrame.sizePolicy().hasHeightForWidth())
        self.videoFrame.setSizePolicy(sizePolicy)
        self.videoFrame.setMaximumSize(QtCore.QSize(690, 16777215))
        self.videoFrame.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.videoFrame.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:0px solid red;\n"
"    color: rgb(255, 254, 255);\n"
"    border-radius:15px\n"
"}")
        self.videoFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.videoFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.videoFrame.setObjectName("videoFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.videoFrame)
        self.horizontalLayout_4.setContentsMargins(-1, 24, -1, 24)
        self.horizontalLayout_4.setSpacing(24)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.videoView = QtWidgets.QLabel(parent=self.videoFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoView.sizePolicy().hasHeightForWidth())
        self.videoView.setSizePolicy(sizePolicy)
        self.videoView.setMaximumSize(QtCore.QSize(640, 360))
        self.videoView.setStyleSheet("background-color: b;\n"
"border-radius:15px")
        self.videoView.setText("")
        self.videoView.setScaledContents(True)
        self.videoView.setObjectName("videoView")
        self.horizontalLayout_4.addWidget(self.videoView)
        self.upperLayout.addWidget(self.videoFrame)
        self.controlFrame = QtWidgets.QFrame(parent=self.homePage)
        self.controlFrame.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border:0px solid red;\n"
"color: rgb(255, 254, 255);\n"
"border-radius:15px\n"
"}\n"
"QLabel{\n"
"font: bold;\n"
"font-size: 16;\n"
"color:b;\n"
"}\n"
"QPushButton {\n"
"background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #8a9195, stop:1 black);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #7d8488, stop:1 black);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #6a7073, stop:1 black);\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #6a7073, stop:1 black);\n"
"color: gray\n"
"}")
        self.controlFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.controlFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.controlFrame.setObjectName("controlFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.controlFrame)
        self.verticalLayout_3.setContentsMargins(18, 25, 18, 24)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.startButton = QtWidgets.QPushButton(parent=self.controlFrame)
        self.startButton.setEnabled(True)
        self.startButton.setMinimumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.verticalLayout_3.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(parent=self.controlFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setMinimumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout_3.addWidget(self.stopButton)
        self.screenshotButton = QtWidgets.QPushButton(parent=self.controlFrame)
        self.screenshotButton.setMinimumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.screenshotButton.setFont(font)
        self.screenshotButton.setObjectName("screenshotButton")
        self.verticalLayout_3.addWidget(self.screenshotButton)
        self.saveButton = QtWidgets.QPushButton(parent=self.controlFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setMinimumSize(QtCore.QSize(100, 25))
        self.saveButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout_3.addWidget(self.saveButton)
        self.saveToButton = QtWidgets.QPushButton(parent=self.controlFrame)
        self.saveToButton.setMinimumSize(QtCore.QSize(100, 25))
        self.saveToButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.saveToButton.setFont(font)
        self.saveToButton.setObjectName("saveToButton")
        self.verticalLayout_3.addWidget(self.saveToButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.totalFramLayout = QtWidgets.QHBoxLayout()
        self.totalFramLayout.setObjectName("totalFramLayout")
        self.totalFrameTitleLabel = QtWidgets.QLabel(parent=self.controlFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalFrameTitleLabel.sizePolicy().hasHeightForWidth())
        self.totalFrameTitleLabel.setSizePolicy(sizePolicy)
        self.totalFrameTitleLabel.setObjectName("totalFrameTitleLabel")
        self.totalFramLayout.addWidget(self.totalFrameTitleLabel)
        self.totalFrameLabel = QtWidgets.QLabel(parent=self.controlFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalFrameLabel.sizePolicy().hasHeightForWidth())
        self.totalFrameLabel.setSizePolicy(sizePolicy)
        self.totalFrameLabel.setObjectName("totalFrameLabel")
        self.totalFramLayout.addWidget(self.totalFrameLabel)
        self.verticalLayout_3.addLayout(self.totalFramLayout)
        self.upperLayout.addWidget(self.controlFrame)
        self.upperLayout.setStretch(0, 2)
        self.verticalLayout_5.addLayout(self.upperLayout)
        self.resultFrame = QtWidgets.QFrame(parent=self.homePage)
        self.resultFrame.setMaximumSize(QtCore.QSize(946, 300))
        self.resultFrame.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:0px solid red;\n"
"    color: rgb(255, 254, 255);\n"
"    border-radius:15px\n"
"}\n"
"QTableWidget{\n"
"color:b;\n"
"}")
        self.resultFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.resultFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.resultFrame.setObjectName("resultFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.resultFrame)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.screenshotView = QtWidgets.QLabel(parent=self.resultFrame)
        self.screenshotView.setMinimumSize(QtCore.QSize(448, 252))
        self.screenshotView.setMaximumSize(QtCore.QSize(448, 252))
        self.screenshotView.setStyleSheet("background-color: black;")
        self.screenshotView.setText("")
        self.screenshotView.setObjectName("screenshotView")
        self.horizontalLayout_3.addWidget(self.screenshotView)
        self.line = QtWidgets.QFrame(parent=self.resultFrame)
        self.line.setStyleSheet("background-color:b;")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.resultTable = QtWidgets.QTableWidget(parent=self.resultFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultTable.sizePolicy().hasHeightForWidth())
        self.resultTable.setSizePolicy(sizePolicy)
        self.resultTable.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.resultTable.setFont(font)
        self.resultTable.setStyleSheet("color:b;")
        self.resultTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.resultTable.setDragDropOverwriteMode(False)
        self.resultTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.resultTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.resultTable.setGridStyle(QtCore.Qt.PenStyle.DashLine)
        self.resultTable.setObjectName("resultTable")
        self.resultTable.setColumnCount(3)
        self.resultTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.resultTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.resultTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.resultTable.setHorizontalHeaderItem(2, item)
        self.resultTable.verticalHeader().setVisible(False)
        self.horizontalLayout_3.addWidget(self.resultTable)
        self.verticalLayout_5.addWidget(self.resultFrame)
        self.stackedWidget.addWidget(self.homePage)
        self.settingPage = QtWidgets.QWidget()
        self.settingPage.setObjectName("settingPage")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.settingPage)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.settingFrame = QtWidgets.QFrame(parent=self.settingPage)
        self.settingFrame.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border:0px solid red;\n"
"color: rgb(255, 254, 255);\n"
"border-radius:15px\n"
"}\n"
"QLabel{\n"
"font: bold;\n"
"font-size: 16;\n"
"color:b;\n"
"}\n"
"QPushButton {\n"
"background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #8a9195, stop:1 black);\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #7d8488, stop:1 black);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #6a7073, stop:1 black);\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #6a7073, stop:1 black);\n"
"color: gray\n"
"}")
        self.settingFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.settingFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.settingFrame.setObjectName("settingFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.settingFrame)
        self.verticalLayout_6.setContentsMargins(-1, 24, -1, 24)
        self.verticalLayout_6.setSpacing(24)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_9.addWidget(self.settingFrame)
        self.stackedWidget.addWidget(self.settingPage)
        self.consolePage = QtWidgets.QWidget()
        self.consolePage.setObjectName("consolePage")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.consolePage)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.consoleFrame = QtWidgets.QFrame(parent=self.consolePage)
        self.consoleFrame.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"border:0px solid red;\n"
"    color: rgb(255, 254, 255);\n"
"border-radius:30px\n"
"}")
        self.consoleFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.consoleFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.consoleFrame.setObjectName("consoleFrame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.consoleFrame)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.consoleText = QtWidgets.QTextEdit(parent=self.consoleFrame)
        self.consoleText.setObjectName("consoleText")
        self.verticalLayout_14.addWidget(self.consoleText)
        self.verticalLayout_11.addWidget(self.consoleFrame)
        self.stackedWidget.addWidget(self.consolePage)
        self.verticalLayout_13.addWidget(self.stackedWidget)
        self.horizontalLayout_18.addWidget(self.rightFrame)
        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 5)
        self.verticalLayout_2.addWidget(self.backgroundFrame)
        objectdetectionWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(objectdetectionWindow)
        self.menuList.setCurrentRow(-1)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(objectdetectionWindow)

    def retranslateUi(self, objectdetectionWindow):
        _translate = QtCore.QCoreApplication.translate
        objectdetectionWindow.setWindowTitle(_translate("objectdetectionWindow", "Real-time Object Detection - YoloV8"))
        __sortingEnabled = self.menuList.isSortingEnabled()
        self.menuList.setSortingEnabled(False)
        item = self.menuList.item(0)
        item.setText(_translate("objectdetectionWindow", "Home"))
        item = self.menuList.item(1)
        item.setText(_translate("objectdetectionWindow", "Settings"))
        item = self.menuList.item(2)
        item.setText(_translate("objectdetectionWindow", "Export Result"))
        item = self.menuList.item(3)
        item.setText(_translate("objectdetectionWindow", "Terminal"))
        self.menuList.setSortingEnabled(__sortingEnabled)
        self.startButton.setText(_translate("objectdetectionWindow", "Start"))
        self.stopButton.setText(_translate("objectdetectionWindow", "Stop"))
        self.screenshotButton.setText(_translate("objectdetectionWindow", "Screenshot"))
        self.saveButton.setText(_translate("objectdetectionWindow", "Save"))
        self.saveToButton.setText(_translate("objectdetectionWindow", "Save to.."))
        self.totalFrameTitleLabel.setText(_translate("objectdetectionWindow", "Total Frames:"))
        self.totalFrameLabel.setText(_translate("objectdetectionWindow", "0"))
        item = self.resultTable.horizontalHeaderItem(0)
        item.setText(_translate("objectdetectionWindow", "Name"))
        item = self.resultTable.horizontalHeaderItem(1)
        item.setText(_translate("objectdetectionWindow", "Frame Count"))
        item = self.resultTable.horizontalHeaderItem(2)
        item.setText(_translate("objectdetectionWindow", "Avg.  Conf."))
