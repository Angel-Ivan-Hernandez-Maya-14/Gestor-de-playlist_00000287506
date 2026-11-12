canciones=[]
artistas=[]

def menu():
    print("\n===MENU DE PLAYLIST===")
    print("1. Agregar cancion")
    print("2. Mostrar playlist")
    print("3. Buscar cancion")
    print("4. Eliminar cancion")
    print("5. Salir\n")

def agregar():
    cancion=str(input("Titulo de la cancion: "))
    artista=str(input("Artsita: "))
    canciones.append(cancion)
    artistas.append(artista)
    print(f"´{cancion}´ de {artista} agregada con éxito.")

def mostrar():
    print("\n===Lista de reproduccion===\n")
    for i in range(len(canciones)):
        print(f"{canciones[i]} - {artistas[i]}")

def buscar():
    encontrado=False
    busca=str(input("Ingrese el nombre de la cancion a buscar: "))
    for i in range(len(canciones)):
        if canciones[i]==busca:
            print(f"Cancion encontrada: {canciones[i]} - {artistas[i]}")
            encontrado=True
            break
        else:
            encontrado=False
    if encontrado==False:
        print("Cancion no encontrada")

def eliminar():
    encontrado1=False
    busca1=str(input("Ingrese el nombre de la cancion a eliminar: "))
    for i in range(len(canciones)):
        if canciones[i]==busca1:
            print(f"Cancion eliminada: {canciones[i]} - {artistas[i]}")
            encontrado1=True
            canciones.remove(canciones[i])
            artistas.remove(artistas[i])
            break
        else:
            encontrado1=False
    if encontrado1==False:
        print("Cancion no encontrada. Por lo tanto no se elimino")


        
            


