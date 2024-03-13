class Usuarios:
    def __init__(self):
        self.__user = None
        self.__password = None

    def criar_usuario(self, username, password):
        self.__user = username
        self.__password = password
        self.salvar_user()

    def mudar_senha(self, username, senha_antiga, senha_nova):
        if username == self.__user and senha_antiga == self.__password:
            self.__password = senha_nova
            print("Senha alterada com sucesso!")
        else:
            print("Usuário ou senha antiga incorretos.")
            
    def salvar_user(self):
        arquivo = open('users.txt', 'w')
        arquivo.write(f'{self.__user}, {self.__password}')
        arquivo.close()

    @property
    def usuario(self):
        return self.__user

    def __str__(self):
        return f'Usuário: {self.__user}'
