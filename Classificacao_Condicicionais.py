filmes = ["Brilho eterna de uma mente sem lembranças", "Pitch Perfect", "La Vie D'Adele","Laranja Mecânica"]

 

print("Olá, seja bem-vindo à classificação.")

print("Você irá classificar os filmes de 1 a 5, sendo 1: Péssimo e 5: Muito bom.")

print("Aperte 0 a qualquer momento para sair.\n")

 

for filme in filmes:

    while True:

        classificacao = input(f"Como você classificaria '{filme}' de 1 a 5? (ou 0 para parar): ")

        if classificacao == '0':

            print("Ah! Que pena.")

            break  

        classificacao = int(classificacao)

        if classificacao < 1 or classificacao > 5:

            print("Por favor se atente aos parâmetros de classificação.")

        else:

            print(f"Você classificou '{filme}' com {classificacao} estrelas.\n")

            break 

 

print("Obrigada por participar! Até mais ver.")