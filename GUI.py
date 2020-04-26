from PyQt5 import QtCore, QtGui, QtWidgets
import os
import lookOnGoogle


class Ui_main_window(object):

    def setup_ui(self, main_window):
        self.central_widget = QtWidgets.QWidget(main_window)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.central_widget)
        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.directLink = QtWidgets.QRadioButton(self.central_widget)
        self.amazonBox = QtWidgets.QCheckBox(self.central_widget)
        self.linkBox = QtWidgets.QCheckBox(self.central_widget)
        self.googleBox = QtWidgets.QCheckBox(self.central_widget)
        self.letMeChooseRadioButton = QtWidgets.QRadioButton(self.central_widget)
        self.everywhereRadioButton = QtWidgets.QRadioButton(self.central_widget)
        self.searchButton = QtWidgets.QPushButton(self.central_widget)
        self.queryLineEdit = QtWidgets.QLineEdit(self.central_widget)

        main_window.setObjectName("main_window")
        main_window.resize(800, 600)
        self.central_widget.setObjectName("central_widget")

        self.queryLineEdit.setGeometry(QtCore.QRect(20, 30, 671, 31))
        self.queryLineEdit.setObjectName("plainTextEdit")
        self.queryLineEdit.returnPressed.connect(self.clicked)
        self.searchButton.setGeometry(QtCore.QRect(700, 30, 89, 31))
        self.searchButton.setObjectName("searchButton")
        # self.searchButton.setAutoDefault(True)
        # self.searchButton.setDefault(True)
        self.searchButton.clicked.connect(self.clicked)
        """selection"""
        self.everywhereRadioButton.setGeometry(QtCore.QRect(70, 90, 211, 23))
        self.everywhereRadioButton.setObjectName("everywhereRadioButton")
        self.everywhereRadioButton.setChecked(True)
        self.everywhereRadioButton.clicked.connect(self.everywhere_selection)
        self.letMeChooseRadioButton.setGeometry(QtCore.QRect(290, 90, 141, 23))
        self.letMeChooseRadioButton.setObjectName("letMeChooseRadioButton")
        self.letMeChooseRadioButton.clicked.connect(self.let_me_choose_selection)
        self.googleBox.setGeometry(QtCore.QRect(320, 120, 100, 23))
        self.googleBox.setObjectName("googleBox")
        self.googleBox.clicked.connect(self.let_me_choose_selection)
        self.linkBox.setGeometry(QtCore.QRect(320, 150, 100, 23))
        self.linkBox.setCheckable(False)
        self.linkBox.setObjectName("linkBox")
        self.linkBox.clicked.connect(self.let_me_choose_selection)
        self.amazonBox.setGeometry(QtCore.QRect(320, 180, 100, 23))
        self.amazonBox.setCheckable(False)
        self.amazonBox.setObjectName("amazonBox")
        self.amazonBox.clicked.connect(self.let_me_choose_selection)
        self.directLink.setGeometry(QtCore.QRect(500, 90, 141, 23))
        self.directLink.setObjectName("directLinkRadioButton")
        self.directLink.clicked.connect(self.direct_link_selection)
        self.directLink.setCheckable(False)

        main_window.setCentralWidget(self.central_widget)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menu_bar.setObjectName("menubar")
        main_window.setMenuBar(self.menu_bar)
        self.status_bar.setObjectName("statusbar")
        main_window.setStatusBar(self.status_bar)
        """resultsBox"""
        self.plainTextEdit.setGeometry(QtCore.QRect(15, 221, 771, 331))
        self.plainTextEdit.setObjectName("resultText")

        main_window.setCentralWidget(self.central_widget)
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("mainWindow", "Price Searcher"))
        self.searchButton.setText(_translate("mainWindow", "Search"))
        self.everywhereRadioButton.setText(_translate("mainWindow", "Search Everywhere"))
        self.letMeChooseRadioButton.setText(_translate("mainWindow", "Let Me Choose"))
        self.googleBox.setText(_translate("mainWindow", "Google ads"))
        self.linkBox.setText(_translate("mainWindow", "Links"))
        self.amazonBox.setText(_translate("mainWindow", "Amazon"))
        self.directLink.setText(_translate("mainWindow", "Direct Link"))

    def everywhere_selection(self):
        self.everywhereRadioButton.setChecked(True)
        self.letMeChooseRadioButton.setChecked(False)
        self.googleBox.setChecked(False)
        # self.linkBox.setChecked(False)
        # self.amazonBox.setChecked(False)
        self.directLink.setChecked(False)

    def let_me_choose_selection(self):
        self.everywhereRadioButton.setChecked(False)
        self.letMeChooseRadioButton.setChecked(True)
        self.googleBox.setChecked(True)
        # self.linkBox.setChecked(True)
        # self.amazonBox.setChecked(True)
        self.directLink.setChecked(False)

    def direct_link_selection(self):
        """self.everywhereRadioButton.setChecked(False)
        self.letMeChooseRadioButton.setChecked(False)
        self.googleBox.setChecked(False)
        #self.linkBox.setChecked(False)
        #self.amazonBox.setChecked(False)
        self.directLink.setChecked(True)"""

    def key_press_event(self, event):
        if event.key() == 16777216:
            self.searchButton.clicked

    def clicked(self):
        query = self.queryLineEdit.text()
        if query is not "":
            lookOnGoogle.look_on_google(query=query)
            self.plainTextEdit.appendPlainText("Google ads:")
            with open("temp_file2.txt", "r") as textFile:
                text = textFile.read()
                self.plainTextEdit.appendPlainText(text)
        else:
            self.plainTextEdit.setPlainText("nothing to search")
        os.remove("temp_file2.txt")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())


