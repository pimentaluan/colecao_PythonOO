from registrar_usuarios import Usuarios
from registrar_colecao import Colecao

if __name__ == '__main__':
    user = Usuarios()
    colecao = Colecao(user)
    while True:
        print('''Opções 
1 - Criar usuário
2 - Criar coleção
3 - Adicionar um item em uma coleção
4 - Ver as coleções
5 - Ver informações do usuário
6 - Sair''')
        opcao = input('Escolha uma opção: ')
        
        match opcao:
            case '1':
                print('Vamos criar um usuário:')
                username = input('Username: ')
                password = input('Senha: ')
                user.criar_usuario(username, password)
            
            case '2':
                print('Vamos criar uma coleção')
                nome = input('Escolha o nome da sua nova coleção: ')
                colecao.adicionar_colecao(nome)
            
            case '3':
                print('Vamos adicionar um item a sua coleção')
                colecao_nome = input ('Adicionar em qual coleção? ')
                while True:
                    item_nome = input('Nome do item (n para nenhum): ')
                    colecao.adicionar_item(colecao_nome, item_nome)
                    if item_nome in 'Nn':
                        break
            
            case '4':
                print('Vamos ver suas coleções')
                print(colecao.ver_colecoes)       
                
            case '5':
                print('O usuário é: ')
                print(colecao.get_usuario_info())
                
            case '6':
                break