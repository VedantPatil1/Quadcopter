import sqlite3
from Components import Motor, Propeller


class Drone():
    def __init__(self,configId):
        self.configID = configId
        self.Motor = Motor("RC2216")
        
        

    
    
    