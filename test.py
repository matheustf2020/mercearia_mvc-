saldo = 0
conta2 = 0
def transferirSaldo(conta_corrente, conta_poupanca):
    valorTransfer = float(input('Digite o valor a ser transferido para conta poupança: '))
    if valorTransfer > conta_corrente:
        print('Valor na conta corrente insuficiente')
        return conta_corrente, conta_poupanca
    else:
        conta_corrente -= valorTransfer
        conta_poupanca += valorTransfer
        print(f'Valor transferido com sucesso')
        return conta_corrente, conta_poupanca
    
def poupforCorrente(conta_corrente, conta_poupanca):
    valorTransfer = float(input('Digite o valor que você quer transferir da sua conta poupança para corrente: '))
    if valorTransfer > conta_poupanca:
        print('Saldo na conta poupança insuficiente')
        return conta_corrente, conta_poupanca
    else:
        conta_poupanca -= valorTransfer
        conta_corrente += valorTransfer
        print(f'O valor foi adicionado a sua conta corrente')
        return conta_corrente, conta_poupanca

    
def adicionarSaldo(saldo, conta2):
    opc = int(input('Digite a 1 para conta corrente, e 2 para conta poupança: '))
    valor = float(input('Digite valor a adicionar: '))
    if opc == 1:
        saldo += valor
        print(f'O valor R${valor:.2f} reais foi adicionado em sua conta')
        return saldo, conta2
    elif opc == 2:
        conta2 += valor
        print(f'O valor R${valor:.2f} reais foi adicionado em sua conta')
        return saldo, conta2
        
def saqueSaldo(saldo_atual):
    valor = float(input('Digite valor a ser sacado: '))
    if valor > saldo_atual:
        print(f'Saldo insuficiente')
        return saldo_atual 
    else:
        saldo_atual -= valor
        print(f'O valor R${valor:.2f} reais, foi retirado de sua conta')
        return saldo_atual

def saquePoupanca(saque_poupanca):
    valor = float(input('Digite um valor para sacar da conta poupança: '))
    if valor > saque_poupanca:
        print('Saldo poupança insuficiente para sacar')
        return saque_poupanca
    else:
        saque_poupanca -= valor
        print(f'O valor R${valor:.2f} reais foi sacado com sucesso')
        return saque_poupanca

def mostrarSaldo(saldo, conta2):
    opc = int(input('Digite 1 para ver o saldo da conta 1 e 2 para o saldo da conta 2: '))
    if opc == 1:
        print(f'Conta 1 tem o saldo de R${saldo:.2f} reais')
    elif opc == 2:
        print(f'Conta poupança tem o saldo de R${conta2:.2f} reais')
    

while True:
    print('=' * 30)
    print('Digite 1 para adicionar um valor: \n'
          'Digite 2 para sacar um valor da conta corrente: \n'
          'Digite 3 para sacar um valor da conta poupança: \n'
          'Digite 4 para ver saldo: \n'
          'Digite 5 para transferir da conta corrente para a poupança: \n' \
          'Digite 6 para transferir da poupança para a conta corrente: \n'
          'Digite 0 para sair..')
    print('=' * 30)
    opc = int(input('Digite uma opção válida: '))
    if opc == 1:
        saldo, conta2 = adicionarSaldo(saldo, conta2)
    elif opc == 2:
        saldo = saqueSaldo(saldo)
    elif opc == 3:
        conta2 = saquePoupanca(conta2)
    elif opc == 4:
        mostrar = mostrarSaldo(saldo, conta2)
    elif opc == 5:
        saldo, conta2 = transferirSaldo(saldo, conta2)
    elif opc == 6:
        saldo, conta2 = poupforCorrente(saldo, conta2)
    elif opc == 0:
        print('Você escolheu sair..')
        break
    else:
        print('Opção inválida, tente novamente.')

        