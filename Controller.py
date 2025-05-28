from Models import Categoria, Estoque, Produtos, Fornecedor, Pessoa, Funcionario, Venda
from DAO import DaoCategoria, DaoVenda, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario
from datetime import datetime

class ControllerCategoria:
    
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler() #Chama a DAOLER
        #validação: 
        for i in x:
            if i.categoria == novaCategoria:
                existe = True #Ele vai iterar e procurar se ja existe uma categoria igual a nova categoria, se sim ele vai retornar True
        if not existe:
            DaoCategoria.salvar(novaCategoria) #se não existir ele vai chamar o salvar do Dao, e para o usuario saber que foi salvo, precisamos passar uma mensagem para ele.
            print('Categoria cadastrada com sucesso.')
        else:
            print('A categoria que deseja cadastrar, já existe!')


#a = ControllerCategoria()
#a.cadastraCategoria('Smartphones')


    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler() #Chama a DAOLER para ler todas as categorias salvas
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x)) 
        if len(cat) <= 0:
            print('A categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso')
            #TODO: COLOCAR SEM CATEGORIA NO ESTOQUE
            #até aqui removemos a categoria apenas da memoria ram, mas ainda ta na lista ou banco
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

        
        estoque = DaoEstoque.ler()
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, 'Sem Categoria'), x.quantidade) if(x.produto.categoria == categoriaRemover) else(x), estoque))

        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')



    def alterarCategoria(self, categoriaAlterar, categoriaAlterada): #Não pode receber apenas um parametro, ele recebe a categoria a alterar e depois categoria alterada.
        x = DaoCategoria.ler() #x igual a lista de categorias puxadas pela dao ler.

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))
        if len(cat) > 0:
            catalterada = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(catalterada) == 0: #Aqui ele garante que não existe uma categoria com nome existente com o que vai alterar.
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
                print('Categoria alterada com sucesso')

                estoque = DaoEstoque.ler()
                estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoriaAlterada), x.quantidade) if(x.produto.categoria == categoriaAlterar) else(x), estoque))
                

                with open('estoque.txt', 'w') as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                        arq.writelines('\n')

            else: 
                print('A categoria para qual deseja alterar já existe')

        else:
            print('A categoria que deseja alterar não existe')
        #Novamente essas mudanças até aqui o código só altera na memoria ram, e não no código txt, a seguir vamos altera-lo no código.
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria vazia')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')
    
class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()

        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0: #Se existir na lista a categoria
            if len(est) == 0: #Se o produto não tiver o mesmo nome ja na lista.
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso')
            else:
                print('O produto ja existe em estoque')
        else:
            print('Categoria inexistente')


    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda i: i.produto.nome == nome, x))
        #ou:
        # est = []
        # for i in x:
        #     if i.produto.nome == nome:
        #         est.append(i)

        if len(est) > 0:
            for i in range(len(x)): #vai percorrer toda DaoEstoque.ler()
                if x[i].produto.nome == nome: #se ele encontrar na lista o nome digitado dentro de .produto.nome ele vai deletar.
                    del x[i]
                    break
                print('Produto removido com sucesso')
        else:
            print('O produto que deseja remover não existe')
#da memoria pra cima
        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        c = list(filter(lambda i: i.categoria == novaCategoria, y))
        if len(c) > 0:
            est = list(filter(lambda i: i.produto.nome == nomeAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda i: i.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda i: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if(i.produto.nome == nomeAlterar) else(x), x))
                    print('O produto foi alterado com sucesso')
                else:
                    print('Produto já cadastrado')
            else:
                print('O produto que deseja alterar não existe')
            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                    arq.writelines('\n')
        else:
            print('A categoria informada não existe')



    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio')
        else:
            for i in estoque:
                print('-' * 10)
                print(f'Nome: {i.produto.nome}\n'
                      f'Preco: {i.produto.preco}\n'
                      f'Categoria: {i.produto.categoria}\n'
                      f'Quantidade: {i.quantidade}')
                
class controllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        '''
        return 1 = produto não existe
        return 2 = quantidade vendida não tem estoque
        return 3 = venda efetuada com sucesso 

        '''
        x = DaoEstoque.ler()
        temp = []
        existe = False # variavel que diz que não existe produto em estoque
        quantidade = False # 

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)

                        DaoVenda.salvar(vendido)

            temp.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])
        arq = open('estoque.txt', 'w')
        arq.write("")
       
        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i[0].nome + '|' + i[0].preco + '|' + i[0].categoria + '|' + str(i[1])) 
                arq.writelines('\n')

        if existe == False:
            print('O produto não existe')
            return None
        elif not quantidade:
            print('A quantidade vendida não contem em estoque')
            return None
        else:
            print('Venda realizada com sucesso')
            return valorCompra
        
    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.itensVendidos.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)}
                if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})

        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)
        print('Esses são os produtos mais vendidos')
        a = 1
        for i in ordenado:
            print(f'==========Produtos [{a}]==========')
            print(f'Produto: {i['produto']}\n'
                    f'Quantidade: {i['quantidade']}\n')
            a += 1
        #escrever em relatorio.txt
        with open('relatorio.txt', 'w') as arq:
            arq.write('Esses sao os produtos mais vendidos\n')
            a = 1
            for i in ordenado:
                arq.writelines(f'==========Produtos [{a}]==========\n')
                arq.writelines(f'Produto: {i['produto']}\n')
                arq.writelines(f'Quantidade: {i['quantidade']}\n')
                a += 1
            
        



    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y')
        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1 and datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas))

        count = 1
        total = 0

        for i in vendasSelecionadas:
            print(f'==========Venda [{count}]==========')
            print(f'Nome: {i.itensVendidos.nome}\n'
                  f'Categoria: {i.itensVendidos.categoria}\n'
                  f'Data: {i.data}\n'
                  f'Quantidade: {i.quantidadeVendida}\n'
                  f'Cliente: {i.comprador}\n'
                  f'Vendedor: {i.vendedor}')
            total += int(i.itensVendidos.preco) * int(i.quantidadeVendida)
            count += 1

        print(f'Total vendido: R${total:.2f} reais')

class controllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        fornecedor = DaoFornecedor.ler()
        
        listacnpj = list(filter(lambda i: i.cnpj == cnpj, fornecedor))
        listatelefone = list(filter(lambda i: i.telefone == cnpj, fornecedor))
        if len(listacnpj) > 0:
            print('O CNPJ já existe')
        elif len(listatelefone) > 0:
            print('O telefone já existe')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            else:
                print('Digite um CNPJ ou Telefone válido')

    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novoCategoria):
        x = DaoFornecedor.ler()
        est = list(filter(lambda i: i.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda i: i.cnpj == novoCnpj, x))
            if len(est) == 0:
                x = list(map(lambda i: Fornecedor(novoNome, novoCnpj, novoTelefone, novoCategoria) if(i.nome == nomeAlterar) else(i), x))
            else:
                print('CNPJ já existe')
        else:
            print('O fornecedor que deseja alterar não existe')
        
        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + str(i.categoria))
                arq.writelines('\n')
            print('Fornecedor alterado com sucesso')

    def removerFornecedor(self, nome):
        x = DaoFornecedor.ler()
        
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O fornecedor que deseja remover não existe')
            return None
        
        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + str(i.categoria))
                arq.writelines('\n')
            print('Fornecedor removido com sucesso')

    def mostrarFornecedores(self):
        fornecedores = DaoFornecedor.ler()
        if len(fornecedores) == 0:
            print('Lista de fornecedores vazia')
        
        for i in fornecedores:
            print('==========Fornecedores==========')
            print(f'Categoria fornecida: {i.categoria}\n'
                    f'Nome: {i.nome}\n'
                    f'Telefone: {i.telefone}\n'
                    f'CNPJ: {i.cnpj}')
                

class controllerCliente:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()
        listacpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listacpf) > 0:
            print('CPF já existente')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('Cliente cadastrado com sucesso')
            else:
                print('Digite um CPF ou telefone válido')
    
    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoPessoa.ler()
        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if(x.nome == nomeAlterar) else(x), x))

        else:
            print('O Cliente que deseja alterar não existe')
        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')
            print('Cliente alterado com sucesso')
        
    def removerCliente(self, nome):
        x = DaoPessoa.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O cliente que deseja remover não existe')
            return None
        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')
            print('Cliente removido com sucesso')

    def mostrarClientes(self):
        clientes = DaoPessoa.ler()
        if len(clientes) == 0:
            print('Lista de clientes vazia')
        for i in clientes:
            print('==========Cliente==========')
            print(f'Nome: {i.nome}\n'
                  f'Telefone: {i.telefone}\n'
                  f'Endereco: {i.endereco}\n'
                  f'Email: {i.email}\n'
                  f'CPF: {i.cpf}')
        

class controllerFuncionario:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()
        listacpf = list(filter(lambda x: x.cpf == cpf, x))
        listaclt = list(filter(lambda x: x.clt == clt, x))
        if len(listacpf) > 0:
            print('CPF já existe')
        elif len(listaclt) > 0:
            print('Já existe um funcionário essa CLT')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print('Funcionario cadastrado com sucesso')
            else:
                print('Digite um cpf ou telefone válido')
    
    def alterarFuncionario(self, nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoFuncionario.ler()
        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Funcionario(novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco), x))
        else:
            print('O funcionario que deseja alterar não existe')

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + '|' + i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')
            print('Funcionario alterado com sucesso')
        
    
    def removerFuncionario(self, nome):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O funcionario que deseja remover não existe')
            return None
        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')
            print('Funcionario removido com sucesso')

    def mostrarFuncionario(self):
        funcionario = DaoFuncionario.ler()

        if len(funcionario) == 0:
            print('Lista de funcionarios vazia')

        for i in funcionario:
            print('==========Funcionario==========')
            print(f'Nome: {i.nome}\n'
                  f'Telefone: {i.telefone}\n'
                  f'Email: {i.email}\n'
                  f'Endereço: {i.endereco}\n'
                  f'CPF: {i.cpf}\n'
                  f'CLT: {i.clt}\n')




