palavra = input('Digite uma palavra: ')

reversa = ''

for i in range(len(palavra), 0, -1):
    reversa += palavra[i-1]

print(reversa)