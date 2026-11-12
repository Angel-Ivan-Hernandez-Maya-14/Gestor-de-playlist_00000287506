import gestor

while True:
    gestor.menu()
    opcion=int(input("Elige una opción: "))
    if opcion==1:
        gestor.agregar()
    elif opcion==2:
        gestor.mostrar()
    elif opcion==3:
        gestor.buscar()
    elif opcion==4:
        gestor.eliminar()
    elif opcion==5:
        print("Saliendo del programa...")
        break
    else:
        print("\nOpción no válida. Intentelo de nuevo.")


#Capturas en classroom, codigo en github, el enlace del github en classroom