import sys

from main_window import MainWindow
from display import Display
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Make the aplication
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()
    
    #Set icon   
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)
    
    # Display
    display = Display()
    window.addToVLayout(display)
    
    window.show()
    app.exec()