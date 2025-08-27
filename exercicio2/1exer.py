#peça ao usuário para inserir 4 notas de um aluno

lista =  []

for nota in range (4):
    lista.append(float(input("digite uma nota do aluno")))
soma = sum(lista)
media=soma/4
print(f"media das notas:{media}")

lista.sort()
print (lista[-1])
print (lista[0])
qnt = 0
for nota in lista:
  if nota >= media:
    qnt =+ 1
print(qnt)
