from random import randint
num_random = randint(0, 9)
tag = True
print('\n* CHUTE UM NUMERO ENTRE 0/9 *')
while tag == True:
    resposta = int(input('  R -> '))
    if resposta == num_random:
        print('\n* RESPOSTA CORRETA! =D *')
        tag = False
    else:
        print('\n* RESPOSTA ERRADA, tente novamente! *\n')
        tag = True