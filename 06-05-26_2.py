idade = int(input("Qual é a sua idade?"))

if idade < 12:
    print("Criança")
elif idade <18:
      print("Adolescente")
elif idade <=59:
    print("Adulto")
else:
    print("Idoso")