from main_view import *
from PyQt5.QtWidgets import *
from PyQt5 import uic


class DlgRoomDataInput(QDialog):
    def __init__(self):
        super().__init__()
        self.__room_name = None
        self.__target_temp = None
        self.__target_hm = None
        
        uic.loadUi("hum_dialog.ui", self)
        
        buttonbox = self.findChild(QDialogButtonBox, "buttonBox")
        self.handler = DlgRoomDataInputHandler()
        buttonbox.accepted.connect(self.handler.create_room_object)
        buttonbox.rejected.connect(self.close)
        
        le1 = self.findChild(QLineEdit, "lineEdit")
        le2 = self.findChild(QLineEdit, "lineEdit_2")
        le3 = self.findChild(QLineEdit, "lineEdit_3")
        
        self.__room_name = le1
        self.__target_temp = le2
        self.__target_hm = le3        
    
    def get_name(self):
        return self.__room_name.text()
    
    def get_target_temp(self):
        return self.__target_temp.text()
    
    def get_target_hm(self):
        return self.__target_hm.text()
    
    def get_room_no(self):
        return self.__room_no.text()
        
               
                
                
class DlgRoomDataInputHandler(DlgRoomDataInput):
    def __init__(self, room_name, target_temp, target_hm):
        super().__init__(room_name, target_temp, target_hm)

        
        
        
        
    def create_room_object(self):
        
        
        name = DlgRoomDataInput.get_name()
        target_temp = DlgRoomDataInput.get_target_temp()
        target_hm = DlgRoomDataInput.get_target_hm()
        number = DlgRoomDataInput.get_room_no()
        
        print(name, target_temp, target_hm, number)
        
        room = DlgRoomDataInput(self, name, target_temp, target_hm, number)
        print(room)
        
        return room

