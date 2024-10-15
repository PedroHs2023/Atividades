import os 

restaurantes = [{'nome':'Praca','Categoria':'Japonesa','Ativo':False}, 
                {'nome':'Pizza suprema','Categoria':'Pizza','Ativo':True},
                {'nome':'Don Florentino','Categoria':'Italiano','Ativo':True}]

def exibir_nome_do_programa():
    print('Sabor Express            \n')

def exibir_opcoes():
    print('1. Cadastrar restaurante             \n')
    print('2. Listar restaurante                \n')
    print('3. Alternar estado do restaurante    \n')
    print('4. Sair                              \n')
    
def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('opcao invalida! \n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes ')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante,
    'Categoria':categoria, 'Ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def lista_restaurantes():
    exibir_subtitulo('Listar novos restaurantes ')

    print(f'{'Nome do restaurante'.ljust(20)} |  {'Categoria'.ljust(19)} | Ativo ')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['Categoria']
        ativo = 'ativado' if restaurante['Ativo']else 'desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['Ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')        


    voltar_ao_menu_principal()

def escolher_opcao():
    try: 
        opcao_escolhida = int(input('Escolhas uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida   == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            lista_restaurantes()  
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()  
        else                     :
            opcao_invalida() 
    except:
        opcao_invalida()   

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()