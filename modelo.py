class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def ano(self):
        return self._ano    

    @ano.setter
    def ano(self, novo_ano):
        self._ano = novo_ano

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, novo_likes):
        self._likes = novo_likes

    def dar_like(self):
        self.likes += 1

    def __str__(self):
        return f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Likes: {vingadores.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, nova_duracao):
        self.__duracao = nova_duracao

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} - Likes: {self.likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        return self.__temporadas

    @temporadas.setter
    def temporadas(self, nova_temporadas):
        self.__temporadas = nova_temporadas
    
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self.likes}'

vingadores = Filme("vingadores - guera infinita", 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Serie("Atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')

filmes_series = [vingadores, atlanta]

#For com operador ternário
for programa in filmes_series:
    # exemplo de Operador Ternário
    detalhes = f'Duração: {programa.duracao}' if hasattr(programa, 'duracao') else f'Temporadas: {programa.temporadas}'
    print(f'Nome: {programa.nome} - Ano: {programa.ano} - Likes: {programa.likes} - {detalhes}')

#For correto para usufruir do polimorfismo
for programa in filmes_series:
    print(repr(programa))
    print(programa)

print(repr(filmes_series))