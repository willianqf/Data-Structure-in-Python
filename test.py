
valorInicial = 6960
valor = valorInicial
juros = 0.0690
meses = 37

##
# R$480,24
##
somaJuros = 0
cont = 0
while(cont < meses):
    #valor = valor + (valor * juros)

    valor = valor + (valorInicial * juros)
    cont = cont + 1

JurosFinal = ((valor - valorInicial)/valorInicial)*100
print('Valor final será: R$'+str(round(valor, 2)))
print('Juros pelo emprestimo: '+str(round(JurosFinal, 2))+'%');
print('Você pagará esse valor a mais: R$'+str(round((valor - valorInicial), 2)))
print('Valor de sua parcela será: R$'+str(round(valor/meses, 2)))