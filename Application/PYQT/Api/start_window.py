import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QCheckBox
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_start_window(object):
    def setupUi(self, main_Wind):
        main_Wind.setObjectName("main_Wind")
        main_Wind.resize(250, 500)

        self.central_widg = QWidget(main_Wind)
        self.central_widg.setObjectName("central_widg")
        self.central_widg.setStyleSheet("#central_widg{background-image: url('Other/image.png'); background-position: center;}")

        self.central_layout = QVBoxLayout(self.central_widg)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setSpacing(0)

        self.frame = QFrame(self.central_widg)
        self.frame.setFixedSize(170, 520)
        self.frame.setStyleSheet("border-radius: 10px;")
        self.frame.setObjectName("frame")

        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(10, 20, 10, 20)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName("verticalLayout")

        self.profit_tree_pushButton = QPushButton(self.frame)
        self.profit_tree_pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profit_tree_pushButton.sizePolicy().hasHeightForWidth())
        self.profit_tree_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.profit_tree_pushButton.setFont(font)
        self.profit_tree_pushButton.setMouseTracking(False)
        self.profit_tree_pushButton.setTabletTracking(False)
        self.profit_tree_pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(191, 0, 153, 255), stop:1 rgba(0, 140, 178, 255))")
        self.profit_tree_pushButton.setIconSize(QtCore.QSize(16, 16))
        self.profit_tree_pushButton.setCheckable(False)
        self.profit_tree_pushButton.setChecked(False)
        self.profit_tree_pushButton.setAutoDefault(False)
        self.profit_tree_pushButton.setDefault(False)
        self.profit_tree_pushButton.setFlat(False)
        self.profit_tree_pushButton.setObjectName("profit_tree_pushButton")
        self.verticalLayout.addWidget(self.profit_tree_pushButton)

        self.prices_pushButton = QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prices_pushButton.sizePolicy().hasHeightForWidth())
        self.prices_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.prices_pushButton.setFont(font)
        self.prices_pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(191, 0, 153, 255), stop:1 rgba(0, 140, 178, 255))")
        self.prices_pushButton.setIconSize(QtCore.QSize(16, 16))
        self.prices_pushButton.setCheckable(False)
        self.prices_pushButton.setChecked(False)
        self.prices_pushButton.setAutoDefault(False)
        self.prices_pushButton.setDefault(False)
        self.prices_pushButton.setFlat(False)
        self.prices_pushButton.setObjectName("prices_pushButton_1")
        self.verticalLayout.addWidget(self.prices_pushButton)

        self.discord_bot_pushButton = QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.discord_bot_pushButton.sizePolicy().hasHeightForWidth())
        self.discord_bot_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.discord_bot_pushButton.setFont(font)
        self.discord_bot_pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(191, 0, 153, 255), stop:1 rgba(0, 140, 178, 255))")
        self.discord_bot_pushButton.setIconSize(QtCore.QSize(16, 16))
        self.discord_bot_pushButton.setCheckable(False)
        self.discord_bot_pushButton.setChecked(False)
        self.discord_bot_pushButton.setAutoDefault(False)
        self.discord_bot_pushButton.setDefault(False)
        self.discord_bot_pushButton.setFlat(False)
        self.discord_bot_pushButton.setObjectName("prices_pushButton_2")
        self.verticalLayout.addWidget(self.discord_bot_pushButton)

        self.statistics_pushButton = QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statistics_pushButton.sizePolicy().hasHeightForWidth())
        self.statistics_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.statistics_pushButton.setFont(font)
        self.statistics_pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(191, 0, 153, 255), stop:1 rgba(0, 140, 178, 255))")
        self.statistics_pushButton.setIconSize(QtCore.QSize(16, 16))
        self.statistics_pushButton.setCheckable(False)
        self.statistics_pushButton.setChecked(False)
        self.statistics_pushButton.setAutoDefault(False)
        self.statistics_pushButton.setDefault(False)
        self.statistics_pushButton.setFlat(False)
        self.statistics_pushButton.setObjectName("statistics_pushButton")
        self.verticalLayout.addWidget(self.statistics_pushButton)

        self.checkBox = QCheckBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setStyleSheet("color: white;")
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox, 0, QtCore.Qt.AlignLeft)

        self.label_bot_status = QLabel(self.frame)
        self.label_bot_status.setMinimumSize(QtCore.QSize(0, 25))
        self.label_bot_status.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_bot_status.setAlignment(QtCore.Qt.AlignCenter)
        font.setPointSize(8)

        font.setWeight(75)
        self.label_bot_status.setFont(font)
        self.label_bot_status.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(191, 0, 153, 255), stop:1 rgba(0, 140, 178, 255)); color: white;")
        self.label_bot_status.setObjectName("label_bot_status")
        self.verticalLayout.addWidget(self.label_bot_status)

        self.label_active = QLabel(self.frame)
        self.label_active.setMinimumSize(QtCore.QSize(0, 25))
        self.label_active.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_active.setAlignment(QtCore.Qt.AlignCenter)
        font.setPointSize(8)

        font.setWeight(75)
        self.label_active.setFont(font)
        self.label_active.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(191, 0, 153, 255), stop:1 rgba(0, 140, 178, 255)); color: green;")
        self.label_active.setObjectName("label_active")
        self.label_active.setText("Active")
        self.verticalLayout.addWidget(self.label_active)

        self.central_layout.addStretch()
        self.central_layout.addWidget(self.frame, 0, QtCore.Qt.AlignCenter)
        self.central_layout.addStretch()

        main_Wind.setCentralWidget(self.central_widg)

        self.retranslateUi(main_Wind)
        QtCore.QMetaObject.connectSlotsByName(main_Wind)

    def retranslateUi(self, main_Wind):
        _translate = QtCore.QCoreApplication.translate
        main_Wind.setWindowTitle(_translate("main_Wind", "MainWindow"))
        self.profit_tree_pushButton.setText(_translate("main_Wind", "Profit Tree"))
        self.prices_pushButton.setText(_translate("main_Wind", "Prices"))
        self.discord_bot_pushButton.setText(_translate("main_Wind", "Disc Bot"))
        self.statistics_pushButton.setText(_translate("main_Wind", "Statistics"))
        self.checkBox.setText(_translate("main_Wind", "Close after change"))
        self.label_bot_status.setText(_translate("main_Wind", "Bot Status"))



class MainWindow(QMainWindow, Ui_start_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

