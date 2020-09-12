programa = True
opcao = 9
dados = dict()
registrado = 0

while programa == True:
    print('\n***** MENU *****\n1-REGISTRAR PESSOA\n2-MOSTRAR PESSOA\n3-SAIR')
    print('*' * 16)
    opcao = int(input('\nDigite a opcao: '))
    if opcao == 3:
        print('\nPROGRAMA ENCERRADO!')
        programa = False
    elif opcao == 1:
        print('\nPreencha os dados a seguir:')
        dados['Nome']  = str(input('Digite o nome -> '))
        dados['Idade'] = int(input('Digite a idade -> '))
        dados['CPF']   = str(input('Digite o CPF -> '))
        registrado += 1
        print('\nPESSOA REGISTRADA COM SUCESSO!')
    elif opcao == 2:
        if registrado <= 0:
            print('\nNINGUEM FOI REGISTRADO AINDA...')
        else:
            print('\nPessoa registrada: ')
            for k, v in dados.items():
                print(f'{k}: {v}')
    else:
        print('\nOPCAO INVALIDA, DIGITE OUTRA...')