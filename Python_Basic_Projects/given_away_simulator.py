from random import randint
controle = True
while controle == True:
    dado = randint(0, 6)
    resposta = int(input('\n*1* GIRAR DADO\n*2* SAIR\n R -> '))
    if resposta == 1:
        print('\n', dado)
    else:
        controle = False