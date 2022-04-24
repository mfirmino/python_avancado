#A partir do Python 3, o operador != retorna automaticamente o inverso do retorno do método __eq__(), se o método __ne__() não tiver sido implementado.
#Apesar disso, se sua classe herdar de outra em que o método __ne__() é definido (como é nos tipos primitivos), o comportamento do != se baseará no que é especificado nesse método, não no inverso do __eq__()!
#Por conta disso, é recomendável sempre declarar o método __ne__() quando quisermos implementar o __eq__(), tanto pela compatibilidade com o Python 2 (que sem esse método vai comparar os ids), quanto para evitar possíveis problemas em nosso código.

class Filme():
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor
    def __str__(self):
        return self.titulo + ' - ' + self.diretor
    def __eq__(self, outro_filme):
        return self.titulo == outro_filme.titulo

def pega_todos_os_filmes():
    filme1 = Filme('A Teoria de Tudo', 'James Marsh')
    filme2 = Filme('La La Land', 'Damien Chazelle')
    filme3 = Filme('O Poderoso Chefão', 'Francis Ford Coppola')
    return [filme1, filme2, filme3]



meus_filmes = pega_todos_os_filmes()
for filme in meus_filmes:
    print(filme)

def tenho_o_filme_pior_modo(filme_procurado):
    meus_filmes = pega_todos_os_filmes()
    for filme in meus_filmes:
        if filme_procurado == filme:
            return True
    return False

def tenho_o_filme(filme_procurado):
    meus_filmes = pega_todos_os_filmes()
    return filme_procurado in meus_filmes

filme_procurado = Filme('A Teoria de Tudo', 'James Marsh')

if tenho_o_filme(filme_procurado):
    print('Tenho o filme!')
else:
    print('Não tenho :(')   