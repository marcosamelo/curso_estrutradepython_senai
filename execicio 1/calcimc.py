#-	Peça o peso e altura de uma pessoa
#-	Calcule o IMC (peso / altura²)
#-	Classifique o resultado:
#-	Abaixo de 18.5: Abaixo do peso
#-	18.5 a 24.9: Peso normal
#-	25.0 a 29.9: Sobrepeso
#-	30.0 ou mais: Obeso


peso=float(input("Digite seu peso em kg: "))
altura=float(input("Digite sua altura em metros: "))        
imc=peso/(altura**2)
print("Seu IMC é: {:.2f}".format(imc))
if imc < 18.5: 
    print("Abaixo do peso")
elif imc>=18.6 and imc <= 24.9:
    print("Peso normal")
elif imc >=25 and imc <=29.9:
    print("SOBREPESO")
else:
    print("OBESO")
#-	Calcule --- IGNORE ---94