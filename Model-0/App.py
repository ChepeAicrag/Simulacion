import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('gui.iu', self)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_gui = App()
    app_gui.show()
    sys.exit(app.exec_())