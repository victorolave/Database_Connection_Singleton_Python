from DBConnection import DBConnection

Employes = "Employes"
Nomina = "Nomina"

conn = DBConnection.getInstance()
conn.Connect(Employes)
conn.Disconnect()

conn = DBConnection.getInstance()
conn.Connect(Nomina)
conn.Disconnect()