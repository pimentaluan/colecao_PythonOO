from registrar_usuarios import Usuarios
from registrar_colecao import Colecao

if __name__ == '__main__':
    user = Usuarios()
    colecao = Colecao(user)
    
    while True:
        try:
            print('\033[47m')
            print('''
            Opções:
            criar - Criar usuário
            nova - Nova coleção
            add - Adicionar um item em uma coleção
            ver - Ver as coleções
            info - Informações do usuário
            sair - Sair
            \033[m''')
            
            opcao = input('Escolha uma opção: ')
            
            match opcao:
                case 'criar':
                    print('\nVamos criar um usuário:')
                    username = input('Username: ')
                    password = input('Senha: ')
                    user.criar_usuario(username, password)
                
                case 'nova':
                    print('\nVamos criar uma coleção')
                    nome = input('Escolha o nome da sua nova coleção: ')
                    colecao.adicionar_colecao(nome)
                
                case 'add':
                    print('\nVamos adicionar um item à sua coleção')
                    colecao_nome = input('Adicionar em qual coleção? ')
                    
                    while True:
                        item_nome = input('Nome do item (n para nenhum): ')
                        
                        if item_nome in 'Nn':
                            break
                        colecao.adicionar_item(colecao_nome, item_nome)
                        
                case 'ver':
                    print('\nVamos ver suas coleções')
                    print(colecao.ver_colecoes)
                    
                case 'info':
                    print('\nAs informações do usuário são:')
                    print(colecao.get_usuario_info())
                    
                case 'sair':
                    print('\nAté mais!')
                    break
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
