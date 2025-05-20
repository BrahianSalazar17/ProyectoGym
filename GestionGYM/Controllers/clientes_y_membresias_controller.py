# clientes_y_membresias_controller.py j

import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from models.cliente import Cliente
# from models.membresia import Membresia

clientes_data = {}
membresias_data = {}
cliente_id_counter = 1
membresia_id_counter = 1

def obtener_clientes():
    return {"clientes": list(clientes_data.values())}

def obtener_cliente(cliente_id):
    cliente = clientes_data.get(cliente_id)
    return {"cliente": cliente} if cliente else ({"mensaje": "Cliente no encontrado"}, 404)

def crear_cliente(data):
    global cliente_id_counter
    nuevo_id = cliente_id_counter
    clientes_data[nuevo_id] = data
    cliente_id_counter += 1
    return {"mensaje": "Cliente creado", "id": nuevo_id}, 201

def actualizar_cliente(cliente_id, data):
    if cliente_id in clientes_data:
        clientes_data[cliente_id].update(data)
        return {"mensaje": f"Cliente {cliente_id} actualizado"}
    return {"mensaje": "Cliente no encontrado"}, 404

def eliminar_cliente(cliente_id):
    if cliente_id in clientes_data:
        del clientes_data[cliente_id]
        return {"mensaje": f"Cliente {cliente_id} eliminado"}
    return {"mensaje": "Cliente no encontrado"}, 404

def obtener_membresias():
    return {"membresias": list(membresias_data.values())}

def obtener_membresia(membresia_id):
    membresia = membresias_data.get(membresia_id)
    return {"membresia": membresia} if membresia else ({"mensaje": "Membresía no encontrada"}, 404)

def crear_membresia(data):
    global membresia_id_counter
    nuevo_id = membresia_id_counter
    membresias_data[nuevo_id] = data
    membresia_id_counter += 1
    return {"mensaje": "Membresía creada", "id": nuevo_id}, 201

def actualizar_membresia(membresia_id, data):
    if membresia_id in membresias_data:
        membresias_data[membresia_id].update(data)
        return {"mensaje": f"Membresía {membresia_id} actualizada"}
    return {"mensaje": "Membresía no encontrada"}, 404

def eliminar_membresia(membresia_id):
    if membresia_id in membresias_data:
        del membresias_data[membresia_id]
        return {"mensaje": f"Membresía {membresia_id} eliminada"}
    return {"mensaje": "Membresía no encontrada"}, 404

if __name__ == "__main__":
    print("Clientes:")
    print(obtener_clientes())
    print(crear_cliente({"nombre": "Ana", "apellido": "Diaz"}))
    print(obtener_cliente(1))
    print("Membresías:")
    print(obtener_membresias())
    print(crear_membresia({"tipo": "Anual", "precio": 100}))
    print(obtener_membresia(1))
