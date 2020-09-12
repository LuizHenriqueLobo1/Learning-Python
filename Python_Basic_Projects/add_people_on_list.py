cont = 1
qtd_pessoas = int(input('Digite a quantidade de pessoas: '))
lista = []
while cont <= qtd_pessoas:
    nomes = str(input('Digite o nome da pessoa: '))
    lista.insert(0, nomes)
    if cont == qtd_pessoas:
        break
    cont += 1
print('Pessoas da lista:\n', lista[::-1])