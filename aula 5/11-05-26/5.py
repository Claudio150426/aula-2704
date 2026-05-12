#Funçao de cadastro   
def cadastro(n):
    print(f"Usuário {n} cadastrado com sucesso")
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

def menu_principal():

    while True:

        print(menu)
        opcoes = int(input(""))

        match opcoes:
            
            case 1:
                nome = input("Qual o seu nome?")
                cadastro(nome)
            case 2:
                login()
            case 3:
                sair()
                break
            case _:
                print("OPÇÃO INVÁLIDA")
menu_principal()
