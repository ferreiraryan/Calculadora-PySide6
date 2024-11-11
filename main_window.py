
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent,*args, **kwargs)
        
        # Config layout
        self.cw = QWidget()
        self.Layout = QVBoxLayout()
        self.cw.setLayout(self.Layout)
        self.setCentralWidget(self.cw)
        
        # Set title
        self.setWindowTitle("Calculadora")
        

        
        
    def adjustFixedSize(self):
        #Last ajust
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        
    def addToVLayout(self, widget: QWidget):
        self.Layout.addWidget(widget)