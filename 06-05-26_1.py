#DESAFIO: RECEBA DO USUÁRIO O NOME E A IDADE.
#CALCULE O ANO DE NASCIMENTO DO USUÁRIO E UTILIZE OS DADOS RECEBIDOS PARA ESCREVER NA SAÍDA PADRÃO, CONFORME O EXEMPLO A SEGUIR
#"FULANO VOCÊ NASCEU EM 19XX"

nome = input("Qual é o sua nome?")

idade = int(input("Qual é a sua idade?"))

print(f"{nome} vc nasceu em {2026 - idade}")