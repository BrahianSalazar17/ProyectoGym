# registros_y_pagos_controller.py jb

import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

# from models.registro_entrada import RegistroEntrada
# from models.registro_pago import RegistroPago
# from models.tipo_pago import TipoPago

def obtener_registros_entrada():
    registros = []
    return {"registros_entrada": registros}

def obtener_registro_entrada(registro_id):
    registro = None
    return {"registro_entrada": registro}

def crear_registro_entrada(data):
    print(f"Crear entrada: {data}")
    return {"mensaje": "Entrada creada"}, 201

def actualizar_registro_entrada(registro_id, data):
    print(f"Actualizar entrada {registro_id}: {data}")
    return {"mensaje": f"Entrada {registro_id} actualizada"}

def eliminar_registro_entrada(registro_id):
    print(f"Eliminar entrada {registro_id}")
    return {"mensaje": f"Entrada {registro_id} eliminada"}

def obtener_registros_pago():
    registros = []
    return {"registros_pago": registros}

def obtener_registro_pago(registro_id):
    registro = None
    return {"registro_pago": registro}

def crear_registro_pago(data):
    print(f"Crear pago: {data}")
    return {"mensaje": "Pago creado"}, 201

def actualizar_registro_pago(registro_id, data):
    print(f"Actualizar pago {registro_id}: {data}")
    return {"mensaje": f"Pago {registro_id} actualizado"}

def eliminar_registro_pago(registro_id):
    print(f"Eliminar pago {registro_id}")
    return {"mensaje": f"Pago {registro_id} eliminado"}

def obtener_tipos_de_pago():
    tipos_pago = ["Efectivo", "Tarjeta"]
    return {"tipos_de_pago": tipos_pago}

if __name__ == "__main__":
    print(obtener_registros_entrada())
    print(crear_registro_entrada({"cliente": 1, "fecha": "hoy"}))
    print(obtener_tipos_de_pago())
