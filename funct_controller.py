from sensor import *
from main_view import *
from room import *
import sys
from PyQt5.QtWidgets import *


 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    dialog = DlgRoomDataInput()
    window.setup_buttons()
    window.setup_labels()
    sys.exit(app.exec_())


