class CalculadoraArea:
    def calcular_area(self, forma, *args):
        if forma == "quadrado":
            lado = args[0]
            return lado * lado
        elif forma == "circulo":
            raio = args[0]
            return 3.14 * raio * raio
