import string
from PyQt5 import QtCore, QtWidgets

class PlainTextEdit(QtWidgets.QTextEdit):
    
    
    def keyPressEvent(self, event):
        ### Allow digit 0 to 9 and Key_Backspace

        
        allow_keys={48,49,50,51,52,53,54,55,56,57,58,QtCore.Qt.Key.Key_Backspace}
        if event.key() not in allow_keys:    
            event.ignore()
            return
        
        sending_name =self.sender()
        obj_name = sending_name.objectName()
        super(PlainTextEdit, self).keyPressEvent(event)
    def sender(self):
        return self
