import os

corredores = [{'nome':'Johnny Joestar', 'categoria':'Velocidade', 'ativo':True},
              {'nome':'Gyro Zeppeli', 'categoria':'Técnica', 'ativo':True},
              {'nome':'Diego Brando', 'categoria':'Força', 'ativo':False},
              {'nome':'Sandman', 'categoria':'Resistência', 'ativo':True}]

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print('')

def retorna_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal')
    main()

def mostra_titulo():
    print('''

    Steel Ball Run - Race for Life

    ''')

def mostra_escolhas():
    print('1. Cadastro de corredores')
    print('2. Listar corredores')
    print('3. Ativar corredor')
    print('4. Sair')

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('Você escolheu a opção: ', opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_corredores()
        elif opcao_escolhida == 2:
            mostrar_corredores()
        elif opcao_escolhida == 3:
            print('Ativar/desativar corredor')
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_corredores():
    exibir_subtitulo('Cadastrar Corredores')

    nome_corredor = input('Digite o nome do corredor: ')
    categoria = input('Digite a categoria do corredor: ')
    corredores.append({'nome': nome_corredor, 'categoria': categoria, 'ativo': False})
    print(f'{nome_corredor} foi adicionado(a) aos corredores de Steel Ball Run')

    retorna_menu_principal()

def mostrar_corredores():
    exibir_subtitulo('Listar Corredores')

    for corredor in corredores:
        nome_corredor = corredor['nome']
        categoria = corredor['categoria']
        ativo = corredor['ativo']
        print(f' - {nome_corredor} | {categoria} | {"Ativo" if ativo else "Inativo"}')
    
    retorna_menu_principal()

def finalizar_programa():
    os.system('cls')
    print('Finalizando programa')

def opcao_invalida():
    print('Essa opção não é permitida')
    retorna_menu_principal()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()

