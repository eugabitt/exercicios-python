nota1 = float(input("Nota da primeira prova: "))
nota2 = float(input("Nota da segunda prova: "))
nota3 = float(input("Nota do trabalho: "))
soma = (nota1+nota2+nota3) / 3
if soma >= 8:
    print("Parabéns, você passou com",  f'{soma:.1f}', "pontos")
elif (soma > 5.9):
    print("Você passou raspando com", f'{soma:.1f}',"e tem a opção de aumentar a nota.")
else:
    print("Ruim, você rodou, recuperação direto com seus míseros", f'{soma:.1f}',"pontinhos")