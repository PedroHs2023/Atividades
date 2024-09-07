#def entrada_de_dados():
#    idade = int(input('Digite sua idade : '))
#    if 0 <= idade <= 12:
#         print('Crianca')
#    elif 13 >= idade <=18:
#         print('Adolecente')
#    else:
#         print('adulto')

#def entrada_de_dados():
#   usuario_banco = "pedro"
#    senha_banco = 123
#   usuario = input('Digite o usuario: ')
#    senha   = int(input('Digite a senha: '))
#    if usuario == usuario_banco and senha == senha_banco:
#        print('Usuario encontrado')
#    else:
#        print('Login invalido')

def entrada_de_dados():
    x = int(input('Digite as cordenadas no ponto x : '))
    y = int(input('Digite as cordenadas no ponto y:  '))

    if x > 0 and y > 0:
        print('Primeiro Quadrante')
    elif x < 0 and y > 0:
        print('Segundo Quadrante')
    elif x < 0 and y < 0:
        print('Terceiro Quadrante')
    elif x > 0 and y < 0:
        print('Quarto Quadrante')
    else:
        print('O ponto esta localizado no eixo ou origem')

def main():
    entrada_de_dados()

if __name__ == '__main__':
    main()