class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def ligar(self):
        print(f"Motor {self.tipo} ligado.")

    def desligar(self):
        print(f"Motor {self.tipo} desligado.")

class Carro(Motor):
    def __init__(self, tipo, modelo):
        super().__init__(tipo)
        self.modelo = modelo

    def ligar(self):
        super().ligar()
        print(f"Carro modelo {self.modelo} ligado.")

    def desligar(self):
        super().desligar()
        print(f"Carro modelo {self.modelo} desligado.")
