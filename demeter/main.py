class Funcionario:
    def __init__(self, salario):
        self.salario = salario

class Departamento:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

class Empresa:
    def __init__(self):
        self.departamentos = []

    def adicionar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def calcular_soma_salarios(self):
        soma_salarios = 0
        for departamento in self.departamentos:
            for funcionario in departamento.funcionarios:
                soma_salarios += funcionario.salario
        return soma_salarios
