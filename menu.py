print("Menu")
while True:
        menu=int(input("escoge una opcion: \n 1-persona , \n 2-vehiculos, \n 3-universidades, \n 4-notas, \n 5-salir, \n escoge: "))

        if menu == 1:
            print("has presionado la opcion persona")
            
        if menu == 2:
            print("has presionado la opcion vehiculos")
            
        if menu == 3:
            print("has presionado la opcion universidades")
            
        if menu == 4:
            print("has presionado la opcion notas")
            
        if menu == 5:
            print("saliendo") 
            break
        if menu >5 or menu <1:
            print("opcion no valida digite otra opcion")
            
        