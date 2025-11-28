# Programa que recebe nomes de alunos e armazena em lista

alunos = []

print("Cadastro de Alunos - Digite 'sair' para encerrar.")

while True:
    nome = input("Digite o nome do aluno: ").strip()
    if nome.lower() == 'sair':
        break
    alunos.append(nome)

print("\n--- Lista de Alunos Cadastrados ---")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}. {aluno}")

print(f"\nTotal de alunos cadastrados: {len(alunos)}")