#!venv/bin/python3.10

from PyQt6 import QtWidgets, QtGui, QtCore
import sys

NAME_WINDOW: str = "BancDaos"
WIDTH: int = 600
HEAIGHT: int = 350

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Main Layout
        #---------------------------------------------------
        self.main_layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        #---------------------------------------------------

        # Loading the widgets
        self.create_widget_ui()

        # Container of Widgets
        #---------------------------------------------------
        self.container: QtWidgets.QWidget = QtWidgets.QWidget()
        self.container.setLayout(self.main_layout)
        #---------------------------------------------------

        # The main widget of window
        self.setCentralWidget(self.container)

        # load the configs of window
        self.create_window()

    def create_window(self) -> None:
        """
        This function will be create end load all configurations of window.
        """
        self.setWindowTitle(NAME_WINDOW)
        self.setMinimumSize(WIDTH, HEAIGHT)
        self.show()
    
    def create_widget_ui(self) -> None:

        self.font: QtGui.QFont = QtGui.QFont()
        self.font.setFamily("monospace")
        self.font.setPointSize(30)
        name_label: str = "Bonco de <span style='font-weight: bold'>Dados</span>"
        # Label 
        #---------------------------------------------------
        self.label: QtWidgets.QLabel = QtWidgets.QLabel(name_label)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(self.font)
        #---------------------------------------------------

        # Adding the widgets into the main layout 
        #===================================================
        self.main_layout.addWidget(self.label)
        #===================================================

    def ceate_menu(self) -> None: pass

if __name__ == "__main__":

    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    window: MainWindow = MainWindow()
    sys.exit(app.exec())
