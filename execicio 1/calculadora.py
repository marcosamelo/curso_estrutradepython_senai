#Faça uma calculadora que:

#-	Peça dois números ao usuário
#-	Peça qual operação deseja (+, -, *, /, %)
#-	Use match case para escolher a operação
#-	Exiba o resultado
#-	Trate o caso de divisão por zero
#-	Para operações inválidas, exiba mensagem de erro

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /, %): ")  

match operacao:
    case "+":
        resultado = num1 + num2
        print(f"O resultado de {num1} + {num2} é: {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"O resultado de {num1} - {num2} é: {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"O resultado de {num1} * {num2} é: {resultado}")
    case "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado de {num1} / {num2} é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    case "%":
        if num2 != 0:
            resultado = num1 % num2
            print(f"O resultado de {num1} % {num2} é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    case _:
        print("Erro: Operação inválida.")       




