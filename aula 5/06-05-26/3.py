#CRIE UM SISTEMA DE NOTAS:
#A (10-9)
#B (8-70
#C (abaixo de 7)
nota = 0
nota = int(input("Qual é a nota?"))
#a nota varia de 0 a 10
if nota < 7:
    print("Nota C")
elif nota < 9:
    print("Nota B")
elif nota < 11:
    print("Nota A")
else:
    print("Nota Inválida")