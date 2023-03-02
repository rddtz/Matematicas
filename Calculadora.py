def transformarEmNum(item):
    try:
        item = eval(item)
        return item
    except:
        return item

def calcular(valorDef):
    if lista[n] == '-':
        valorDef -= lista[n + 1]
    if lista[n] == '+':
        valorDef += lista[n + 1]
    if lista[n] == '/':
        valorDef /= lista[n + 1]
    if lista[n] == 'x':
        valorDef *= lista[n + 1]
    else:
        if valorDef == 0 and n == 0:
            valorDef += lista[n]
        else:
            pass
    return valorDef

def localdaPrioridadeVez():
    for n in range(tamanhoLista):
        if lista[n] == 'x':
            return n


def localdaPrioridadeDiv():
    for n in range(tamanhoLista):
        if lista[n] == '/':
            return n

def deletarDaLista(local):
    contador = 0
    while True:
        del lista[local - 1]
        contador += 1
        if contador == 3:
            break

def prioridadeVezes():
    local = localdaPrioridadeVez()
    resultado = lista[local - 1]*lista[local + 1]
    deletarDaLista(local)
    lista.insert(local - 1, resultado)

def prioridadeDivisao():
    local = localdaPrioridadeDiv()
    resultado = lista[local - 1]/lista[local + 1]
    deletarDaLista(local)
    lista.insert(local - 1, resultado)

def arrumarZeroFlutuante(valor):
    valorInt = int(valor)
    vDez = valor * 10
    vIntDez = valorInt * 10

    if vDez == vIntDez:
        return valorInt
    else:
        return valor
#---------------------------------
lista = input('Digite Números: ')
lista = lista.split(' ')
lista = list(filter(lambda item: item != '', lista))
lista = list(map(transformarEmNum, lista))
soPraManter = lista

total = 0
tamanhoLista = len(lista)

#Ve se há multiplicação ou divisão, se houver, chama a função para dar prioridade
contadorDeOperacoes = 0
analiseSeJaFezTudo = list(filter(lambda item: item == 'x' or item == '/', lista))
while True:
    for n in lista:
        if n == 'x':
            prioridadeVezes()
            tamanhoLista = len(lista)
            contadorDeOperacoes += 1
        elif n == '/':
            prioridadeDivisao()
            tamanhoLista = len(lista)
            contadorDeOperacoes += 1

    if len(analiseSeJaFezTudo) == contadorDeOperacoes:
        break
    else:
        pass

for n in range(tamanhoLista):
    total = calcular(total)

total = arrumarZeroFlutuante(total)
print(f'O resultado é {total}')
