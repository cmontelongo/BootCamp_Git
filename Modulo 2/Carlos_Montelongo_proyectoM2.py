from curses.ascii import isdigit


print("*" * 20)
print("Ejercicio #1")
print("*" * 20)
palabra = input("Ingresa una palabra: ")
numeroLetras = len(palabra)

if numeroLetras < 4:
    print(f"A la palabra '{palabra}' le faltan letras. Tiene {numeroLetras} letras.")
elif numeroLetras > 8:
    print(f"A la palabra '{palabra}' le sobran letras. Tiene {numeroLetras} letras.")
else:
    print(f"La palabra '{palabra}' es correcta.")

print()
print("*" * 20)
print("Ejercicio #2")
print("*" * 20)

while True:
    valorX = input("Ingresa el valor de X: ")
    if not valorX.lstrip('+-').isalnum():
        print("Valor de X es invalido")
        continue
    elif int(valorX) == 0:
        print("Valor de X debe ser distinto a cero.")
        continue
    else:
        valorX = int(valorX)
        break

while True:
    valorY = input("Ingresa el valor de Y: ")
    if not valorY.lstrip('+-').isalnum():
        print("Valor de Y es invalido")
        continue
    elif int(valorY) == 0:
        print("Valor de Y debe ser distinto a cero.")
        continue
    else:
        valorY = int(valorY)
        break

print(f"X= {valorX} , Y= {valorY}")


if ( (valorX > 0) & (valorY > 0) ):
    print("Cuadrante I")
elif ((valorX < 0) & (valorY > 0)):
    print("Cuadrante II")
elif ((valorX < 0) & (valorY < 0)):
    print("Cuadrante III")
elif ((valorX > 0) & (valorY < 0)):
    print("Cuadrante IV")
else:
    print("Desconocido")

print()
print("==> FIN DEL PROGRAMA <==")