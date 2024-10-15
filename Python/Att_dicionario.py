pessoas = [{'nome':'Jucelino cudecheque', 'idade': 22, 'cidade':'Criciuma', 'profissao':'medico'},
           {'nome':'TaKoKu navara', 'idade': 28, 'cidade':'Criciuma', 'profissao':'dentista'},
           {'nome':'Thomas Turbando', 'idade': 26, 'cidade':'Criciuma', 'profissao':'mecanico'}]

def adicionar_pessoas():
    nome_pessoa         = input('Digite o nome da pessoa: ')
    idade_pessoa        = input('Digite a idade da pessoa: ')
    cidade_pessoa       = input('Digite a cidade da pessoa: ')
    profissao_pessoa    = input('Digite a profissao da pessoa: ')
    dados_pessoa = {'nome':nome_pessoa, 'idade':int(idade_pessoa), 'cidade':cidade_pessoa, 'profissao':profissao_pessoa}
    pessoas.append(dados_pessoa)

def printar_lista():

    print(f'{'Nome da pessoa'.ljust(20)} |  {'idade'} | {'cidade'.ljust(20)} | {'profissao'.ljust(20)}')
    for pessoa in pessoas:
        nome_pessoa         = pessoa['nome']
        idade_pessoa        = pessoa['idade']
        cidade_pessoa       = pessoa['cidade']
        profissao_pessoa    = pessoa['profissao']
        print(f'{nome_pessoa.ljust(20)} | {idade_pessoa} | {cidade_pessoa.ljust(20)} | {profissao_pessoa.ljust(20)}')

def excluir_campo():
     nome_pessoa        = input('Digite o nome da pessoa que vc quer deletar: ')
     pessoa_encontrada  = False
     
     for pessoa in pessoas:
         if nome_pessoa == pessoa['nome']:
              pessoa_encontrada     = True
              pessoas.remove(pessoa)
              pessoa_encontrada     = True
              mensagem              = f' {nome_pessoa} foi deletado com sucesso!!!' 
              print(mensagem)
     if not pessoa_encontrada:
        print('A pessoa nao foi encontrada')
    

def alternar_idade():
    nome_pessoa         = input('Digite o nome da pessoa que deseja alterar a idade: ')
    idade_pessoa        = int(input('Digite o valor novo da idade'))
    pessoa_encontrada   = False

    for pessoa in pessoas:
        if nome_pessoa == pessoa['nome']:
            pessoa_encontrado   = True
            pessoa['idade']     = idade_pessoa
            mensagem            = f'A idade foi alteradade de {nome_pessoa} foi alterada com sucesso' 
            print(mensagem)
    if not pessoa_encontrado:
        print('A pessoa nao foi encontrado') 

adicionar_pessoas()
alternar_idade()
printar_lista()
excluir_campo()
printar_lista()