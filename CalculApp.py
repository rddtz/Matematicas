from tkinter import *
from Calculadora import calculadora

def chamarCalculadora():
    global valor
    global segurar
    global contador
    global fonte
    resultado = calculadora(valor)
    segurar = valor + ':'
    valor = str(resultado)
    if len(valor) > 10 and len(valor) < 20:
        fonte = 15
    elif len(valor) > 20:
        fonte = 10
    else:
        fonte = 25
    if len(segurar) > 10:
        label1.config(font=('Times New Roman', 8))
    else:
        label1.config(font=('Times New Roman', 12))
    label2.config(font=('Times New Roman', fonte))
    mostrarConta.set(segurar)
    mostrarResultado.set(valor)


def adicionarValor(qual):
    global valor
    global fonte
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
    if qual == 'limpa':
        valor = ''
        fonte = 25
        label2.config(font= ('Times New Roman', fonte))
    if qual == '(': valor += ' ( '
    if qual == ')': valor += ' ) '
    if qual == '^': valor += ' ^ '
    if qual == '√': valor += ' √ '
    mostrarResultado.set(valor)
    if len(valor) > 10 and fonte > 0:
        fonte -= 1
        label2.config(font= ('Times New Roman', fonte))
    print(fonte)
    print(valor)

calculapp = Tk()
calculapp.title('Calculadora!')
calculapp.resizable(width=0, height=0)

fonte = 25
mostrarResultado = StringVar()
valor = ''
segurar = ''
mostrarConta = StringVar()

label1 = Label(textvariable=mostrarConta, font= ('Times New Roman', 12), wraplength=240)
label1.grid(column=0, row=0, columnspan=4, sticky='w')


label2 = Label(textvariable=mostrarResultado, font= ('Times New Roman', fonte))
label2.grid(column=0, row=2, columnspan=4, sticky='e')


botao0 = Button(width=7, height=3, text='0', command= lambda: adicionarValor('0'))
botao0.grid(column=1, row= 6)

botao1 = Button(width=7, height=3, text='1', command= lambda: adicionarValor('1'))
botao1.grid(column=0, row= 3)

botao2 = Button(text='2', width=7, height=3, command= lambda: adicionarValor('2'))
botao2.grid(column=1, row= 3)

botao3 = Button(width=7, height=3, text='3', command= lambda: adicionarValor('3'))
botao3.grid(column=2, row= 3)

botao4 = Button(width=7, height=3, text='4', command= lambda: adicionarValor('4'))
botao4.grid(column=0, row= 4)

botao5 = Button(width=7, height=3, text='5', command= lambda: adicionarValor('5'))
botao5.grid(column=1, row= 4)

botao6 = Button(width=7, height=3, text='6', command= lambda: adicionarValor('6'))
botao6.grid(column=2, row= 4)

botao7 = Button(width=7, height=3, text='7', command= lambda: adicionarValor('7'))
botao7.grid(column=0, row= 5)

botao8 = Button(width=7, height=3, text='8', command= lambda: adicionarValor('8'))
botao8.grid(column=1, row= 5)

botao9 = Button(width=7, height=3, text='9', command= lambda: adicionarValor('9'))
botao9.grid(column=2, row= 5)

botaoPonto = Button(width=7, height=3, text='.', command= lambda: adicionarValor('.'))
botaoPonto.grid(column=0, row= 6)

botaoMais = Button(width=7, height=3, text='+', command= lambda: adicionarValor('+'))
botaoMais.grid(column=3, row= 3)

botaoMenos = Button(width=7, height=3, text='-', command= lambda: adicionarValor('-'))
botaoMenos.grid(column=3, row= 4)

botaoVezes = Button(width=7, height=3, text='x',  command= lambda: adicionarValor('x'))
botaoVezes.grid(column=3, row= 5)

botaoDividir = Button(width=7, height=3, text='/', command= lambda: adicionarValor('/'))
botaoDividir.grid(column=3, row= 6)

botaoPoten = Button(width=7, height=3, text='^', command= lambda: adicionarValor('^'))
botaoPoten.grid(column=3, row= 7)

botaoRaiz = Button(width=7, height=3, text='√', command= lambda: adicionarValor('√'))
botaoRaiz.grid(column=2, row= 7)

botaoDel = Button(width=7, height=3, text='DEL', command= lambda: adicionarValor('del'))
botaoDel.grid(column=2, row= 6)

botaoLimpar = Button(width=7, height=3, text='Limpar', command= lambda: adicionarValor('limpa'))
botaoLimpar.grid(column= 0, row= 8)

botaoParInic = Button(width=7, height=3, text='(', command= lambda: adicionarValor('('))
botaoParInic.grid(column=0, row= 7)

botaoParFim = Button(width=7, height=3, text=')', command= lambda: adicionarValor(')'))
botaoParFim.grid(column=1, row= 7)

botaoComeçar = Button(width=24, height=3, text='=', command= chamarCalculadora)
botaoComeçar.grid(column=1, row=8, columnspan=3,)


calculapp.mainloop()