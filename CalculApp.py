#Pelo que vi a maioria das GUIs de calculadora fazem uma operação por vez, vou tentar usar a calculadora que fiz no terminal
#como base, utilizando a GUI pra recebr os dados e mostrar eles, também recebendo dados escritos alem dos botões.

#Ta funcionando lindão, só formatar!

from tkinter import *
from Calculadora import calculadora

def chamarCalculadora():
    global valor
    resultado = calculadora(valor)
    valor = str(resultado)
    print(f'Valor = {valor} | Resultado = {resultado}')
    mostrar.set(valor)

def adicionarValor(qual):
    global valor
    if qual == '0': valor += '0'
    if qual == '1': valor += '1'
    if qual == '2': valor += '2'
    if qual == '3': valor += '3'
    if qual == '4': valor += '4'
    if qual == '5': valor += '5'
    if qual == '6': valor += '6'
    if qual == '7': valor += '7'
    if qual == '8': valor += '8'
    if qual == '9': valor += '9'
    if qual == '+': valor += ' + '
    if qual == '-': valor += ' - '
    if qual == 'x': valor += ' x '
    if qual == '/': valor += ' / '
    if qual == '.': valor += '.'
    if qual == 'del': valor = valor[:-1]
    if qual == 'limpa': valor = ''
    mostrar.set(valor)
    print(valor)

calculapp = Tk()
calculapp.title('Calculadora?')

mostrar = StringVar()
valor = ''

label = Label(textvariable=mostrar, font= ('Times New Roman', 25))
label.grid(column=0, row=0, columnspan=4)


botao0 = Button(width=5, height=3, text='0', command= lambda: adicionarValor('0'))
botao0.grid(column=1, row= 4)

botao1 = Button(width=5, height=3, text='1', command= lambda: adicionarValor('1'))
botao1.grid(column=0, row= 1)

botao2 = Button(text='2', width=5, height=3, command= lambda: adicionarValor('2'))
botao2.grid(column=1, row= 1)

botao3 = Button(width=5, height=3, text='3', command= lambda: adicionarValor('3'))
botao3.grid(column=2, row= 1)

botao4 = Button(width=5, height=3, text='4', command= lambda: adicionarValor('4'))
botao4.grid(column=0, row= 2)

botao5 = Button(width=5, height=3, text='5', command= lambda: adicionarValor('5'))
botao5.grid(column=1, row= 2)

botao6 = Button(width=5, height=3, text='6', command= lambda: adicionarValor('6'))
botao6.grid(column=2, row= 2)

botao7 = Button(width=5, height=3, text='7', command= lambda: adicionarValor('7'))
botao7.grid(column=0, row= 3)

botao8 = Button(width=5, height=3, text='8', command= lambda: adicionarValor('8'))
botao8.grid(column=1, row= 3)

botao9 = Button(width=5, height=3, text='9', command= lambda: adicionarValor('9'))
botao9.grid(column=2, row= 3)

botaoPonto = Button(width=5, height=3, text='.', command= lambda: adicionarValor('.'))
botaoPonto.grid(column=0, row= 4)

botaoMais = Button(width=5, height=3, text='+', command= lambda: adicionarValor('+'))
botaoMais.grid(column=3, row= 1)

botaoMenos = Button(width=5, height=3, text='-', command= lambda: adicionarValor('-'))
botaoMenos.grid(column=3, row= 2)

botaoVezes = Button(width=5, height=3, text='x',  command= lambda: adicionarValor('x'))
botaoVezes.grid(column=3, row= 3)

botaoDividir = Button(width=5, height=3, text='/', command= lambda: adicionarValor('/'))
botaoDividir.grid(column=3, row= 4)

botaoDel = Button(width=5, height=3, text='DEL', command= lambda: adicionarValor('del'))
botaoDel.grid(column= 0, row= 5)

botaoLimpar = Button(width=5, height=3, text='Limpar', command= lambda: adicionarValor('limpa'))
botaoLimpar.grid(column=2, row= 4)

botaoComeçar = Button(width=18, height=3, text='=', command= chamarCalculadora)
botaoComeçar.grid(column=1, row=5, columnspan=3)


calculapp.mainloop()