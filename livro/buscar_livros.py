from livro.livro_repositorio import livros

def buscarLivros(id: int) -> dict or None:
    for livro in livros:
        if livro['id'] == id:
            return livro
    return None

if __name__ == "__main__":
    print(buscarLivros(1))
    print(buscarLivros(2))
