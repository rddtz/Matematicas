#Tentar fazer um varredura completa na lista e criar um software que compreenda o que foi escrito
#Exemplo:
#Recebe -> 2x3 + 3 - 2
#Entende e transforma em -> 2*3 + 3 - 2
#Resolve e devolve -> 7

#Código para receber números e remover os espaços
lista = list(input('Digite números: '))
tamanhoL = len(lista)
print(lista)
apagar = []

for n in range(tamanhoL - 1):
    if lista[n] == ' ':
        apagar.append(n)
        print(apagar)

tamanhoA = len(apagar)
correcao = 0

for m in range(tamanhoA):
        del lista[apagar[m] - correcao]
        correcao = correcao + 1

print(lista)