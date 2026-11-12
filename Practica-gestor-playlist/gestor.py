canciones=[]
artistas=[]

def menu():
    print("\n===MENU DE PLAYLIST===")
    print("1. Agregar canción")
    print("2. Mostrar playlist")
    print("3. Buscar canción")
    print("4. Eliminar canción")
    print("5. Salir\n")

def agregar():
    cancion=str(input("Título de la canción: "))
    artista=str(input("Artista: "))
    canciones.append(cancion)
    artistas.append(artista)
    print(f"´{cancion}´ de {artista} agregada con éxito.")

def mostrar():
    print("\n===Lista de reproducción===\n")
    for i in range(len(canciones)):
        print(f"{canciones[i]} - {artistas[i]}")

def buscar():
    encontrado=False
    busca=str(input("Ingrese el nombre de la canción a buscar: "))
    for i in range(len(canciones)):
        if canciones[i]==busca:
            print(f"Cancion encontrada: {canciones[i]} - {artistas[i]}")
            encontrado=True
            break
        else:
            encontrado=False
    if encontrado==False:
        print("Canción no encontrada")

def eliminar():
    encontrado1=False
    busca1=str(input("Ingrese el nombre de la canción a eliminar: "))
    for i in range(len(canciones)):
        if canciones[i]==busca1:
            print(f"Canción eliminada: {canciones[i]} - {artistas[i]}")
            encontrado1=True
            canciones.remove(canciones[i])
            artistas.remove(artistas[i])
            break
        else:
            encontrado1=False
    if encontrado1==False:
        print("Canción no encontrada. Por lo tanto no se eliminó")


        
            


