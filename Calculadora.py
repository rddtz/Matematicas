#Tentar fazer um varredura completa na lista e criar um software que compreenda o que foi escrito
#Exemplo:
#Recebe -> 2x3 + 3 - 2
#Entende e transforma em -> 2*3 + 3 - 2
#Resolve e devolve -> 7

#Código para receber números e remover os espaços
lista = list(input('Digite números: '))
tamanhoL = len(lista)
apagar = 0

for n in range(tamanhoL - 1):
    if lista[n] == ' ':
        apagar += 1
for n in range(apagar):
        lista.remove(' ')

print(lista)