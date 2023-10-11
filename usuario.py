class Usuario:
    def __init__(self, nombre, balance):
        self.nombre = nombre
        self.balance = balance

    def hacer_deposito(self, deposito):
        self.balance += deposito

    def hacer_retiro(self, retiro):
        self.balance -= retiro

    def hacer_transferencia(self, transferencia,abc):
        self.balance -= transferencia
        for persona in lista_usuarios:
            if persona == abc:
                abc.balance += transferencia

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}")
        print(f"Balance: {self.balance}")


usuario1 = Usuario("Chris", 500)
usuario2 = Usuario("Yanh", 1000)
usuario3 = Usuario("Camila", 20000)
lista_usuarios = [usuario1, usuario2, usuario3] 


print("------------------------------")

usuario1.mostrar_balance_usuario()
print("Se reciben Depositos...")
usuario1.hacer_deposito(10000)
usuario1.hacer_deposito(20000)
usuario1.hacer_deposito(30000)
usuario1.mostrar_balance_usuario()
print("Se ralizan Giros...")
usuario1.hacer_retiro(30000)
usuario1.mostrar_balance_usuario()

print("------------------------------")

usuario2.mostrar_balance_usuario()
print("Se reciben Depositos...")
usuario2.hacer_deposito(50000)
usuario2.hacer_deposito(50000)
usuario2.mostrar_balance_usuario()
print("Se ralizan Giros...")
usuario2.hacer_retiro(20000)
usuario2.hacer_retiro(20000)
usuario2.mostrar_balance_usuario()

print("------------------------------")

usuario3.mostrar_balance_usuario()
print("Se reciben Depositos...")
usuario3.hacer_deposito(50000)
usuario3.mostrar_balance_usuario()
print("Se ralizan Giros...")
usuario3.hacer_retiro(20000)
usuario3.hacer_retiro(500)
usuario3.hacer_retiro(15000)
usuario3.mostrar_balance_usuario()

print("------------------------------")
print("Transferencia")
print("------------------------------")
usuario1.mostrar_balance_usuario()
usuario3.mostrar_balance_usuario()
print("Se realiza transferencia...")
usuario1.hacer_transferencia(500, usuario3)
usuario1.mostrar_balance_usuario()
usuario3.mostrar_balance_usuario()