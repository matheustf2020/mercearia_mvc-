import Controller
import os.path

if __name__ == "__main__":
    while True:
        local = int(input('Digite 1 para acessar (Categorias) \n'
                          'Digite 2 para acessar (Estoque)\n'
                          'Digite 3 para acessar (Fornecedor)\n'
                          'Digite 4 para acessar (Cliente)\n'
                          'Digite 5 para acessar (Funcionario)\n'
                          'Digite 6 para acessar (Vendas)\n' \
                          'Digite 7 para ver os produtos mais vendidos\n'
                          'Digite 0 para sair\n'))
        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input(
                          'Digite 1 para cadastrar uma categoria \n'
                          'Digite 2 para remover uma categoria \n'
                          'Digite 3 para alterar uma categoria \n'
                          'Digite 4 para mostrar as categorias cadastradas \n'
                          'Digite qualquer outra tecla para sair \n'))
                if decidir == 1:
                    categoria = input('Digite uma categoria a ser cadastrada: ')
                    cat.cadastraCategoria(categoria)
                elif decidir == 2:
                    categoria = input('Digite uma categoria a ser removida: ')
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input('Digite a categoria em que deseja alterar: ')
                    novaCategoria = input('Digite a categoria para qual deseja alterar: ')
                    cat.alterarCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    break
        elif local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input(
                          'Digite 1 para cadastrar um produto:  \n'
                          'Digite 2 para remover um produto:  \n'
                          'Digite 3 para alterar um produto:  \n'
                          'Digite 4 para ver o estoque:  \n'
                          'Digite qualquer outra tecla para sair \n'))
                if decidir == 1:
                    nome = input('Digite o nome do produto para cadastrar: ')
                    preco = input('Digite o preco do produto: ')
                    categoria = input('Digite a categoria do produto: ')
                    quantidade = input('Digite a quantidade do produto: ')
                    cat.cadastrarProduto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    nome = input('Nome do produto a ser removido: ')
                    cat.removerProduto(nome)
                    print(f'Produto {nome} foi removido com sucesso')
                elif decidir == 3:
                    nomeAlterar = input('Digite o nome do produto para alterar: ')
                    novoNome = input('Digite o novo nome do produto: ')
                    novoPreco = input('Digite seu novo preço: ')
                    novaCategoria = input('Digite nova categoria: ')
                    novaQuantidade = input('Digite nova quantidade: ')
                    cat.alterarProduto(nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade)
                elif decidir == 4:
                    cat.mostrarEstoque()
                else:
                    break


        elif local == 3:
            forn = Controller.controllerFornecedor()
            while True:
                decidir = int(input(
                          'Digite 1 para cadastrar um fornecedor:  \n'
                          'Digite 2 para remover um fornecedor:  \n'
                          'Digite 3 para alterar um fornecedor:  \n'
                          'Digite 4 para mostrar fornecedores:  \n'
                          'Digite qualquer outra tecla para sair \n'))
                if decidir == 1:
                    nome = input('Digite o nome do fornecedor a cadastrar: ')
                    cnpj = input('Digite CNPJ: ')
                    telefone = input('Digite o telefone: ')
                    categoria = input('Digite a categoria: ')
                    forn.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    nome = input('Digite um fornecedor a ser excluido: ')
                    forn.removerFornecedor(nome)
                elif decidir == 3:
                    nome = input('Digite o nome do fornecedor a ser alterado: ')
                    nomeNovo = input('Digite novo nome do fornecedor: ')
                    novoCnpj = input('Digite o novo CNPJ: ')
                    novoTelefone = input('Digite o novo telefone: ')
                    novaCategoria = input('Digite a categoria nova: ')
                    forn.alterarFornecedor(nome, nomeNovo, novoCnpj, novoTelefone, novaCategoria)
                elif decidir == 4:
                    forn.mostrarFornecedores()
                else:
                    break

        elif local == 4:
            cliente = Controller.controllerCliente()
            while True:
                decidir = int(input(
                          'Digite 1 para cadastrar um cliente:  \n'
                          'Digite 2 para remover um cliente:  \n'
                          'Digite 3 para alterar um cliente:  \n'
                          'Digite 4 para mostrar clientes:  \n'
                          'Digite qualquer outra tecla para sair \n'))
                if decidir == 1:
                    nomeCliente = input('Digite o nome do cliente a ser cadastrado: ')
                    telefoneCliente = input('Digite o telefone do cliente: ')
                    cpf = input('Digite o CPF do cliente: ')
                    email = input('Digite o email do cliente: ')
                    endereco = input('Digite o endereco do cliente: ')
                    cliente.cadastrarCliente(nomeCliente, telefoneCliente, cpf, email, endereco)
                elif decidir == 2:
                    clienteRemover = input('Digite o cliente que você quer remover: ')
                    cliente.removerCliente(clienteRemover)
                elif decidir == 3:
                    nomeAntigo = input('Digite o nome do cliente para alterar: ')
                    nomeNovo = input('Digite o novo cliente: ')
                    novoTelefone = input('Digite novo telefone: ')
                    novoCpf = input('Digite o novo CPF: ')
                    novoEmail = input('Digite o novo Email: ')
                    novoEndereco = input('Digite o novo endereço: ')
                    cliente.alterarCliente(nomeAntigo, nomeNovo, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    cliente.mostrarClientes()
                else:
                    break

        elif local == 5:
            func = Controller.controllerFuncionario()
            while True:
                decidir = int(input(
                          'Digite 1 para cadastrar um funcionario:  \n'
                          'Digite 2 para remover um funcionario:  \n'
                          'Digite 3 para alterar um funcionario:  \n'
                          'Digite 4 para mostrar funcionario:  \n'
                          'Digite qualquer outra tecla para sair \n'))
                if decidir == 1:
                    clt = input('Digite CLT do funcionario: ')
                    nome = input('Digite o nome do funcionario: ')
                    telefone = input('Digite o telefone: ')
                    cpf = input('Digite o CPF: ')
                    email = input('Digite o email do funcionario: ')
                    endereco = input('Digite o endereco: ')
                    func.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    nomeRemover = input('Digite o nome do funcionario que deseja remover: ')
                    func.removerFuncionario(nomeRemover)
                elif decidir == 3:
                    nomeAlterar = input('Digite o nome do funcionario que deseja alterar: ')
                    novaClt = input('Digite nova CLT: ')
                    novoNome = input('Digite o novo nome de funcionario: ')
                    novoTelefone = input('Digite novo telefone: ')
                    novoCpf = input('Digite novo CPF: ')
                    novoEmail = input('Digite novo email: ')
                    novoEndereco = input('Digite novo endereco: ')
                    func.alterarFuncionario(nomeAlterar, novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    func.mostrarFuncionario()
                else:
                    break
        elif local == 6:
            vend = Controller.controllerVenda()
            decidir = (int(input(
                          'Digite 1 para cadastrar uma venda:  \n'
                          'Digite 2 para filtrar as vendas:  \n'
                          'Digite 3 ou outra tecla para sair: \n')))
            if decidir == 1:
                nomeProduto = input('Digite nome do produto vendido: ')
                vendedor = input('Vendedor responsável pela venda: ')
                comprador = input('Digite o nome do comprador: ')
                quantidade = int(input('Digite a quantidade vendida: '))
                vend.cadastrarVenda(nomeProduto, vendedor, comprador, quantidade)
            elif decidir == 2:
                dataInicio = input('Digite data inicio: dia/mes/ano: ')
                dataTermino = input('Digite data termino: dia/mes/ano: ')
                vend.mostrarVenda(dataInicio, dataTermino)
            else:
                break

        elif local == 7:
            a = Controller.controllerVenda()
            a.relatorioProdutos()
        else:
            break



# def criarArquivos(*nome):
#     for i in nome:
#         if not os.path.exists(i):
#             with open(i, 'w') as arq:
#                 arq.write('')

# criarArquivos('categoria.txt', 'clientes.txt', 'estoque.txt', 'fornacedores.txt', 'funcionarios.txt', 'venda.txt', 'relatorio.txt')
