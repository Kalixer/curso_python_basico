def conversor(tipo_moneda, valor_dolar):
    dinero = input("Ingresa la cantidad de pesos " + tipo_moneda + " que quieres convetir: ")
    dinero = int(dinero)
    usd = valor_dolar
    dolares_cantidad = dinero / usd
    dolares_cantidad = round(dolares_cantidad, 2)
    dolares_cantidad = str(dolares_cantidad)
    print("El equivalente en dolares seria de $" + dolares_cantidad)

menu = """
Bienvenido al conversor de monedas 🌎

1 - Pesos chilenos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("chilenos", 950)

elif opcion == 2:
   conversor("argrentinos", 129.33)


elif opcion == 3:
    conversor("mexicanos", 20.33)


else: print("Ingresa una opcion valida")


