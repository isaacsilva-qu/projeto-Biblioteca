from cliente.cliente_repositorio import clientes

def buscarClientes(id: int) -> dict or None:
    for cliente in clientes:
        if cliente['id'] == id:
            return cliente
    return None

if __name__ == "__main__":
    print(buscarClientes(1))