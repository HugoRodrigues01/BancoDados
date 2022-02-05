#!venv/bin/python3.10

from PyQt6 import QtWidgets, QtGui, QtCore
import sys
from windows.database_config_window import DataBaseConfigWindow

NAME_WINDOW: str = "DataBase"
WIDTH: int = 600
HEAIGHT: int = 350
PATH_STYLE: str = "style/style.qss"

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Loading the style
        self.load_style()

        # Load menu
        self.create_menu()

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

        # Loading the windows
        #---------------------------------------------------
        self.config_window: ConfigWindow = ConfigWindow(self)
        #---------------------------------------------------

        # The main widget of window
        self.setCentralWidget(self.container)

        # load the configs of window
        self.create_window()

    def create_window(self) -> None:
        """
        This function will be create end load all configurations of window.
        """

        # Add status bar in window
        self.status_bar: QtWidgets.QStatusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.status_bar)

        self.setWindowTitle(NAME_WINDOW)
        self.setMinimumSize(WIDTH, HEAIGHT)
        self.show()
    
    def create_widget_ui(self) -> None:

        self.font: QtGui.QFont = QtGui.QFont()
        self.font.setFamily("monospace")
        self.font.setPointSize(30)
        name_label: str = "Data<span style='font-weight: bold'>Base</span>"
        # Label 
        #---------------------------------------------------
        self.label: QtWidgets.QLabel = QtWidgets.QLabel(name_label)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(self.font)
        #---------------------------------------------------

        # Button Open Config
        #---------------------------------------------------
        self.button_config: QtWidgets.QPushButton = QtWidgets.QPushButton("Open Config")
        self.button_config.pressed.connect(self.open_config_window)
        #---------------------------------------------------

        # Button Open Database
        #---------------------------------------------------
        self.button_open_database: QtWidgets.QPushButton = QtWidgets.QPushButton("Open DataBase")
        self.button_open_database.pressed.connect(lambda: print())
        #---------------------------------------------------

        # Layout of buttons
        #---------------------------------------------------
        self.button_layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout()
        #---------------------------------------------------

        # Adding the widgets into the buttons layout
        #===================================================
        self.button_layout.addWidget(self.button_config)
        self.button_layout.addWidget(self.button_open_database)
        #===================================================

        # Adding the widgets into the main layout 
        #===================================================
        self.main_layout.addWidget(self.label)
        self.main_layout.addLayout(self.button_layout)
        #===================================================

    def create_menu(self) -> None:

        self.menu: QtWidgets.QMenuBar = self.menuBar()

        # Tools Menu
        #---------------------------------------------------
        self.menu.addMenu("&Tools")
        #---------------------------------------------------
    
    def create_actions(self) -> None: pass

    def load_style(self) -> None:

        with open(PATH_STYLE, "r", encoding="UTF-8") as file_style:

            # open style sile and read in window
            self.setStyleSheet(file_style.read())
    
    def open_config_window(self) -> None:

        self.config_window.cretae_window()

if __name__ == "__main__":

    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    window: MainWindow = MainWindow()
    sys.exit(app.exec())
