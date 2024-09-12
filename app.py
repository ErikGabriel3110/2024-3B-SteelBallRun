import os

def mostra_titulo():
    print('''
    
    Titulo

    ''')
def mostra_escolhas():
    print('1. Cadastro')
    print('2. Listar')
    print('3. Ativar/desativar')
    print('4. Sair')

opcao_escolhida = int(input('Escolha uma opção: '))
print('Você escolheu a opção: ', opcao_escolhida)

def finalizar_progama() :

    os.system('cls')
    print('Finalizando progama')

def escolhe_opcao():

    if opcao_escolhida == 1:
        print('Cadastrar')
    elif opcao_escolhida == 2:
        print('Listar')
    elif opcao_escolhida == 3:
        print('Ativar/desativar')
    else:
        finalizar_progama()

    def main():
        mostra_titulo()
        mostra_escolhas()
        mostra_opcao()

if __name__ == '__main__';
    main()