import time

bd_filmes = [
    ['Vingadores', 2012],
    ['Ilha do Medo', 2010],
    ['Star Wars', 1977],
    ['O senhor dos aneis', 2001]
]

def listar_filmes(bd):
    for i in range(len(bd)):
        print(f"{i + 1}. {bd[i][0]} - ({bd[i][1]})")


def cadastrar_filme(bd, titulo, ano):
    filme = [titulo, ano]
    bd.append(filme)
    return bd


while True:

    print('Bem-Vindo ao CadFilmes')
    print('1 - Cadastrar Filme')
    print('2 - alteraar filme')
    print('3 - Listar Filmes')
    print('0 - Sair')

    try:
        op = int(input('Escolha uma opção: '))
    except Exception as e:
        print(f'Error: {e}')
        op = -1

    time.sleep(1)

    if op == 1:
        print(f'CADASTRO DE FILME')
        titulo = input('Titulo: ')
        ano = input('ano:')
        bd_filmes = cadastrar_filme(bd=bd_filmes, titulo=titulo, ano=ano)

    elif op == 2:
        print('ALTERAR FILME')
        i = int(input('Digite o número do filme que deseja alterar:')) 

        n_titulo = input('Novo Titulo: ')
        n_ano = int(input('Novo ano:'))

    elif op == 3:
        print(f'FILMES CADASTRADOS')
        listar_filmes(bd=bd_filmes)

    elif op == 0:
        print('Saindo...')
        break

    else:
        print('Opção invalida')