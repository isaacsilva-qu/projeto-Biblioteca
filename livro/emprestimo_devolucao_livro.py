from livro.livro_repositorio import livros
from livro.buscar_livros import buscarLivros

def emprestarLivro(id: int):
    livro = buscarLivros(id)
    if not livro:
        print('Livro não encontrado!')
        return

    if not livro['disponivel']:
        print('Erro: O livro está indisponível!')

    livro['disponivel'] = False
    print('Emprestimo realizado com sucesso!')

def devolverLivro(id: int):
    livro = buscarLivros(id)
    if not livro:
        print('Erro: Livro não encontrado!')
        return
    if livro['disponivel']:
        print('Erro: O livro já está disponível!')
        return

    livro['disponivel'] = True
    print('Livro devolvido com sucesso!')

if __name__ == "__main__":
    print(livros)
    emprestarLivro(1)
    print(livros)
    devolverLivro(1)
    print(livros)