class Colecao:
    def __init__(self, user):
        self.__user = user
        self.__colecoes = {}

    def adicionar_colecao(self, nome_colecao):
        self.__colecoes[nome_colecao] = []

    def remover_colecao(self, nome_colecao):
        del self.__colecoes[nome_colecao]

    def adicionar_item(self, nome_colecao, nome_item):
        try:
            self.__colecoes[nome_colecao].append(nome_item)
        except Exception as e:
            print(f'Você teve um erro {e}')            
            
    def remover_item(self, nome_colecao, nome_item):
        self.__colecoes[nome_colecao].remove(nome_item)

    def get_usuario_info(self):
        return str(self.__user)

    @property
    def ver_colecoes(self):
        resultado = ""
        for colecao, itens in self.__colecoes.items():
            resultado += f'{colecao}:\n'
            for item in itens:
                resultado += f'- {item}\n'
        return resultado

    def __str__(self):
        return f'Criando usuário e iniciando coleção {self.__colecoes}'