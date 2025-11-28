# Sistema simples de cadastro de produtos com nome e preço

produtos = {}

print("Cadastro de Produtos - Digite 'sair' para encerrar.")

while True:
    nome = input("Nome do produto: ").strip()
    if nome.lower() == 'sair':
        break
    try:
        preco = float(input("Preço do produto: R$ "))
        produtos[nome] = preco
        print(f"Produto '{nome}' cadastrado com sucesso!\n")
    except ValueError:
        print("Preço inválido. Tente novamente.\n")

print("\n--- Produtos Cadastrados ---")
for nome, preco in produtos.items():
    print(f"{nome}: R$ {preco:.2f}")

print(f"\nTotal de produtos: {len(produtos)}")