"""
Ocorrências de um número:
Crie um programa que percorre a lista_numeros
e exiba quantas vezes cada número aparece na lista.
"""
lista = [5,1,2,3,3,4,3,2,5]

# comece aqui:
for i in lista:
    contador_ocorrencias = 0
    for x in lista:
        if i == x:
            contador_ocorrencias += 1
    print(f"O número {i} aparece {contador_ocorrencias} vezes na lista.")
