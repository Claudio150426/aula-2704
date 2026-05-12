#Funçao de cadastro   
def cadastro():
    print("Cadastro")
#Fim Cadastro

#Funçao de Login 
def login():
    print("Login")  
#Fim Login

#Funçao de Sair 
def sair():
    print("Sair")  
#Fim Sair



menu = '''
BEM VINDO AO APP X

ESCOLHA UMA DAS OPÇÕES DO MENU ABAIXO:
[1] CADASTRO
[2] LOGIN
[3] SAIR
'''

print(menu)

opcoes = int(input(""))

match opcoes:
    case 1:
        cadastro()
    case 2:
        login()
    case 3:
        sair()
    case _:
        print("OPÇÃO INVÁLIDA")