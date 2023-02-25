#Código para receber números e remover os espaços
def apagasinal():
    global total
    global valor
    global tamanhoL
    if lista[0] == '+':
        lista.remove('+')
        tamanhoL = len(lista)
        valor = decimais(valor)
        total += valor
        tamanhoL = len(lista)
    elif lista[0] == '-':
        lista.remove('-')
        tamanhoL = len(lista)
        valor = decimais(valor)
        total -= valor
        tamanhoL = len(lista)
    elif lista[0] == 'x':
        lista.remove('x')
        tamanhoL = len(lista)
        valor = decimais(valor)
        total *= valor
        tamanhoL = len(lista)
    elif lista[0] == '/':
        lista.remove('/')
        tamanhoL = len(lista)
        valor = decimais(valor)
        total /= valor
        tamanhoL = len(lista)
    else:
        valor = decimais(valor)
        total += valor
        tamanhoL = len(lista)
#Função pra definir as dezenas, centenas e unidades
def decimais(num):
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

lista = list(input('Digite os números para somar: '))
tamanhoL = len(lista)
apagar = 0

#Apagar espaços
for n in range(tamanhoL - 1):
    if lista[n] == ' ':
        apagar += 1
for n in range(apagar):
        lista.remove(' ')

#variaveis para o while
tamanhoL = len(lista)
total = 0
valor = 0
l = 0

#aqui o calculo é feito, utilizando while e if para descobrir como sera construida a conta para o computador
while l != tamanhoL or l < tamanhoL:
    if lista[l] == 'X':
        lista[l] = 'x'
    if tamanhoL == 0:
        break
    #chama para fazer as contar
    apagasinal()
    #---------------------
    if l == tamanhoL or tamanhoL == 0:
        break

print(f"A soma equivale a:", total)