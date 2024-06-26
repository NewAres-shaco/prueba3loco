import json

def mostrar_menu():
    print("***MUNDO LIBRO***")
    print("1 - Mantenedor de categorias")
    print("2 - Reportes")
    print("3 - Salir")


def menu_mantenedor_categorias():
    opcion = 0
    while opcion !=5:
        print("1 - Agregar categoria")
        print("2 - Editar categoria")
        print("3 - Eliminar categoria")
        print("4 - Buscar categoria")
        print("5 - Volver")
        
        opcion = int(input("Selecciona una opcion "))

        if opcion == 1:
            Agregar_categoria()
        elif opcion == 2:
            editar_categoria()
        elif opcion == 3:
            eliminar_categoria()
        elif opcion == 4:
            buscar_categoria()
        elif opcion == 5:
            quit
        else:
            print("opcion no valida")


def Agregar_categoria():
    Nombre = input("Ingrese el nombre de la nueva categoria ")


    with open('biblioteca.json', 'r+') as archivoJson:
        datos=json.load(archivoJson)
        nueva_categoria={'nombre': Nombre}
        datos['Categoria'].append(nueva_categoria)
        archivoJson.seek(0)
        json.dump(datos, archivoJson, indent=4)

        print(f"Categoria '{Nombre}' agregado correctamente")

def editar_categoria():
    Nombre = input("Ingrese el nombre de la categoria a editar ")
    nuevo_nombre = input("ingrese el nuevo nombre ")


    with open('biblioteca.json', 'r+') as archivoJson:
        datos=json.load(archivoJson)
        for categoria in datos['Categoria']:
            if categoria['Nombre'] == Nombre:
                if nuevo_nombre:
                    categoria['Nombre'] = nuevo_nombre
                archivoJson.seek(0)
                json.dump(datos, archivoJson, indent=4)
                archivoJson.truncate()
                print(f"categoria '{Nombre}' editado correctamente")
                return
                    
        print(f"Categoria '{Nombre}' no encontrada")


def eliminar_categoria():
    Nombre = input("Ingrese el nombre de la categoria a eliminar ")

    with open('biblioteca.json', 'r+') as archivoJson:
        datos=json.load(archivoJson)
        for categoria in datos['Categoria']:
            if categoria['Nombre'] == Nombre:
                datos['Categoria'].remove(categoria)
                archivoJson.seek(0)
                json.dump(datos, archivoJson, indent=4)
                archivoJson.truncate()
                print(f"Categoria '{Nombre}' eliminada correctamente")
                return
        
        print(f"categoria '{Nombre}' no encontrado")


def buscar_categoria():
    Nombre = input("ingrese el nombre de la categoria a buscar ")

    with open('biblioteca.json', 'r') as archivoJson:
        datos=json.load(archivoJson)
        for categoria in datos['Categoria']:
            if categoria['Nombre'] == Nombre:
                print(f"categoria encontrada:\nNombre: {categoria['Nombre']}")
                return
            
        print(f"categoria '{Nombre}' no encontrada")


def mostrar_reporte():
    reporte = {
        "libros": [
            {"nombre": "la casa de bernarda alba", "veces prestado":2},
            {"nombre": "la fiesta del chavo", "veces prestado":11},
            {"nombre": "don quijote de la mancha", "veces prestado":2},
            {"nombre": "la ciudad y los perros", "veces prestado":5}
        ]
    }

    print("Reporte de veces prestado un libro por su nombre:")
    for libros in reporte['libros']:
        print(f"{libros['nombre']:20} - {libros['veces prestado']}")

    nombre_archivo = "Reportes_biblioteca_mundo.json"
    with open(nombre_archivo, 'w') as archivo:
        json.dump(reporte, archivo, indent=4)

    print(f"reporte exportado a '{nombre_archivo}'")                

        







                





        
    




