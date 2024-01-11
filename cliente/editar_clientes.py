from cliente.cliente_repositorio import clientes
from cliente.buscar_cliente import buscarClientes

def editarClientes(id: int, nome: str):
    cliente = buscarClientes(id)
    if cliente:
        cliente['nome'] = nome
        print('Dados alterados com sucesso!')
        return
    else:
        print("")