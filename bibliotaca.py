import matplotlib.pyplot as plt #import da biblio matplot

# criando classe livros
class livros:
    def __init__(self, titulo, autor, genero, quantidade_disponivel):
         self.titulo = titulo
         self.autor = autor
         self.genero = genero
         self.quantidade_disponivel = quantidade_disponivel
# print retorno com dados add
    def __str__(self):
        # Corrected to use quantidade_disponivel instead of self.ano_publicacao
        return (f'{self.titulo} por {self.autor}, Quantidade {self.quantidade_disponivel}') 
        pass

# criando lista de livros na biblioteca
biblioteca = []

# função para add livros na biblio
def adicionar_livro(titulo, autor, genero, quantidade_disponivel):
        novo_livro = livros(titulo, autor, genero, quantidade_disponivel)
        biblioteca.append(novo_livro)
        print(f'{titulo} foi adicionado à biblioteca.')

# Função para listar todos os livros na biblioteca
def listar_livros():
    print()
    for livro in biblioteca:
        print(livro)

# add livros
adicionar_livro("Iguape", "G. Trevisani", "turismo", 3) 
adicionar_livro("A primeira maravilha do mundo sou eu", "G. Trevisani", "Romance", 8) 
adicionar_livro("Virando o pé na chuva", "B. Furlan", "Terror", 1) 
adicionar_livro("Quem pegou a coca que estava aqui?", "G. Morilha", "Terror", 2) 
adicionar_livro("Manual para desacumular", "R. G. Régio", "Mudanças", 7)
adicionar_livro("Cansado", "P. G. Alves", "Saúde", 3) 
adicionar_livro("Estudo de uma doença", "A. Trevisani", "Saúde", 4) 
adicionar_livro("Relatos de uma GCD", "R. G. Maciel", "Superação", 1) 
adicionar_livro("Solidão", "M. Dinnouti", "Drama", 2) 
adicionar_livro("Mudando os ares", "G. Trevisani", "Mudanças", 7) 

# proprocurando livros por nome
def procurar_livros(titulo):
    validos = []
    for livro in biblioteca:
        if livro.titulo == input(titulo):
            validos.append(livro)
    return validos

# agrupando os livros por genero
def group_by_genero(livro_element):
    return livro_element.genero

biblioteca.sort(key=group_by_genero) 

# separando os dados
generos = [group_by_genero(livro) for livro in biblioteca]
quantidades = [livro.quantidade_disponivel for livro in biblioteca]

# separando generos
unique_generos = list(set(generos))
# somando quantidades de livros dentro de cada categoria
contagem_livros = [sum([livro.quantidade_disponivel for livro in biblioteca if livro.genero == genero]) for genero in unique_generos]

# Criando um gráfico de barras 
plt.bar(unique_generos, contagem_livros, color='pink')

plt.xlabel('Gênero')
plt.ylabel('Quantidade de livros disponíveis')
plt.title('Quantidade de livros na biblioteca por gênero')

# Adicionando rótulos aos pontos de dados 
for i, valor in enumerate(contagem_livros):
    plt.text(i, valor, str(valor), ha='center', va='bottom')