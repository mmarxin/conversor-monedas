def conversor(tipo_pesos, valor_dolar):
    pesos = input(("¿cuantos pesos " + "tipo_pesos" + " tienes?:  "))
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print ("Tienes $" + dolares + " dolares")


menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

El número representa la opción de moneda.
Elije una opción: """

opción = input(menu)
print ("""""")
if opción == "1":
    conversor("Colombianos", 40000)
elif opción == "2":
    conversor("Argentinos", 65)
elif opción == "3":
    conversor("Mexicanos", 25)
else:
    print("Ingresa una opción valida por favor")


