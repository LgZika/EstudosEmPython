def menu():
	print("Calculadora")
	print("Opera 2 numeros nas operações: +, -, *, /, %")
	num01 = int(input("Insira o primeiro número: "))
	num02 = int(input("Insira o segundo número: "))
	operation = input("Selecione a operação matemática: ")
	if(operation != "0"):
		print(float(doMath(operation, num01, num02)))
	else:
		return 0

def doMath(op, n01, n02):
	match op:
		case "+":
			return(n01 + n02)
		case "-":
			return(n01 - n02)
		case "/":
			return("n01 / n02")
		case "*":
			return(n01 * n02)
		case "%":
			return(n01 % n02)
		case _:
			return(0)

while(True):
	menu()
	if(menu() == 0):
		break