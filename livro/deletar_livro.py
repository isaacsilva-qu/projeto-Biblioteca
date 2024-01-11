from livro.livro_repositorio import livros
from livro.buscar_livros import buscarLivros

def deletarLivro(id: int):
    livro = buscarLivros(id)
    if livro:
        livros.remove(livro)
        print('Livro removido com sucesso!')
    else:
        print('Erro: Livro não encontrado!!')

if __name__ == "__main__":
    print(livros)
    deletarLivro(1)
    print(livros)
    deletarLivro(1)
