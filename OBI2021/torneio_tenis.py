
#Solução por: Laryssa de Oliveira Ferreira - Engenharia de Computação - UnB

'Esse problema permite a aplicação de manipulação de listas, em um contexto de torneio de tênis'
'Devemos definir quem são os vencedores e perdedores, e em qual lista estarão'

i = 0 # cria contador
ganha = [] #lista vazia para ganhadores
perde = [] #lista vazia perdedores

for i in range(6): #loop para receber as 6 entradas
    resultado = input()
    i += 1 #adiciona no contador
    if resultado == 'V':
        ganha.append(resultado) #adiciona à lista vazia dos ganhadores
    else:
        perde.append(resultado)

qnt_ganha = len(ganha) #retorna o tamanho da lista
qnt_perde = len(perde)

if qnt_ganha == 5 or qnt_ganha == 6: #condições definidas no enunciado
    print('1')
elif qnt_ganha == 3 or qnt_ganha == 4:
    print('2')
elif qnt_ganha == 1 or qnt_ganha == 2:
    print('3')
else: #não colocado em nenhum dos três
    print('-1')
