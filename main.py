import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget, QGridLayout
from PyQt5.Qt import QLabel, QPushButton, QHBoxLayout, QVBoxLayout, Qt
from PyQt5.QtGui import QIcon


class GUI(QMainWindow):     # Inherit to QWidget
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt5")  # Setting title to the window
        self.resize(400, 300)
        self.add_menus_and_status()  # Calling to the method
        # self.position_widget_layout()
        # self.horizontal_vertical_box_layout()
        self.layout_using_grid()

    # layout using grid
    def layout_using_grid(self):
        label_1 = QLabel('Our first label')  # create and set the label
        label_2 = QLabel('Another label')
        label_span = QLabel('Label spanning columns span span span')

        button_1 = QPushButton('Click 1')
        button_2 = QPushButton('Click 2')

        grid_layout = QGridLayout()
        # set columns and row
        grid_layout.addWidget(label_1, 0, 0)
        grid_layout.addWidget(button_1, 0, 1)
        grid_layout.addWidget(label_2, 1, 0)
        grid_layout.addWidget(button_2, 1, 1)
        # set item label with span
        grid_layout.addWidget(label_span, 2, 0, 1, 3)
        # set horientation of the items
        grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        grid_layout.setAlignment(label_1, Qt.AlignRight)
        grid_layout.setAlignment(label_2, Qt.AlignRight)

        layout_widget = QWidget()
        layout_widget.setLayout(grid_layout)

        self.setCentralWidget(layout_widget)

    # layout uing box
    def horizontal_vertical_box_layout(self):
        label_1 = QLabel('Our first label')  # create and set the label
        label_2 = QLabel('Another label')

        button_1 = QPushButton('Click 1')
        button_2 = QPushButton('Click 2')

        hbox_1 = QHBoxLayout()
        hbox_1.addStretch()
        hbox_2 = QHBoxLayout()
        hbox_2.addStretch()

        hbox_1.addWidget(label_1)
        hbox_1.addWidget(button_1)

        hbox_2.addWidget(label_2)
        hbox_2.addWidget(button_2)

        vbox = QVBoxLayout()
        vbox.addStretch()  #fijarlo hasta abajo

        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)

        layout_widget = QWidget()  # Create the object
        layout_widget.setLayout(vbox)

        self.setCentralWidget(layout_widget)

    # set widget for position
    def position_widget_layout(self):
        label_1 = QLabel('Our first label', self)  # create and set the label

        print(self.menuBar().size())  # siza default 100, 30
        mbar_height = self.menuBar().height()
        print(mbar_height)
        label_1.move(10, mbar_height)  # move the label in the window

        label_2 = QLabel('Another label', self)
        label_2.move(10, mbar_height * 2)

        button_1 = QPushButton('Click 1', self)
        button_2 = QPushButton('Click 2', self)

        button_1.move(label_1.width(), label_1.height())
        button_2.move(label_2.width(), label_2.height() * 2)

    def add_menus_and_status(self):
        self.statusBar().showMessage('Text in status bar')  # Like a label in teh botom

        menu_bar = self.menuBar()      # Creating a menu bar
        # Menus items
        file_menu = menu_bar.addMenu('File')  # add menu to menu bar

        new_icon = QIcon('icons/new_icon.png')  # Creating a icon
        new_action = QAction(new_icon, 'New', self)  # Create an action to file_menu
        new_action.setStatusTip('New File')  # update the message in the status of the bottom
        file_menu.addAction(new_action)  # Add the action to the menu_file

        # separador
        file_menu.addSeparator()

        # new option to the same row
        exit_icon = QIcon('icons/exit_icon.png')
        exit_action = QAction(exit_icon, 'Exit', self)
        exit_action.setStatusTip('Click to exit to the application')
        exit_action.triggered.connect(self.close)     # Close the app
        exit_action.setShortcut('Ctrl+q')               # close the app with ctrl+q
        file_menu.addAction(exit_action)

        edit_menu = menu_bar.addMenu('Edit')


if __name__ == '__main__':
    app = QApplication(sys.argv)   # Creating application
    gui = GUI()                     # Set the gui of the aplication
    gui.show()                      # Creating the gui
    sys.exit(app.exec_())           #  Running the gui







