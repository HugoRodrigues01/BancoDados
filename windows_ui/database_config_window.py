
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DataBaseConfigWindow(object):
    def setupUi(self, DataBaseConfigWindow):
        DataBaseConfigWindow.setObjectName("DataBaseConfigWindow")
        DataBaseConfigWindow.resize(673, 501)
        DataBaseConfigWindow.setMinimumSize(QtCore.QSize(0, 0))
        DataBaseConfigWindow.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.central_widget = QtWidgets.QWidget(DataBaseConfigWindow)
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_database_config = QtWidgets.QLabel(self.central_widget)
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(27)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_database_config.setFont(font)
        self.label_database_config.setStyleSheet("color: rgb(0, 0, 0);\n"
"padding-top: 10px;\n"
"background-color: none;")
        self.label_database_config.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_database_config.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
        self.label_database_config.setObjectName("label_database_config")
        self.verticalLayout_2.addWidget(self.label_database_config)
        self.horizontal_layout_button = QtWidgets.QHBoxLayout()
        self.horizontal_layout_button.setContentsMargins(-1, 0, -1, -1)
        self.horizontal_layout_button.setSpacing(0)
        self.horizontal_layout_button.setObjectName("horizontal_layout_button")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontal_layout_button.addItem(spacerItem)
        self.push_button_setting_database = QtWidgets.QPushButton(self.central_widget)
        self.push_button_setting_database.setMinimumSize(QtCore.QSize(200, 30))
        self.push_button_setting_database.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color: none;\n"
"border: none;\n"
"margin: 0px;\n"
"border-right: 1px solid back;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"QPushButton:checked {\n"
"    color: red;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}")
        self.push_button_setting_database.setCheckable(False)
        self.push_button_setting_database.setChecked(False)
        self.push_button_setting_database.setObjectName("push_button_setting_database")
        self.horizontal_layout_button.addWidget(self.push_button_setting_database)
        self.push_button_show_configs = QtWidgets.QPushButton(self.central_widget)
        self.push_button_show_configs.setMinimumSize(QtCore.QSize(200, 30))
        self.push_button_show_configs.setAutoFillBackground(False)
        self.push_button_show_configs.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color: none;\n"
"border: none;\n"
"margin: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"QPushButton:checked {\n"
"    color: red;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}")
        self.push_button_show_configs.setCheckable(False)
        self.push_button_show_configs.setChecked(False)
        self.push_button_show_configs.setDefault(False)
        self.push_button_show_configs.setObjectName("push_button_show_configs")
        self.horizontal_layout_button.addWidget(self.push_button_show_configs)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontal_layout_button.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontal_layout_button)
        self.frame_show_configs = QtWidgets.QFrame(self.central_widget)
        self.frame_show_configs.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_show_configs.setMaximumSize(QtCore.QSize(0, 0))
        self.frame_show_configs.setStyleSheet("QFrame {\n"
"border-top: 2px solid rgba(0, 0, 0, 100);\n"
"border-left: 1px solid gray;\n"
"border-right: 1px solid gray;\n"
"border-bottom: 1px solid gray;\n"
"}")
        self.frame_show_configs.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_show_configs.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_show_configs.setObjectName("frame_show_configs")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_show_configs)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.grid_layout_show_configs = QtWidgets.QGridLayout()
        self.grid_layout_show_configs.setContentsMargins(33, 15, 23, 15)
        self.grid_layout_show_configs.setHorizontalSpacing(24)
        self.grid_layout_show_configs.setVerticalSpacing(14)
        self.grid_layout_show_configs.setObjectName("grid_layout_show_configs")
        self.label_host_2 = QtWidgets.QLabel(self.frame_show_configs)
        self.label_host_2.setStyleSheet("border: none;\n"
"color: black;")
        self.label_host_2.setObjectName("label_host_2")
        self.grid_layout_show_configs.addWidget(self.label_host_2, 2, 0, 1, 1)
        self.label_connected = QtWidgets.QLabel(self.frame_show_configs)
        self.label_connected.setStyleSheet("border: none;\n"
"color: black;")
        self.label_connected.setObjectName("label_connected")
        self.grid_layout_show_configs.addWidget(self.label_connected, 5, 0, 1, 1)
        self.label_info_password = QtWidgets.QLabel(self.frame_show_configs)
        self.label_info_password.setStyleSheet("border: none;\n"
"color: black;")
        self.label_info_password.setObjectName("label_info_password")
        self.grid_layout_show_configs.addWidget(self.label_info_password, 3, 1, 1, 1)
        self.label_info_connected = QtWidgets.QLabel(self.frame_show_configs)
        self.label_info_connected.setStyleSheet("border: none;\n"
"color: black;")
        self.label_info_connected.setObjectName("label_info_connected")
        self.grid_layout_show_configs.addWidget(self.label_info_connected, 5, 1, 1, 1)
        self.label_info_user = QtWidgets.QLabel(self.frame_show_configs)
        self.label_info_user.setStyleSheet("border: none;\n"
"color: black;")
        self.label_info_user.setObjectName("label_info_user")
        self.grid_layout_show_configs.addWidget(self.label_info_user, 4, 1, 1, 1)
        self.label_info_host = QtWidgets.QLabel(self.frame_show_configs)
        self.label_info_host.setStyleSheet("border: none;\n"
"color: black;")
        self.label_info_host.setObjectName("label_info_host")
        self.grid_layout_show_configs.addWidget(self.label_info_host, 2, 1, 1, 1)
        self.label_password_2 = QtWidgets.QLabel(self.frame_show_configs)
        self.label_password_2.setStyleSheet("border: none;\n"
"color: black;")
        self.label_password_2.setObjectName("label_password_2")
        self.grid_layout_show_configs.addWidget(self.label_password_2, 3, 0, 1, 1)
        self.label_database_name_2 = QtWidgets.QLabel(self.frame_show_configs)
        self.label_database_name_2.setStyleSheet("border: none;\n"
"color: black;")
        self.label_database_name_2.setObjectName("label_database_name_2")
        self.grid_layout_show_configs.addWidget(self.label_database_name_2, 1, 0, 1, 1)
        self.label_user_2 = QtWidgets.QLabel(self.frame_show_configs)
        self.label_user_2.setStyleSheet("border: none;\n"
"color: black;")
        self.label_user_2.setObjectName("label_user_2")
        self.grid_layout_show_configs.addWidget(self.label_user_2, 4, 0, 1, 1)
        self.label_info_database_name = QtWidgets.QLabel(self.frame_show_configs)
        self.label_info_database_name.setStyleSheet("border: none;\n"
"color: black;")
        self.label_info_database_name.setObjectName("label_info_database_name")
        self.grid_layout_show_configs.addWidget(self.label_info_database_name, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.grid_layout_show_configs, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_show_configs)
        self.frame_setting_database = QtWidgets.QFrame(self.central_widget)
        self.frame_setting_database.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_setting_database.setStyleSheet("QFrame {\n"
"border-top: 2px solid rgba(0, 0, 0, 100);\n"
"}")
        self.frame_setting_database.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_setting_database.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_setting_database.setObjectName("frame_setting_database")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_setting_database)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem6, 2, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 2, 1, 1)
        self.main_layout = QtWidgets.QGridLayout()
        self.main_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.main_layout.setContentsMargins(12, 16, 3, 13)
        self.main_layout.setHorizontalSpacing(14)
        self.main_layout.setVerticalSpacing(15)
        self.main_layout.setObjectName("main_layout")
        self.horizontal_layout_password = QtWidgets.QHBoxLayout()
        self.horizontal_layout_password.setSpacing(0)
        self.horizontal_layout_password.setObjectName("horizontal_layout_password")
        self.line_edit_password = QtWidgets.QLineEdit(self.frame_setting_database)
        self.line_edit_password.setMinimumSize(QtCore.QSize(250, 30))
        self.line_edit_password.setMaximumSize(QtCore.QSize(16777215, 30))
        self.line_edit_password.setStyleSheet("QLineEdit {\n"
"\n"
"border: none;\n"
"padding-left:5px;\n"
"border-left: 2px solid rgba(0,0,0,100);\n"
"background-color: rgba(255, 255, 255, 100);\n"
"\n"
"padding: 5px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border-left: 3px solid rgba(0,0,0,100); \n"
"\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"border-left : 3px solid rgba(35, 148, 4, 200);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.line_edit_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.line_edit_password.setPlaceholderText("Password")
        self.line_edit_password.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.VisualMoveStyle)
        self.line_edit_password.setClearButtonEnabled(True)
        self.line_edit_password.setObjectName("line_edit_password")
        self.horizontal_layout_password.addWidget(self.line_edit_password)
        self.push_button_show_hide_password = QtWidgets.QPushButton(self.frame_setting_database)
        self.push_button_show_hide_password.setStyleSheet("QPushButton {\n"
"border: none;\n"
"padding: 5px;\n"
"border-radius: 2px;\n"
"margin-left: 5px; \n"
"background-color: none;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(139, 139, 139, 100);\n"
"}")
        self.push_button_show_hide_password.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("windows_ui/ui_files/../../images/icons/16x16/show_password.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("windows_ui/ui_files/../../images/icons/16x16/hide_password.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.push_button_show_hide_password.setIcon(icon)
        self.push_button_show_hide_password.setCheckable(True)
        self.push_button_show_hide_password.setChecked(True)
        self.push_button_show_hide_password.setObjectName("push_button_show_hide_password")
        self.horizontal_layout_password.addWidget(self.push_button_show_hide_password)
        self.main_layout.addLayout(self.horizontal_layout_password, 2, 2, 1, 1)
        self.radio_button_save = QtWidgets.QRadioButton(self.frame_setting_database)
        self.radio_button_save.setToolTipDuration(-1)
        self.radio_button_save.setStyleSheet("QRadioButton {\n"
"color: back;\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("windows_ui/ui_files/../../images/icons/16x16/computador(3).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.radio_button_save.setIcon(icon1)
        self.radio_button_save.setObjectName("radio_button_save")
        self.main_layout.addWidget(self.radio_button_save, 4, 2, 1, 1)
        self.label_password = QtWidgets.QLabel(self.frame_setting_database)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: none;\n"
"border: none;")
        self.label_password.setObjectName("label_password")
        self.main_layout.addWidget(self.label_password, 2, 1, 1, 1)
        self.label_user = QtWidgets.QLabel(self.frame_setting_database)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_user.setFont(font)
        self.label_user.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: none;\n"
"border: none;")
        self.label_user.setObjectName("label_user")
        self.main_layout.addWidget(self.label_user, 1, 1, 1, 1)
        self.line_edit_user = QtWidgets.QLineEdit(self.frame_setting_database)
        self.line_edit_user.setMinimumSize(QtCore.QSize(400, 30))
        self.line_edit_user.setMaximumSize(QtCore.QSize(400, 16777215))
        self.line_edit_user.setStyleSheet("QLineEdit {\n"
"border: none;\n"
"padding-left:5px;\n"
"border-left: 2px solid rgba(0,0,0,100);\n"
"background-color: rgba(255, 255, 255, 100);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border-left: 3px solid rgba(0,0,0,100); \n"
"\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"border-left : 3px solid rgba(35, 148, 4, 200);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.line_edit_user.setClearButtonEnabled(True)
        self.line_edit_user.setObjectName("line_edit_user")
        self.main_layout.addWidget(self.line_edit_user, 1, 2, 1, 1)
        self.line_edit_database_name = QtWidgets.QLineEdit(self.frame_setting_database)
        self.line_edit_database_name.setMinimumSize(QtCore.QSize(0, 30))
        self.line_edit_database_name.setMaximumSize(QtCore.QSize(400, 16777215))
        self.line_edit_database_name.setStyleSheet("QLineEdit {\n"
"border: none;\n"
"padding-left:5px;\n"
"border-left: 2px solid rgba(0,0,0,100);\n"
"background-color: rgba(255, 255, 255, 100);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border-left: 3px solid rgba(0,0,0,100); \n"
"\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"border-left : 3px solid rgba(35, 148, 4, 200);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.line_edit_database_name.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.VisualMoveStyle)
        self.line_edit_database_name.setClearButtonEnabled(True)
        self.line_edit_database_name.setObjectName("line_edit_database_name")
        self.main_layout.addWidget(self.line_edit_database_name, 3, 2, 1, 1)
        self.label_database_name = QtWidgets.QLabel(self.frame_setting_database)
        self.label_database_name.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_database_name.setFont(font)
        self.label_database_name.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: none;\n"
"border: none;")
        self.label_database_name.setObjectName("label_database_name")
        self.main_layout.addWidget(self.label_database_name, 3, 1, 1, 1)
        self.line_edit_host = QtWidgets.QLineEdit(self.frame_setting_database)
        self.line_edit_host.setMinimumSize(QtCore.QSize(400, 30))
        self.line_edit_host.setMaximumSize(QtCore.QSize(400, 16777215))
        self.line_edit_host.setStyleSheet("QLineEdit {\n"
"border: none;\n"
"padding-left:5px;\n"
"border-left: 2px solid rgba(0,0,0,100);\n"
"background-color: rgba(255, 255, 255, 100);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border-left: 3px solid rgba(0,0,0,100); \n"
"\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"border-left : 3px solid rgba(35, 148, 4, 200);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.line_edit_host.setText("")
        self.line_edit_host.setPlaceholderText("Host")
        self.line_edit_host.setClearButtonEnabled(True)
        self.line_edit_host.setObjectName("line_edit_host")
        self.main_layout.addWidget(self.line_edit_host, 0, 2, 1, 1)
        self.label_host = QtWidgets.QLabel(self.frame_setting_database)
        self.label_host.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_host.setFont(font)
        self.label_host.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: none;\n"
"border: none;")
        self.label_host.setObjectName("label_host")
        self.main_layout.addWidget(self.label_host, 0, 1, 1, 1)
        self.main_layout.setRowStretch(0, 1)
        self.gridLayout.addLayout(self.main_layout, 1, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem8, 4, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem10, 0, 1, 1, 1)
        self.horizontal_layout_buttons_sc = QtWidgets.QHBoxLayout()
        self.horizontal_layout_buttons_sc.setContentsMargins(-1, -1, -1, 9)
        self.horizontal_layout_buttons_sc.setObjectName("horizontal_layout_buttons_sc")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontal_layout_buttons_sc.addItem(spacerItem11)
        self.push_button_cancel = QtWidgets.QPushButton(self.frame_setting_database)
        self.push_button_cancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.push_button_cancel.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color: rgba(255, 0, 0, 200);\n"
"border: none;\n"
"width: 100px;\n"
"border-radius: 5px;\n"
"height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: black;\n"
"\n"
"}")
        self.push_button_cancel.setObjectName("push_button_cancel")
        self.horizontal_layout_buttons_sc.addWidget(self.push_button_cancel)
        self.push_button_save = QtWidgets.QPushButton(self.frame_setting_database)
        self.push_button_save.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.push_button_save.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color: rgba(76, 76, 76, 200);\n"
"border: none;\n"
"width: 100px;\n"
"border-radius: 5px;\n"
"height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: black;\n"
"\n"
"}")
        self.push_button_save.setObjectName("push_button_save")
        self.horizontal_layout_buttons_sc.addWidget(self.push_button_save)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontal_layout_buttons_sc.addItem(spacerItem12)
        self.gridLayout.addLayout(self.horizontal_layout_buttons_sc, 5, 1, 1, 1)
        self.frame_progress_bar = QtWidgets.QFrame(self.frame_setting_database)
        self.frame_progress_bar.setStyleSheet("border: none;\n"
"background-color: none;")
        self.frame_progress_bar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_progress_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_progress_bar.setObjectName("frame_progress_bar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_progress_bar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progress_bar_load_infos = QtWidgets.QProgressBar(self.frame_progress_bar)
        self.progress_bar_load_infos.setMinimumSize(QtCore.QSize(0, 0))
        self.progress_bar_load_infos.setMaximumSize(QtCore.QSize(16777215, 20))
        self.progress_bar_load_infos.setStyleSheet("QProgressBar {\n"
"text-align: center;\n"
"color: black;\n"
"background-color: white;\n"
"border-radius: 12px;\n"
"}\n"
"QProgressBar::chunk {\n"
"background-color: rgba(12, 99, 3, 200);\n"
"width: 5px;\n"
"padding: 5px;\n"
"\n"
"}")
        self.progress_bar_load_infos.setProperty("value", 24)
        self.progress_bar_load_infos.setObjectName("progress_bar_load_infos")
        self.verticalLayout.addWidget(self.progress_bar_load_infos)
        self.label_loadinf_infos = QtWidgets.QLabel(self.frame_progress_bar)
        self.label_loadinf_infos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_loadinf_infos.setStyleSheet("color: rgba(0, 0, 0, 180);\n"
"background-color: none;")
        self.label_loadinf_infos.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_loadinf_infos.setObjectName("label_loadinf_infos")
        self.verticalLayout.addWidget(self.label_loadinf_infos)
        self.gridLayout.addWidget(self.frame_progress_bar, 3, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_setting_database)
        DataBaseConfigWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(DataBaseConfigWindow)
        self.push_button_cancel.clicked.connect(self.line_edit_database_name.clear)
        self.push_button_cancel.clicked.connect(self.line_edit_user.clear)
        self.push_button_cancel.clicked.connect(self.line_edit_host.clear)
        self.push_button_cancel.clicked.connect(self.line_edit_password.clear)
        QtCore.QMetaObject.connectSlotsByName(DataBaseConfigWindow)
        DataBaseConfigWindow.setTabOrder(self.line_edit_host, self.line_edit_user)
        DataBaseConfigWindow.setTabOrder(self.line_edit_user, self.line_edit_password)
        DataBaseConfigWindow.setTabOrder(self.line_edit_password, self.line_edit_database_name)
        DataBaseConfigWindow.setTabOrder(self.line_edit_database_name, self.radio_button_save)
        DataBaseConfigWindow.setTabOrder(self.radio_button_save, self.push_button_cancel)
        DataBaseConfigWindow.setTabOrder(self.push_button_cancel, self.push_button_save)

    def retranslateUi(self, DataBaseConfigWindow):
        _translate = QtCore.QCoreApplication.translate
        DataBaseConfigWindow.setWindowTitle(_translate("DataBaseConfigWindow", "MainWindow"))
        self.label_database_config.setText(_translate("DataBaseConfigWindow", "DataBase Configuration"))
        self.push_button_setting_database.setText(_translate("DataBaseConfigWindow", "Setting Database"))
        self.push_button_show_configs.setText(_translate("DataBaseConfigWindow", "Show Configs"))
        self.label_host_2.setText(_translate("DataBaseConfigWindow", "Host"))
        self.label_connected.setText(_translate("DataBaseConfigWindow", "Connected"))
        self.label_info_password.setText(_translate("DataBaseConfigWindow", "3"))
        self.label_info_connected.setText(_translate("DataBaseConfigWindow", "5"))
        self.label_info_user.setText(_translate("DataBaseConfigWindow", "4"))
        self.label_info_host.setText(_translate("DataBaseConfigWindow", "2"))
        self.label_password_2.setText(_translate("DataBaseConfigWindow", "Password"))
        self.label_database_name_2.setText(_translate("DataBaseConfigWindow", "Database Name"))
        self.label_user_2.setText(_translate("DataBaseConfigWindow", "User"))
        self.label_info_database_name.setText(_translate("DataBaseConfigWindow", "1"))
        self.radio_button_save.setText(_translate("DataBaseConfigWindow", "Save"))
        self.label_password.setText(_translate("DataBaseConfigWindow", "Password"))
        self.label_user.setText(_translate("DataBaseConfigWindow", "User"))
        self.line_edit_user.setPlaceholderText(_translate("DataBaseConfigWindow", "User"))
        self.line_edit_database_name.setPlaceholderText(_translate("DataBaseConfigWindow", "Database name"))
        self.label_database_name.setText(_translate("DataBaseConfigWindow", "Database name"))
        self.label_host.setText(_translate("DataBaseConfigWindow", "Host"))
        self.push_button_cancel.setText(_translate("DataBaseConfigWindow", "Cancel"))
        self.push_button_save.setText(_translate("DataBaseConfigWindow", "Connect"))
        self.label_loadinf_infos.setText(_translate("DataBaseConfigWindow", "Loading the infos..."))
