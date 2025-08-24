def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(int(vuelto))  
    print("Centavos:")
    print(int(round((vuelto - int(vuelto)) * 100))) 
change()