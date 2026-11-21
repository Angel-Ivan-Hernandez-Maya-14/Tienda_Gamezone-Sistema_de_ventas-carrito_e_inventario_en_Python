import json
import os

def mostrar(codigos,games,precios,existencias):
    for i in range(len(codigos)):
        print(f"Código del producto {i+1}: {codigos[i]}. | Videojuego: {games[i]}. | Precio: ${round(precios[i],2)}. | Existencia: {existencias[i]}\n")

def buscar(codigos,games,precios,existencias,buscap):
    encontrado=None
    for i in range(len(codigos)):
        indice=-1
        if buscap==codigos[i]:
            encontrado=f"Videojuego: {games[i]}. | Precio: ${round(precios[i],2)}. | Existencia: {existencias[i]}"
            indice=i
            break
        
    return encontrado,indice
        
def valiexst(existencias,indice,cantidad):
    if cantidad<=0:
        print("La cantidad debe ser mayor que cero.")
        existente=False
        return existente,indice
    else:
        if cantidad<=existencias[indice]:
            existente=True
            return existente,indice
        else:
            print(f"\nExistencia insuficiente. Solo hay {existencias[indice]} unidades disponibles.")
            existente=False
            return existente,indice
    
def calcimporte(precios,indice,cantidad,subtotal):
    importe=round(precios[indice]*cantidad,2)
    subtotal=round(subtotal+importe,2)
    return importe,subtotal
    
def calctotal(subtotal,descuento=0.0,impuesto=0.16):
    if subtotal>=1000:
        descuento=0.1
    descontado=round(subtotal*descuento,2)
    impuestoc=round(subtotal*impuesto,2)
    total=round((subtotal-descontado)+impuestoc,2)
    return descontado,impuestoc,total
    
def actualizar(existencias,indice,cantidad):
    existencias[indice]-=cantidad
    return existencias[indice]

def guardarcarrito(carrito,subtotal,descontado,impuestoc,total,nomarch="carrito.json"):
    carpetatienda=os.path.dirname(os.path.abspath(__file__))
    ruta=os.path.join(carpetatienda,nomarch)
    info={
        "productos":carrito,
        "subtotal":round(subtotal,2),
        "descuento":round(descontado,2),
        "impuesto":round(impuestoc,2),
        "total":round(total,2)
    }
    with open(ruta,"w",encoding="utf-8") as archivo:
        json.dump(info,archivo,indent=4,ensure_ascii=False)
    
    return nomarch

