class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def ano(self):
        return self.__ano    

    @ano.setter
    def ano(self, novo_ano):
        self.__ano = ano

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, nova_duracao):
        self.__duracao = nova_duracao

    @property
    def likes(self):
        return self.__likes

    @likes.setter
    def likes(self, novo_likes):
        self.__likes = novo_likes

    def dar_like(self):
        self.likes += 1
    

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def ano(self):
        return self.__ano    

    @ano.setter
    def ano(self, novo_ano):
        self.__ano = ano

    @property
    def temporadas(self):
        return self.__temporadas

    @temporadas.setter
    def temporadas(self, nova_temporadas):
        self.__temporadas = nova_temporadas

    @property
    def likes(self):
        return self.__likes

    @likes.setter
    def likes(self, novo_likes):
        self.__likes = novo_likes

    def dar_like(self):
        self.likes += 1


vingadores = Filme("vingadores - guera infinita", 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Serie("Atlanta", 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')