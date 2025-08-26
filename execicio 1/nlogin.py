#Crie um sistema simples de login que:

#-	Tenha um usuário e senha pré-definidos
#-	Peça ao usuário para inserir login e senha
#	Verifique se estão corretos
#-	Se correto: exiba "Bem-vindo!"
#-	Se usuário errado: "Usuário não encontrado"
#-	Se senha errada: "Senha incorreta"
#-	Se ambos errados: "Usuário e senha incorretos"





nome = "MarcosMelo"
senha = "1965"
usuario = input("Digite seu nome de usuario: ")
senha_digitada = input("Digite sua senha: ")   
if usuario == nome and senha_digitada == senha:
    print("Bem-vindo!")
elif usuario != nome and senha_digitada == senha:
    print("Usuário não encontrado")
elif usuario == nome and senha_digitada != senha:
    print("Senha incorreta")
else:
    print("Usuário e senha incorretos")