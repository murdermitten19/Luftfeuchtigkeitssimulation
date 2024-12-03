import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from funct_controller import *
from room import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("hum_sim.ui", self)
        
        
    def setup_buttons(self):
        btn_create_room = self.findChild(QPushButton, "btn_create_room")
        btn_create_room.clicked.connect(self.show_dialog)
        
        btn_exec_sim = self.findChild(QPushButton, "btn_exec_sim")
        btn_exec_sim.clicked.connect(self.execute_simulation)
        
        btn_show_sim_data = self.findChild(QPushButton, "btn_show_sim_data")
        btn_show_sim_data.clicked.connect(self.show_simulation_data)
    
    
    def setup_labels(self):
        lbl_rm_nr = self.findChild(QLabel, "lbl_rm_nr")
        lbl_rm_nr.hide()
        
        lbl_rm_nm = self.findChild(QLabel, "lbl_rm_nm")
        lbl_rm_nm.hide()
        
        lbl_tm_sh = self.findChild(QLabel, "lbl_tm_sh")
        lbl_tm_sh.hide()
        
        lbl_hm_sh = self.findChild(QLabel, "lbl_hm_sh")
        lbl_hm_sh.hide()
        
        lbl_tm_id = self.findChild(QLabel, "lbl_tm_id")
        lbl_tm_id.hide()
        
        lbl_hy_id = self.findChild(QLabel, "lbl_hy_id")
        lbl_hy_id.hide()
        
        lbl_rel_hm = self.findChild(QLabel, "lbl_rel_hm")
        lbl_rel_hm.hide()
        
        lbl_abs_hm = self.findChild(QLabel, "lbl_abs_hm")
        lbl_abs_hm.hide()
        
        lbl_time = self.findChild(QLabel, "lbl_time2")
        lbl_time.hide()
        
    
        
    def show_dialog(self):
        dialog = DlgRoomDataInput()
        dialog.exec_()

        
    def execute_simulation(self):
        print("Simulation executed")
    
    def show_simulation_data(self):
        print("Simulation data shown")
        
        
















