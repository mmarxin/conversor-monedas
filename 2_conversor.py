def conversor(tipo_pesos, valor_dolar):
    pesos = input(("驴cuantos pesos " + "tipo_pesos" + " tienes?:  "))
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print ("Tienes $" + dolares + " dolares")


menu = """
Bienvenido al conversor de monedas 馃挵

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

El n煤mero representa la opci贸n de moneda.
Elije una opci贸n: """

opci贸n = input(menu)
print ("""""")
if opci贸n == "1":
    conversor("Colombianos", 40000)
elif opci贸n == "2":
    conversor("Argentinos", 65)
elif opci贸n == "3":
    conversor("Mexicanos", 25)
else:
    print("Ingresa una opci贸n valida por favor")


