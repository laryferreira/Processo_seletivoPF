'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.'''



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
