import sys

def transformarEmNum(item):
    '''Retorna os itens da lista convertidos para números caso for possível, se forem stringgs como + ou - ele
    apenas retorna a string, também caso ele ache parenteses ele apagara ele pra depois os parenteses serem readicionados,
    isso por que ao escrever (10 isso se torna uma string e é preciso separar o ( do dez, deletando o parenteses e rechamando a funçaõ'''

    try:
        item = eval(item)
        return item
    except:
        if '(' in item:
            listaAux = list(item)
            if listaAux[0] == '(':
                del listaAux[0]
            listaAux = ''.join(listaAux)
            item = transformarEmNum(listaAux) #Chama a funcção novamente depois de separar os parenteses
            return item
        elif ')' in item:
            listaAux = list(item)
            final = len(listaAux) - 1
            if listaAux[final] == ')':
                del listaAux[final]
            listaAux = ''.join(listaAux)
            item = transformarEmNum(listaAux) #Chama a função novamente depois de separar os parenteses
            return item
        else:
            return item

def calcular(parametro, valorDef, n):
    '''Calcula as contas normalmente baseado nas strings de sinalização (+, -, x ou /)'''
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
            valorDef += lista[n] #Caso seja o primeiro item e seja positivo
        else:
            pass
    return valorDef

def prioridadeParenteses():
    '''Chama as funções para adicionar novamente os parenteses, primerios os ( e depois os ), com base nos locais
    que foram salvos pela função localdaPrioridadeParenteses'''
    adicionarParentesesInic()
    adicionarParentesesFim()

def localdaPrioridadeParenteses():
    '''Salva o local dos parenteses na lista, para depois que forem removidos pela função transformarEmNum() possam ser
    adicionados novamente no lugar exato'''
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
    '''Isola e calcula os números que ficam entre os parenteses, depois apaga os parenteses e insere o resultado na lista no
    lugar onde se encontrava a conta do parenteses'''
    contador = 0
    while True:
        if lista[contador] == '(':
            resultado = 0
            localF = localDoFinalDoParenAtual() #Ve onde acaba o parenteses que esta sendo trabalhando pra pegar tudo dentro dele
            totalDeVezes = localF - contador
            listaAux = [] #lista pra isolar os números e calcula-los separados
            for loop in range(totalDeVezes):
                del lista[contador] #apagar a conta dentro do () da lista para adicionar o resultado no lugar
                listaAux.append(lista[contador])
            del listaAux[len(listaAux) - 1]
            del lista[contador]
            listaAux = calcularPrioridade(listaAux) #Caso haja prioridade de X ou / dentro dos parenteses irá ser feito aqui
            for n in range(len(listaAux)):
                resultado = calcular(listaAux, resultado, n) #Faz a conta normal com o que sobrou
            lista.insert(contador, resultado) #Adiciona o resultado na lista
            contador = 0 #Reseta o contador pra ele voltar do ínicio pois a lista mudou de tamanho
        contador += 1
        if TrOuFalseParaParent(lista) == True: #Ve se ainad há parenteses na conta, se não tiver vai acabar o loop
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
    deletarDaLista(listaPriovezes, local) #Deleta os itens da lista para adicionar o resultado no local
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
    deletarDaLista(listaPrioDiv, local) #Deleta os itens da lista para adicionar o resultado no local
    listaPrioDiv.insert(local - 1, resultado)
    return listaPrioDiv

def calcularPrioridade(parametro):
    '''Analisa a lista recebi pelo parametro, ve se há multiplicação ou divisão, caso tenha procura o local, faz o calculo dos
    números, apaga os originais e adiciona o resultado, similar ao o que acontece com os parenteses'''
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
                break #Esse break quebra o For, pra voltar a correr do início da lista sempre que uma operação for realizada
            if n == '/':
                listaDePrioridade = prioridadeDivisao(listaDePrioridade)
                tamanhoLista = len(listaDePrioridade)
                contadorDeOperacoes += 1
                break

        if len(analiseSeJaFezTudo) == contadorDeOperacoes: #ve se todas operações que recebem prioridade ja foram realizado
            return listaDePrioridade
        else:
            pass

def arrumarZeroFlutuante(valor):
    'Só pra transformar 5.0 em 5'
    valorInt = int(valor)
    vDez = valor * 10
    vIntDez = valorInt * 10

    if vDez == vIntDez:
        return valorInt
    else:
        return valor
#---------------------------------

#Início do programa

localInicio = [] #Variavel pra guardar o local dos parenteses '(', em geral tudo que tem inicio se refere a isso
localFim = [] #Mesma coisa que o inicio, mas para ')'

lista = input('Digite números: ') #Recebe a contaa
lista = lista.split(' ')
lista = list(filter(lambda item: item != '', lista)) #Remove os espaços
localdaPrioridadeParenteses()
lista = list(map(transformarEmNum, lista)) #Transforma os itens da lista em números inteiros/float se for possivel
lista = list(filter(lambda item: item != '', lista)) #Remove os espaços novamente, pra caso haja espaço entre os parenteses não tenha erro

total = 0
tamanhoLista = len(lista)

#ver se há parenteses na conta e já faz os calcúlos necessários
if len(localInicio) > 0 and len(localFim) > 0:
    prioridadeParenteses()
    calcularParenteses()

#Ve se há multiplicação ou divisão, se houver, chama a função para dar prioridade
lista = calcularPrioridade(lista)

for n in range(tamanhoLista):
    #calcula todos itens restantes da lista
    total = calcular(lista, total, n) #Total envia a ele mesmo coo parametro, por isso não reseta a cada chamada

total = arrumarZeroFlutuante(total)
print(f'O resultado é {total}')
