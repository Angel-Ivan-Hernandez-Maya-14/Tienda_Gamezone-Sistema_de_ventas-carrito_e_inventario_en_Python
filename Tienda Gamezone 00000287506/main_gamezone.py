import sistemaventasgamezone
import time

codigos=["G001","G002","G003","G004","G005"]
games=["DOOM Eternal","Minecraft","The Legend of Zelda: Tears of the Kingdom","Super Mario Bros. Wonder","Hollow Knight"]
precios=[699.00,499.00,1199.00,999.00,249.00]
existencias=[5,8,3,4,10]

def main():
    carrito = []
    subtotal = 0.0
    while True:
        print("\n====================================CATÁLOGO====================================\n")
        sistemaventasgamezone.mostrar(codigos,games,precios,existencias)
        while True:
            buscap=str(input("Ingrese el código del videojuego que desea buscar (o 'SALIR'): "))
            if buscap=="SALIR":
                print("\n==============================RESUMEN DE COMPRA==============================\n")
                if len(carrito)==0:
                    print("Todavía no hay productos agregados al carrito")
                else:
                    for linea in carrito:
                        print(f"Videojuego: {linea['videojuego']} | Cantidad: {linea['cantidad']} | Importe: ${round(linea['importe'], 2)}")
                
                descontado,impuestoc,total=sistemaventasgamezone.calctotal(subtotal,descuento=0.0,impuesto=0.16)
                print(f"\nSubtotal: ${round(subtotal,2)}")
                print(f"Descuento: ${round(descontado,2)}")
                print(f"Impuesto (16%): ${round(impuestoc,2)}")
                print(f"Total a pagar: ${round(total,2)}")
                sistemaventasgamezone.guardarcarrito(carrito,subtotal,descontado,impuestoc,total)
                print("\n==============================INVENTARIO RESTANTE==============================\n")
                sistemaventasgamezone.mostrar(codigos,games,precios,existencias)
                print("\nSaliendo del programa...")
                time.sleep(2)
                print("Hasta luego :)")
                return
            
            print()
            encontrado,indice=sistemaventasgamezone.buscar(codigos,games,precios,existencias,buscap)
            if indice!=-1:
                print(encontrado)
                break
            else:
                print("El código que ingresaste no está disponible. Intentelo de nuevo.\n")
                    
        cantidad=int(input("\nIngrese la cantidad de unidades que desea comprar de ese videojuego: "))
        existente,indice=sistemaventasgamezone.valiexst(existencias,indice,cantidad)
        print()
        print(existente)
        if existente==True:
            importe,subtotal=sistemaventasgamezone.calcimporte(precios,indice,cantidad=cantidad,subtotal=subtotal)
            carrito.append({
                "codigo": codigos[indice],
                "videojuego": games[indice],
                "cantidad": cantidad,
                "importe": importe
            })
            print(f"Importe: ${round(importe,2)}.")
            act=sistemaventasgamezone.actualizar(existencias,indice,cantidad)
            print(f"Existencia actualizada: {act} unidades")
            
if __name__== "__main__":
    main()