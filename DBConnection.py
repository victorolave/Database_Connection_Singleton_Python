class DBConnection:

    __instance = None
    
    @staticmethod 
    def getInstance():
       if DBConnection.__instance == None:
          DBConnection()
          print("Instancia Creada")
       return DBConnection.__instance

    def __init__(self):
       if DBConnection.__instance != None:
          raise Exception("This class is a singleton!")
       else:
          DBConnection.__instance = self

    def Connect(self, dbname):
        print("Connected with: " + dbname)

    def Disconnect(self):
        print("Disconnected")