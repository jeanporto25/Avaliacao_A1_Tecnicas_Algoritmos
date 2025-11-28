# Contador de números pares de 1 a 100 usando for e while

print("Números pares de 1 a 100 (usando FOR):")
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=" ")

print("\n\nNúmeros pares de 1 a 100 (usando WHILE):")
contador = 1
while contador <= 100:
    if contador % 2 == 0:
        print(contador, end=" ")
    contador += 1

print("\n\nFim da contagem!")