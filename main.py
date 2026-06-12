def calcular_total_compra(produtos):
    total = 0

    for produto in produtos:
        nome = produto["nome"]
        quantidade = produto["quantidade"]
        preco = produto["preco"]

        if quantidade <= 0:
            print(f"Erro: a quantidade do produto '{nome}' deve ser maior que zero.")
            continue

        if preco < 0:
            print(f"Erro: o preço do produto '{nome}' não pode ser negativo.")
            continue

        total_item = quantidade * preco

        print(f"{nome}: R$ {total_item:.2f}")

        total += total_item

    return total


def aplicar_desconto(total):
    if total > 100:
        desconto = total * 0.10
        valor_final = total - desconto
        return desconto, valor_final

    return 0, total


def main():
    produtos = []

    quantidade_produtos = int(input("Quantos produtos deseja cadastrar? "))

    for i in range(quantidade_produtos):
        print(f"\nProduto {i + 1}")

        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço unitário: "))

        produto = {
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco
        }

        produtos.append(produto)

    total = calcular_total_compra(produtos)

    print(f"\nValor original da compra: R$ {total:.2f}")

    desconto, valor_final = aplicar_desconto(total)

    if desconto > 0:
        print(f"Desconto aplicado: R$ {desconto:.2f}")
        print(f"Valor final da compra: R$ {valor_final:.2f}")
    else:
        print(f"Valor total da compra: R$ {valor_final:.2f}")


if __name__ == "__main__":
    main()