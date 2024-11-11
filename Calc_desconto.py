valor_produto = float(input("Digite o preço: "))
percentual_desconto = float(input("Agora, digite o desconto: "))
desconto = valor_produto * (percentual_desconto / 100)
valor_final = valor_produto - desconto

if percentual_desconto >= 0 and percentual_desconto <= 20:
    print("O preço com desconto é R$", valor_final)
else:
    print("Desconto máximo de 20%.")