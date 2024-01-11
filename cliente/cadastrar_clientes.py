from cliente.cliente_repositorio import clientes

id_atual = 1

def cadastrarCliente(nome: str):
    global id_atual
    id_atual += 1
    cliente = {
        "id": id_atual,
        "nome": nome,
        "livros": []
    }
    clientes.append(cliente)

if __name__ == "__main__":
    print(clientes)
    cadastrarCliente("Isaac")
    print(clientes)