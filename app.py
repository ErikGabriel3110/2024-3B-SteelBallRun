print("""
 
   Nome

""")

print('1. Cadastro')
print('2. Listar')
print('3. Ativar/desativar')
print('4. Sair')

opcao_escolhida = int(input('Escolha uma opção: '))
print('Você escolheu a opção: ', opcao_escolhida)

if opcao_escolhida == 1:
    print('Cadastrar')
elif opcao_escolhida == 2:
    print('Listar')
elif opcao_escolhida == 3:
    print('Ativar/desativar')
else:
    print('Saindo da aplicação')