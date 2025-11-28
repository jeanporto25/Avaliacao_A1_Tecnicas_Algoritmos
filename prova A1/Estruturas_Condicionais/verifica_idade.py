# Programa que simula sistema de verificação de idade para entrada em eventos

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você não pode entrar. Menores de 18 anos não são permitidos.")
elif idade >= 18 and idade < 60:
    print("Bem-vindo ao evento!")
else:
    print("Entrada gratuita para idosos (60+ anos).")

print(f"Idade verificada: {idade} anos")