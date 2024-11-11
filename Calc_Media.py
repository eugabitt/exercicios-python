nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
 
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

arredondar_media = lambda media: round(media, 2)
media = calcular_media([nota1, nota2, nota3])
media_arredondada = arredondar_media(media)
if media_arredondada >= 7:
    print("Aprovada(o)")
else:
    print("Reprovada(o)")
