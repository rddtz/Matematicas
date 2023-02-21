print('Digite a função conforme o exemplo (com os espaços) -> 2x2 + 3x + 9')
conta = list(input('Digite a função de segundo grau: '))

tamanho = len(conta)
a = 0
b = 1
c = 0

#IFs para descobrir os valores.

#Pegar valor A
if conta[0] == 'x':
    a = 1
else:
    a = eval(conta[0])

#Pegar valor B
for n in range(3, 8):
    if conta[n] == '-':
        for m in range(5, 8):
            if conta[m] != ' ' and conta[m] != 'x' and conta[m] != '+' and conta[m] != '-':
                b = eval(conta[m])
                b -= b * 2
    elif conta[n] == '+':
        for m in range(5, 8):
            if conta[m] != ' ' and conta[m] != 'x' and conta[m] != '+' and conta[m] != '-':
                b = eval(conta[m])

#Pegar valor C (FOR usado para descobrir o sinal)
if len(conta) < 8:
    c = 0
else:
    for n in range(8, tamanho):
        if conta[n] == '-':
            for m in range(8, tamanho):
                if conta[m] != ' ' and conta[m] != 'x' and conta[m] != '+' and conta[m] != '-':
                    c = eval(conta[m])
                    c -= c * 2
        elif conta[n] == '+':
            for m in range(8, tamanho):
                if conta[m] != ' ' and conta[m] != 'x' and conta[m] != '+' and conta[m] != '-':
                    c = eval(conta[m])

print('Resultados:')

#Calcúlo do Delta
delta = (b*b-(4*a*c))**0.5

if type(delta) != complex:
    if delta > 0:
        Xpos = (-(b) + delta) / (2*a)
        print('X´ = ', Xpos)
#Calcúlo das raizes, em cima com + raiz e em baixo - raiz
        Xneg = (-(b) - delta) / (2*a)
        print('X´´ = ', Xneg)
else:
    print('Como delta é menor que zero, a equação não terá raízes reais, pois não existe raiz quadrada de número negativo.')
