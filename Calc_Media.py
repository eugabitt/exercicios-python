notas = list()
loop_exit = False

while not loop_exit:
    teste = input("Digite a nota ou aperte X para sair: ")
    if teste == 'x' or teste == 'X':
        loop_exit = True
        break
    notas.append(float(teste))

def calcular_media(notas_calc):
    total = sum(notas_calc)
    media_calc = total / len(notas_calc)
    return media_calc

arredondar_media = lambda media: round(media, 0)
media = calcular_media(notas)
media_arredondada = arredondar_media(media)


if media_arredondada >= 7:
    situacao = "Aprovada(o)"
else: 
    situcao_n = "Reprovada(o)"

for teste in notas: 
    print("A nota do(a) aluno(a) é: ", teste)

print("A média do(a) aluno(a) é: ", media_arredondada)    

if media_arredondada >= 7:
    print("O/a aluno(a) foi: ",situacao)
else:
    print("O/a aluno(a) foi: ",situcao_n)

print("Mais bonitnho")