from funciones import mostrar_menu, menu_mantenedor_categorias, mostrar_reporte

while True:
    mostrar_menu()
    opcion_principal = int(input("escoga una opcion "))

    if opcion_principal == 1:
        menu_mantenedor_categorias()
    elif opcion_principal == 2:
        mostrar_reporte()
        print("reporte generado correctamente")
    elif opcion_principal == 3:
        print("Saliendo..")
        break
    else:
        print("opcion no valida, vuelva a intentarlo")                       
                           
