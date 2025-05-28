#Dada a folha de pontuação dos participantes para o seu Dia de Esportes Universitários, você deve encontrar a pontuação do segundo colocado. Você recebe pontuações. Armazene-as em uma lista e encontre a pontuação do segundo colocado.

lista = []

while True:

    pontuacao = int(input('Digite sua pontuação, para sair digite 0: '))
    lista.append(pontuacao)
    if pontuacao == 0:
        break
    
    


sort = sorted(lista, reverse=True)
org = list(enumerate(sort))
#max = max(lista)

for i, j in org:
    sel = []
    if i == 1:
        sel.append(j)
        print(f'A segunda maior pontuação é: {j}')   
    

print(org)

