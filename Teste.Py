ano_nasc = int(input("Qual o ano que você nasceu?") )
ano_atual = int(input("Qual o ano atual?"))
menos = ano_atual - ano_nasc + 27
print("Você terá", menos, "anos no fim do mundo")   
if  menos > 30: 
    print("Você irá de base após o retorno de saturno. Yay!")
    if menos < 25:
        print("Você virará camisa da saudade com o lobo frontal não desenvolvido")
else:
 print("Você irá de Wakanda forever na horizontal sem nenhum marco importante na sua vida")