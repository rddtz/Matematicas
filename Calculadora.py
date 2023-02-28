import sys

def localEitem():
    global local
    global item
    local.clear()
    item.clear()
    for n in range(tamanhoL):
        if lista[n] == '+':
            local.append(n)
            item += lista[n]
        if lista[n] == '/':
            local.append(n)
            item += lista[n]
        if lista[n] == '-':
            local.append(n)
            item += lista[n]
        if lista[n] == 'x':
            local.append(n)
            item += lista[n]

def prioridade():
    'Analisa e procura se há divisão ou multiplicação para realizar primeiro'
    global tamanhoL
    global segurar
    global tamanhoSegurado
    global local
    global item

    localEitem()
    for n in item:
        if n == '/' or n == 'x':
            if tamanhoL > 0:
                if item[0] != '/' and item[0] != 'x':
                    if lista[local[0]] != '/' or lista[local[0]] != 'x':
                        while lista[local[0]] == item[0]:
                            segurar += lista[0]
                            del lista[0]
                            local[0] -= 1
                        del item[0]
                        del local[0]
                        tamanhoL = len(lista)
                        tamanhoSegurado = len(segurar)
                        localEitem()
                        tamItem = len(item)
                        if tamItem > 0:
                            while item[0] != '/' and item[0] != 'x':
                                    if lista[local[0]] != '/' or lista[local[0]] != 'x':
                                        while lista[local[0]] == item[0]:
                                            segurar += lista[0]
                                            del lista[0]
                                            local[0] -= 1
                                        del item[0]
                                        del local[0]
                                        tamanhoL = len(lista)
                                        tamanhoSegurado = len(segurar)
                                        localEitem()
    tamanhoL = len(lista)
    apagasinal() #fazer as contas
    tamanhoL = len(lista)
    tamanhoSegurado = len(segurar)
    tamanhoL = len(lista)

    if tamanhoL == 0 and tamanhoSegurado > 0:
        for i in range(tamanhoSegurado):
            lista.append(segurar[0])
            del segurar[0]

def apagasinal():
    'Analisa qual a operação realizada, remove o sinal da lista e chama a função para realizar a conta'

    global seguraVal
    global total
    global valor
    global tamanhoL
    if lista[0] == '+':
        lista.remove('+')
        tamanhoL = len(lista)
        if tamanhoL == 0:
            pass
        else:
            valor = decimais()
            total += valor
            tamanhoL = len(lista)
    elif lista[0] == '-':
        lista.remove('-')
        tamanhoL = len(lista)
        if tamanhoL == 0:
            pass
        else:
            valor = decimais()
            total -= valor
            tamanhoL = len(lista)
    elif lista[0] == 'x':
        lista.remove('x')
        tamanhoL = len(lista)
        if tamanhoL == 0:
            pass
        else:
            valor = decimais()
            if seguraVal > 0:
                seguraVal *= valor
                tamanhoL = len(lista)
            else:
                total *= valor
                tamanhoL = len(lista)
    elif lista[0] == '/':
        lista.remove('/')
        tamanhoL = len(lista)
        if tamanhoL == 0:
            pass
        else:
            valor = decimais()
            if seguraVal > 0:
                try:
                    seguraVal /= valor
                except ZeroDivisionError:
                    print('É impossível dividir por 0')
                    sys.exit()
                tamanhoL = len(lista)
            else:
                try:
                    total /= valor
                except ZeroDivisionError:
                    print('É impossível dividir por 0')
                    sys.exit()
                tamanhoL = len(lista)
    else:
        if tamanhoL > 1 and (lista[1] == 'x' or lista[1] == '/'):
            valor = decimais()
            seguraVal += valor
            tamanhoL = len(lista)
            apagasinal()
            if segurar[0] == '-':
                total -= seguraVal
            else:
                total += seguraVal
            seguraVal = 0
        else:
            valor = decimais()
            total += valor
            tamanhoL = len(lista)


def decimais():
    'Caso tenha números em sequencia na lista, transforemara em números inteiros maiores (1, 2, 5 vira 125)! Depois retorna o valor obtido para adicionar ao calcúlo.'

    num = 0
    LDef = 0
    dezena = 10
    times = 0
    C = LDef + 1
    Ctam = 0

    #ve quantos tem na sequencia | 1, 2, 3, '+' tem três números em sequencia
    if tamanhoL != 1:
        while lista[C] != '+' and lista[C] != '-' and lista[C] != 'x' and lista[C] != '/' and C < tamanhoL:
            Ctam += 1
            C += 1
            if C == tamanhoL or C > tamanhoL:
                break

    ordem = []

    #Transforma os números em sequencia em numeros completos / 1, 2, 3 vira 123
    while lista[LDef] != '+' and lista[LDef] != '-' and lista[LDef] != 'x' and lista[LDef] != '/' :
        ordem.append(eval(lista[Ctam - LDef]) * (dezena ** times))
        times += 1
        LDef += 1
        if LDef == tamanhoL or LDef > tamanhoL:
            break

    #faz os calculos e tira o numero da lista
    for n in range(times):
        del lista[0]
    TamOrdem = len(ordem)
    for n in range(TamOrdem):
        num += ordem[n]

    return num

#-------------------------------------------

lista = list(input('Digite a conta: '))
segurar = []
item = []
local = []
tamanhoL = len(lista)
tamanhoSegurado = len(segurar)
apagar = 0
seguraVal = 0

#Apagar espaços na lista
for n in range(tamanhoL - 1):
    if lista[n] == ' ':
        apagar += 1
for n in range(apagar):
        lista.remove(' ')


#variaveis para o while
tamanhoL = len(lista)
total = 0
valor = 0

#aqui o calculo é feito, utilizando while e if para descobrir como sera construida a conta para o computador
while True:
    prioridade() #chama para fazer as contar
    if tamanhoL == 0 and tamanhoSegurado == 0:
        break

print(f"O resultado é:", total)
