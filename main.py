from PyQt5.QtWidgets import *
from GUI import *
import sys


def gui_loader():
    app = QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setup_ui(main_window)

    main_window.show()
    sys.exit(app.exec_())


gui_loader()
