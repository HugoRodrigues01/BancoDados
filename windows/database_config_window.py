from modules import QtWidgets, QtGui, QtCore, Ui_DataBaseConfigWindow
from classes.connect_config_json_file import ConfigJSON

class DataBaseConfigWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super(DataBaseConfigWindow, self).__init__(*args, **kwargs)

        # Loading the database config window
        self.window_ui: Ui_DataBaseConfigWindow = Ui_DataBaseConfigWindow()
        # insert the QMainWindow into the database config window
        self.window_ui.setupUi(self)

        # Loading the dependences  of window
        #---------------------------------------------------
        self.loading_depedences()
        #---------------------------------------------------

    def create_window(self) -> None:
        
        self.window_ui.frame_show_configs.hide()
        self.window_ui.frame_progress_bar.hide()
        self.setWindowTitle("Config DataBase")
        self.show()
    
    def change_echo_mode(self) -> None:

        if self.window_ui.line_edit_password.echoMode() == QtWidgets.QLineEdit.EchoMode.Password:
            self.window_ui.line_edit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        
        else:
            self.window_ui.line_edit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def loading_depedences(self) -> None:

        # Change the max-size of frame_show_configs
        self.window_ui.frame_show_configs.setMaximumSize(QtCore.QSize(16777215, 16777215))

        # Change echo mode pedendence
        #---------------------------------------------------
        self.window_ui.push_button_show_hide_password.pressed.connect(self.change_echo_mode)
        #---------------------------------------------------

        # Open frames dependences
        #---------------------------------------------------
        self.window_ui.push_button_show_configs.pressed.connect(self.open_show_configs)

        self.window_ui.push_button_setting_database.pressed.connect(self.open_setting_database)
        #---------------------------------------------------
    

    def open_show_configs(self) -> None:

        self.window_ui.frame_setting_database.hide()
        self.window_ui.frame_show_configs.show()
    
    def open_setting_database(self) -> None:

        self.window_ui.frame_show_configs.hide()
        self.window_ui.frame_setting_database.show()

