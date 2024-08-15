# Estudos em Python

## 1. Sintaxe em Python
Python é conhecido por sua sintaxe simples e legível. Vamos explorar alguns conceitos básicos:
Exemplo de "Hello, World!":

```python
print("Hello, World!")
```

Este é o programa mais simples em Python, que imprime a mensagem "Hello, World!" na tela.

Observe que o Python não requer ponto e vírgula no final das linhas e que a indentação é fundamental para definir blocos de código.

- Indentação:
Em Python, a indentação não é apenas uma questão de estilo; ela define a estrutura do código. Todos os blocos de código, como loops e condicionais, devem ser indentados de maneira consistente.
- Comentários:
Comentários de linha única são feitos com o símbolo `#`.
Comentários de múltiplas linhas podem ser feitos com três aspas `'''`.

## 2. Variáveis, Tipos de Dados e Operadores
```python
x = 10      	# Inteiro  
y = 3.14    	# Float  
nome = "Alice"  # String  
ativo = True	# Booleano  
```

## 3. Estruturas Condicionais (if, elif, else)
```python
idade = 20 # int(input("Insira a sua idade: "))
if idade >= 18:
	print("Você é maior de idade.")
elif idade < 18 and idade > 12:
	print("Você é adolescente.")
else:
	print("Você é criança.")
```

## 4. Estruturas de Repetição (for, while)
`for`
```python
for i in range(5):
	print(i)
```

`While`
```python
contador = 0
while contador < 5:
	print(contador)
	contador += 1
```	

## 5. Introdução a Funções e Sub-rotinas

def saudacao(nome):
	print(f"Olá, {nome}!")
	
saudacao("João")
```

# 6. Comentários e Documentação Básica de Código
# 6.1 Comentários de Linha Única:

# Esta função calcula a soma de dois números
def soma(a, b):
	return a + b

# 6.2 Docstrings:
def soma(a, b):
	"""
	Retorna a soma de dois números.

	Argumentos:
	a -- o primeiro número
	b -- o segundo número
	"""
	return a + b

# 7. Definição de Classes e Objetos
class Carro:
	def __init__(self, marca, modelo, ano):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano

	def acelerar(self):
		print(f"O {self.modelo} está acelerando.")

	def frear(self):
		print(f"O {self.modelo} está freando.")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)
print(vars(meu_carro))
meu_carro.acelerar()  # Saída: O Corolla está acelerando.

# 7.1 Instâncias, Atributos e Métodos
# Instância: Quando criamos um objeto a partir de uma classe, estamos criando uma instância dessa classe. 
# Por exemplo, meu_carro é uma instância da classe Carro.

# Atributos: São variáveis que pertencem a uma classe e descrevem as propriedades do objeto. 
# No exemplo acima, marca, modelo, e ano são atributos da classe Carro.

# Métodos: São funções que pertencem a uma classe e definem os comportamentos dos objetos. 
# No exemplo, acelerar e frear são métodos da classe Carro.

# 8. Encapsulamento

# Público (Public): 
# Atributos e métodos que podem ser acessados de qualquer lugar. Em Python, eles são definidos sem nenhum caractere especial no início do nome.
class Carro:
	def __init__(self, marca):
		self.marca = marca  # Atributo público

# Protegido (Protected): 
# Atributos e métodos que devem ser acessados apenas dentro da classe e por subclasses. Em Python, usa-se um underscore (_) antes do nome.
class Carro:
	def __init__(self, marca):
		self._marca = marca  # Atributo protegido

# Privado (Private): 
# Atributos e métodos que só podem ser acessados dentro da própria classe. Em Python, usa-se dois underscores (__) antes do nome.
class Carro:
	def __init__(self, marca):
		self.__marca = marca  # Atributo privado

 # 9.Métodos Getter e Setter
# Os métodos getter e setter são usados para acessar e modificar atributos privados de uma classe, respeitando o princípio do encapsulamento.

# Getter: Método que retorna o valor de um atributo privado.
class Carro:
	def __init__(self, marca):
		self.__marca = marca

	def get_marca(self):
		return self.__marca


# Setter: Método que altera o valor de um atributo privado.
class Carro:
	def __init__(self, marca):
		self.__marca = marca

	def set_marca(self, marca):
		self.__marca = marca

# 10 Criação de uma Classe Simples e Manipulação de Objetos
# Vamos criar uma calculadora simples usando o paradigma da orientação a objetos.

# Exemplo: Classe Calculadora
class Calculadora:
	def __init__(self):
    	self._resultado = 0

	def somar(self, valor):
    	self._resultado += valor

	def subtrair(self, valor):
    	self._resultado -= valor

	def multiplicar(self, valor):
    	self._resultado *= valor

	def dividir(self, valor):
    	if valor != 0:
        	self._resultado /= valor
    	else:
        	print("Erro: Divisão por zero não é permitida.")

	def get_resultado(self):
    	return self._resultado

	def reset(self):
    	self._resultado = 0



