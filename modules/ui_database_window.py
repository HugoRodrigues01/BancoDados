
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DataBaseWindow(object):
    def setupUi(self, DatabaseWindow):
        DatabaseWindow.setObjectName("DatabaseWindow")
        DatabaseWindow.resize(687, 563)
        DatabaseWindow.setStyleSheet("background-color: lightgray;")
        self.centralwidget = QtWidgets.QWidget(DatabaseWindow)
        self.centralwidget.setStyleSheet("QFrame {\n"
"border: none;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_table_widget = QtWidgets.QFrame(self.centralwidget)
        self.frame_table_widget.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_table_widget.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_table_widget.setObjectName("frame_table_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_table_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.table_widget = QtWidgets.QTableWidget(self.frame_table_widget)
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(0)
        self.table_widget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.table_widget)
        self.verticalLayout.addWidget(self.frame_table_widget)
        DatabaseWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DatabaseWindow)
        QtCore.QMetaObject.connectSlotsByName(DatabaseWindow)

    def retranslateUi(self, DatabaseWindow):
        _translate = QtCore.QCoreApplication.translate
        DatabaseWindow.setWindowTitle(_translate("DatabaseWindow", "MainWindow"))
