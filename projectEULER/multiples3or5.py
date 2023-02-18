https://projecteuler.net/problem=1

'''para resolver esse problema, devemos:

#1: definir uma variável para receber o resultado

#2: um loop no intervalo (1000) em que o programa irá atuar

#3: adicionar as respostas do programa à variável criada no #1

'''
total = 0 #variável

for i in range(1,1000): #loop 'for in' que atua no intervalo definido

    if i % 3 == 0 or i % 5 == 0: #para ser múltiplo, o resto da sua divisão pelo número deve ser zero
        total+=i #soma à variável vazia a cada loop em que a condição é satisfeita

print(total)
#perceba que o print da soma final deve ser realizado fora do loop, para que apenas o último resultado seja impresso.
