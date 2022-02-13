from modules import QtWidgets, QtGui, QtCore, Ui_DataBaseWindow

class DataBaseWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(DataBaseWindow, self).__init__(*args, **kwargs)

        # Loading the database window
        self.database_window: Ui_DataBaseWindow = Ui_DataBaseWindow()
        # insert QMainWindow into Ui_DataBaseWindow
        self.database_window.setupUi(self)

    def create_window(self) -> None:

        self.setWindowTitle("Database")
        self.show()
