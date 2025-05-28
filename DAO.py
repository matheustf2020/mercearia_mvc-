from Models import *

class DaoCategoria:
    @classmethod #metodo de class
    def salvar(cls, categoria): #Função para salvar o que vem de categoria
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')



    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines() #ler tudo de categoria e jogar para categoria.txt

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        #cls.categoria = list(map(lambda x: x.split('|'), cls.categoria))
        # Aplica a função para remover '\n' de cada item da lista
        # Explicação:
        # - 'map()' aplica uma função (lambda) em cada item de 'cls.categoria'.
        # - 'lambda x: x.replace('\n', '')' remove todos os '\n' de cada string em 'cls.categoria'.

        #print(cls.categoria)

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat
        #Esse bloco faz: Abrir o arquivo texto, pega tudo que tem e adiciona a lista (cat)

class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda): #Pegar a instancia de venda da model
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendidos.nome + '|' + venda.itensVendidos.preco + '|' + venda.itensVendidos.categoria + '|' + venda.vendedor + '|' + venda.comprador + '|' + str(venda.quantidadeVendida) + '|' + venda.data)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        vend = []
        for i in cls.venda:
             vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return vend


class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + '|' + produto.preco + '|' + produto.categoria + '|' + str(quantidade))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2]), int(i[3])))
        return est


class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + '|' + fornecedor.cnpj + '|' + fornecedor.telefone + '|' + fornecedor.categoria)
            arq.writelines('\n')
        
    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()
        cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))
        forn = []
        for i in cls.fornecedores:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
        return forn
    
class DaoPessoa:
    @classmethod
    def salvar(cls, pessoas: Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(pessoas.nome + '|' + pessoas.telefone + '|' + pessoas.cpf + '|' + pessoas.email + '|' + pessoas.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            cls.clientes = arq.readlines()
        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))
        clientes = []
        for i in cls.clientes:
            clientes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return clientes

class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.clt + '|' + funcionario.nome + '|' + funcionario.telefone + '|' + funcionario.cpf + '|' + funcionario.email + '|' + funcionario.endereco)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()

        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))
        funcionarios = []
        for i in cls.funcionarios:
            funcionarios.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
        return funcionarios
    