# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
test = 0
def fibonacci(n, num = 2):
    n1 = 0
    n2 = 1
    n3 = n1 + n2
    print(n1, n2, end=' ')
    for i in range(1, n):
        if(num != 2):
            global test
            if num == 0:
                test = 1
            elif num == n3:
                test = 1

        print(n3, end=" ")
        n1 = n2
        n2 = n3
        n3 = n1 + n2

len = int(input("Informe o tamanho da sequencia de fibonacci: "))
num = int(input("Informe o número que você deseja verificar se existe na sequencia de fibonacci: "))

fibonacci(len, num)

print(end="\n")
if test != 0:
    print('Esse número faz parte da sequencia de fibonacci')
else:
    print('Esse número não faz parte da sequencia de fibonacci')

test = 0
