from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog



class InfoDialogWindow(QtWidgets.QDialog):
    def __init__(self, item_info: dict, parent=None):
        super(InfoDialogWindow, self).__init__(parent)

        self.item_info = item_info

        self.setupUi(self)

        self.settings = QtCore.QSettings("Parser", "info_dialog")
        self.load_settings()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 200)
        Dialog.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.main_frame = QtWidgets.QFrame(Dialog)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_horizontalFrame = QtWidgets.QFrame(self.main_frame)
        self.name_horizontalFrame.setObjectName("name_horizontalFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.name_horizontalFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.name_label = QtWidgets.QLabel(self.name_horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_3.addWidget(self.name_label, 0, QtCore.Qt.AlignHCenter)
        self.name_value = QtWidgets.QLabel(self.name_horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_value.sizePolicy().hasHeightForWidth())
        self.name_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_value.setFont(font)
        self.name_value.setObjectName("name_value")
        self.horizontalLayout_3.addWidget(self.name_value, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.name_horizontalFrame)
        
        self.tier_horizontalFrame = QtWidgets.QFrame(self.main_frame)
        self.tier_horizontalFrame.setObjectName("tier_horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tier_horizontalFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tier_label = QtWidgets.QLabel(self.tier_horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tier_label.sizePolicy().hasHeightForWidth())
        self.tier_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tier_label.setFont(font)
        self.tier_label.setObjectName("tier_label")
        self.horizontalLayout.addWidget(self.tier_label, 0, QtCore.Qt.AlignHCenter)
        self.tier_value = QtWidgets.QLabel(self.tier_horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tier_value.sizePolicy().hasHeightForWidth())
        self.tier_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tier_value.setFont(font)
        self.tier_value.setObjectName("tier_value")
        self.horizontalLayout.addWidget(self.tier_value, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.tier_horizontalFrame)
        
        self.enchant_horizontalFrame = QtWidgets.QFrame(self.main_frame)
        self.enchant_horizontalFrame.setObjectName("enchant_horizontalFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.enchant_horizontalFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.enchant_label = QtWidgets.QLabel(self.enchant_horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enchant_label.sizePolicy().hasHeightForWidth())
        self.enchant_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enchant_label.setFont(font)
        self.enchant_label.setObjectName("enchant_label")
        self.horizontalLayout_2.addWidget(self.enchant_label, 0, QtCore.Qt.AlignHCenter)
        self.enchant_value = QtWidgets.QLabel(self.enchant_horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enchant_value.sizePolicy().hasHeightForWidth())
        self.enchant_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enchant_value.setFont(font)
        self.enchant_value.setObjectName("enchant_value")
        self.horizontalLayout_2.addWidget(self.enchant_value, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.enchant_horizontalFrame)
        
        self.day_horizontalFrame = QtWidgets.QFrame(self.main_frame)
        self.day_horizontalFrame.setObjectName("day_horizontalFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.day_horizontalFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.day_label = QtWidgets.QLabel(self.day_horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.day_label.sizePolicy().hasHeightForWidth())
        self.day_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.day_label.setFont(font)
        self.day_label.setObjectName("day_label")
        self.horizontalLayout_4.addWidget(self.day_label, 0, QtCore.Qt.AlignHCenter)
        self.day_value = QtWidgets.QLabel(self.day_horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.day_value.sizePolicy().hasHeightForWidth())
        self.day_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.day_value.setFont(font)
        self.day_value.setObjectName("day_value")
        self.horizontalLayout_4.addWidget(self.day_value, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.day_horizontalFrame)
        
        self.step_h_horizontalFrame = QtWidgets.QFrame(self.main_frame)
        self.step_h_horizontalFrame.setObjectName("step_h_horizontalFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.step_h_horizontalFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.step_h_label = QtWidgets.QLabel(self.step_h_horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step_h_label.sizePolicy().hasHeightForWidth())
        self.step_h_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.step_h_label.setFont(font)
        self.step_h_label.setObjectName("step_h_label")
        self.horizontalLayout_5.addWidget(self.step_h_label, 0, QtCore.Qt.AlignHCenter)
        self.step_h_value = QtWidgets.QLabel(self.step_h_horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step_h_value.sizePolicy().hasHeightForWidth())
        self.step_h_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.step_h_value.setFont(font)
        self.step_h_value.setObjectName("step_h_value")
        self.horizontalLayout_5.addWidget(self.step_h_value, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.step_h_horizontalFrame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.name_label.setText(_translate("Dialog", "Name"))
        self.name_value.setText(_translate("Dialog", self.item_info["item"]))
        self.tier_label.setText(_translate("Dialog", "Tier"))
        self.tier_value.setText(_translate("Dialog", self.item_info["tier_min"] + "-" + self.item_info["tier_max"]))
        self.enchant_label.setText(_translate("Dialog", "Enchant"))
        self.enchant_value.setText(_translate("Dialog", self.item_info["enchant_min"] + "-" + self.item_info["enchant_max"]))
        self.day_label.setText(_translate("Dialog", "Day"))
        self.day_value.setText(_translate("Dialog", self.item_info["days"]))
        self.step_h_label.setText(_translate("Dialog", "Step-H"))
        self.step_h_value.setText(_translate("Dialog", self.item_info["step_h"]))

# ----------------------------------------------------------------
# Window methods for controlling the state of the application window

    def resizeEvent(self, event):
        super(InfoDialogWindow, self).resizeEvent(event)
        self.main_frame.setGeometry(self.rect())

    def load_settings(self):
        width = self.settings.value("dialogWidth", 200, type=int)
        height = self.settings.value("dialogHeight", 200, type=int)
        self.resize(width, height)

        position = self.settings.value("dialogPosition", QtCore.QPoint(100, 100), type=QtCore.QPoint)
        self.move(position)

    def closeEvent(self, event):
        self.settings.setValue("dialogWidth", self.width())
        self.settings.setValue("dialogHeight", self.height())
        self.settings.setValue("dialogPosition", self.pos())  
        super(InfoDialogWindow, self).closeEvent(event)


# ----------------------------------------------------------------
# Set information





