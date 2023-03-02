import sys

def transformarEmNum(item):
    try:
        item = eval(item)
        return item
    except:
        if '(' in item:
            listaAux = list(item)
            if listaAux[0] == '(':
                del listaAux[0]
            listaAux = ''.join(listaAux)
            item = transformarEmNum(listaAux)
            return item
        elif ')' in item:
            listaAux = list(item)
            final = len(listaAux) - 1
            if listaAux[final] == ')':
                del listaAux[final]
            listaAux = ''.join(listaAux)
            item = transformarEmNum(listaAux)
            return item
        else:
            return item

def calcular(parametro, valorDef, n):
    lista = parametro
    if lista[n] == '-':
        valorDef -= lista[n + 1]
    if lista[n] == '+':
        valorDef += lista[n + 1]
    if lista[n] == '/':
        try:
            valorDef /= lista[n + 1]
        except:
            print('É impossivel dividir um número por 0')
            sys.exit()
    if lista[n] == 'x':
        valorDef *= lista[n + 1]
    else:
        if valorDef == 0 and n == 0:
            valorDef += lista[n]
        else:
            pass
    return valorDef

def prioridadeParenteses():
    adicionarParentesesInic()
    adicionarParentesesFim()

def localdaPrioridadeParenteses():
    for n in range(len(lista)):
        try:
            if '(' in lista[n]:
                localInicio.append(n)
            if ')' in lista[n]:
                localFim.append(n)
        except:
            pass

def adicionarParentesesInic():
    contador = 0
    while True:
        lista.insert(localInicio[0], '(')
        del localInicio[0]
        if len(localInicio) == 0:
            break
        contador += 1
        localInicio[0] += contador

def adicionarParentesesFim():
    contador = 2
    while True:
        localFim[0] += contador
        lista.insert(localFim[0], ')')
        del localFim[0]
        if len(localFim) == 0:
            break
        contador += 2

def localDoFinalDoParenAtual():
    for n in range(len(lista)):
        if lista[n] == ')':
            return n

def calcularParenteses():
    contador = 0
    while True:
        if lista[contador] == '(':
            resultado = 0
            localF = localDoFinalDoParenAtual()
            totalDeVezes = localF - contador
            listaAux = []
            for loop in range(totalDeVezes):
                del lista[contador]
                listaAux.append(lista[contador])
            del listaAux[len(listaAux) - 1]
            del lista[contador]
            listaAux = calcularPrioridade(listaAux)
            for n in range(len(listaAux)):
                resultado = calcular(listaAux, resultado, n)
            lista.insert(contador, resultado)
            contador = 0
        contador += 1
        if TrOuFalseParaParent(lista) == True:
            pass
        else:
            break

def TrOuFalseParaParent(parametro):
    try:
        for i in parametro:
            if i == '(':
                return True
    except:
        pass

def localdaPrioridadeVez(parametro):
    for n in range(len(parametro)):
        if parametro[n] == 'x':
            return n

def localdaPrioridadeDiv(parametro):
    for n in range(len(parametro)):
        if parametro[n] == '/':
            return n

def deletarDaLista(parametro, local):
    contador = 0
    listaParaDeletar = parametro
    if listaParaDeletar[local] == 'x' or listaParaDeletar[local] == '/':
        while True:
            del listaParaDeletar[local - 1]
            contador += 1
            if contador == 3:
                break

def prioridadeVezes(parametro):
    listaPriovezes = parametro
    local = localdaPrioridadeVez(listaPriovezes)
    resultado = listaPriovezes[local - 1]*listaPriovezes[local + 1]
    deletarDaLista(listaPriovezes, local)
    listaPriovezes.insert(local - 1, resultado)
    return listaPriovezes

def prioridadeDivisao(parametro):
    listaPrioDiv = parametro
    local = localdaPrioridadeDiv(listaPrioDiv)
    try:
        resultado = listaPrioDiv[local - 1]/listaPrioDiv[local + 1]
    except:
        print('É impossivel dividir um número por 0')
        sys.exit()
    deletarDaLista(listaPrioDiv, local)
    listaPrioDiv.insert(local - 1, resultado)
    return listaPrioDiv

def calcularPrioridade(parametro):
    listaDePrioridade = parametro
    contadorDeOperacoes = 0
    analiseSeJaFezTudo = list(filter(lambda item: item == 'x' or item == '/', listaDePrioridade))
    global tamanhoLista
    while True:
        for n in listaDePrioridade:
            if n == 'x':
                listaDePrioridade = prioridadeVezes(listaDePrioridade)
                tamanhoLista = len(listaDePrioridade)
                contadorDeOperacoes += 1
                break
            if n == '/':
                listaDePrioridade = prioridadeDivisao(listaDePrioridade)
                tamanhoLista = len(listaDePrioridade)
                contadorDeOperacoes += 1
                break

        if len(analiseSeJaFezTudo) == contadorDeOperacoes:
            return listaDePrioridade
        else:
            pass

def arrumarZeroFlutuante(valor):
    valorInt = int(valor)
    vDez = valor * 10
    vIntDez = valorInt * 10

    if vDez == vIntDez:
        return valorInt
    else:
        return valor
#---------------------------------
localInicio = []
localFim = []
lista = input('Digite números: ')
lista = lista.split(' ')
lista = list(filter(lambda item: item != '', lista))
localdaPrioridadeParenteses()
lista = list(map(transformarEmNum, lista))
lista = list(filter(lambda item: item != '', lista))
soPraManter = lista

total = 0
tamanhoLista = len(lista)
#ver se há parenteses
if len(localInicio) > 0 and len(localFim) > 0:
    prioridadeParenteses()
    calcularParenteses()

#Ve se há multiplicação ou divisão, se houver, chama a função para dar prioridade
lista = calcularPrioridade(lista)

for n in range(tamanhoLista):
    total = calcular(lista, total, n)

total = arrumarZeroFlutuante(total)
print(f'O resultado é {total}')
