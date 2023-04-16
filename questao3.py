# a 
def primos():
    cont=0
    print('A = 0 1', end=' ')
    for i in range(1, 50):
        cont = 0
        for j in range(1, i+1):
            if(i % j == 0):
                cont = cont + 1
        if(cont == 2):
            print(i, end=" ")       

primos()
print(end='\n')

# b
def dobrar():
    print('B =', end=" ")
    for i in range(1, 10):
        test = 2
        print(test**i, end=" ")

dobrar()

print(end='\n')

# c 
def quadradoPerfeito():
    print('C =', end=" ")
    for i in range(1, 11):
        print(i*i, end=' ')

quadradoPerfeito()
print(end='\n')

# d
def quadradoPar():
    print('D =', end=" ")
    for i in range(2, 21, 2):
        print(i**2, end=' ')

quadradoPar()
print(end='\n')

# e
def fibonacci():
    n1 = 0
    n2 = 1
    n3 = n1 + n2
    print('E = 0 1', end=' ')
    for i in range(1, 21):
        print(n3, end=" ")
        n1 = n2
        n2 = n3
        n3 = n1 + n2

fibonacci()