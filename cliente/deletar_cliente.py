from cliente.cliente_repositorio import clientes
from cliente.buscar_cliente import buscarClientes

def deletarCliente(id: int):
    cliente = buscarClientes(id)
    if cliente:
        clientes.remove(cliente)
        print("Cliente removido com sucesso!")
    else:
        print("Cliente não encontrado!")

if __name__ == "__main__":
    print(clientes)
    deletarCliente(1)
    print(clientes)