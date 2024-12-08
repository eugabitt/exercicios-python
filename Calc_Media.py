
notas = list() # guardando as notas em lista
loop_exit = False 

# enquanto o usuário não sair do loop teclando X, será solicitado as notas
while not loop_exit: 
    teste = input("Digite a nota ou aperte X para sair: ")
    if teste == 'x' or teste == 'X':
        loop_exit = True
        break # para se digitado X
    notas.append(float(teste))

# função para calcular a média
def calcular_media(notas_calc):
    total = sum(notas_calc)
    media_calc = total / len(notas_calc)
    return media_calc
    
# função lambda para arredondar a média 
arredondar_media = lambda media: round(media, 0) 

media = calcular_media(notas)
media_arredondada = arredondar_media(media)

# define a situação do aluno
if media_arredondada >= 7:
    situacao = "Aprovada(o)"
else:
    situacao = "Reprovada(o)"

# exibe relatório final 
for teste in notas:
    print("A nota do(a) aluno(a) é: ", teste)

print("A média do(a) aluno(a) é: ", media_arredondada)

print("O/a aluno(a) foi: ",situacao)