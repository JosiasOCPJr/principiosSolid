class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def ligar(self):
        print(f"Motor {self.tipo} ligado.")

    def desligar(self):
        print(f"Motor {self.tipo} desligado.")

class Carro:
    def __init__(self, tipo_motor, modelo):
        self.motor = Motor(tipo_motor)
        self.modelo = modelo

    def ligar(self):
        self.motor.ligar()
        print(f"Carro modelo {self.modelo} ligado.")

    def desligar(self):
        self.motor.desligar()
        print(f"Carro modelo {self.modelo} desligado.")
