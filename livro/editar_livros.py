from livro.livro_repositorio import livros
from livro.buscar_livros import buscarLivros

def editarLivros(id: int, titulo: str, editora: str, disponivel: bool):
    livro = buscarLivros(id)
    if livro:
        livro['titulo'] = titulo
        livro['editora'] = editora
        livro['disponivel'] = disponivel
        print('Dados alterados com sucesso!')
        return
    print('Erro: Livro não encontrado!')

if __name__ == "__main__":
    print(livros)
    editarLivros(1, "Spider-Man", "Marvel Comics", False)
    print(livros)
