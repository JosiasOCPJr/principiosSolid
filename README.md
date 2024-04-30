# Single Responsability

Toda classe deve ter uma única responsabilidade.
Nesse exemplo, a função além de estar realizando a soma, está exibindo o resultado. Podemos quebrar isso em duas funções, uma para realizar a soma e retornar para uma outra classe que exibirá o resultado.

# Demeter

Nesse exemplo, a classe Empresa acessa o salário dos funcionários diretamente, violando a Lei de Demeter. Para consertar isso, podemos redirecionar essa responsabilidade para os departamentos, evitando o acesso direto às informações de objetos que não são relacionados.

# Open-Closed Principle

Os métodos precisam estar abertos para extensão e fechados para modificação. Nesse exemplo, para adicionar uma nova forma, precisaremos modificar a classe, o que fere o princípio open-closed. Então, para consertar, cria-se uma classe generalizada Forma com o método calcular_area() que pode ser definido individualmente por cada forma específica.

# Prefira Composição a Herança

Quando possível, sempre dê preferência a composição do que herança. A herança representa que um objeto é outro, enquanto a composição indica que um possui o outro.
Nesse exemplo, o carro é um motor, ao invés de possuir um motor (implementado na solução).