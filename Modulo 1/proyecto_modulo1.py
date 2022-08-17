# Hacer ciclos en cada campo hasta que se capture un valor válido
while True:
    nombre = input("Ingrese su Nombre: ")
    # Validar que la cadena capturada no sea vacia
    if nombre != "":
        break
    # Continuar preguntando por el campo Nombre
    print('No se ingreso su Nombre. Debe ingresarlo para continuar')

while True:
    apellidoPaterno = input("Ingrese su Apellido Paterno: ")
    # Validar que la cadena capturada no sea vacia
    if apellidoPaterno != "":
        break
    # Continuar preguntando por el campo Apellido paterno
    print('No se ingreso su Apellido Paterno. Debe ingresarlo para continuar')

while True:
    apellidoMaterno = input("Ingrese su Apellido Materno: ")
    # Validar que la cadena capturada no sea vacia
    if apellidoMaterno != "":
        break
    # Continuar preguntando por el campo Apellido materno
    print('No se ingreso su Apellido Materno. Debe ingresarlo para continuar')

# Campos Numéricos
while True:
    edadCaptura = input("Ingrese su edad: ")
    # Validar que el dato capturado no sea una cadena vacia
    if edadCaptura == '':
        print('Debe ingresar un numero para su edad. Favor de volver a capturar')
    else:
        # Hacer un cast del valor capturado a un valor float
        edad = float(edadCaptura)
        # Validad que la edad sea mayor a cero
        if edad > 0:
            # Si es mayor, continuar con el siguiente campo
            break
        print('Debe ingresar un valor mayor a cero para continuar. Favor de volver a capturar')

while True:
    pesoCapturado = float(input("Ingrese su peso en kilogramos: "))
    # Validar que el dato capturado no sea una cadena vacia
    if pesoCapturado == '':
        print('Debe ingresar un valor en kilogramos. Favor de volver a capturar')
    # Hacer un cast del valor capturado a un valor float
    peso = float(pesoCapturado)
    # Validad que la edad sea mayor a cero
    if peso > 0:
        # Si es mayor a cero, continuar con el siguiente campo
        break
    print('Debe ingresar un valor mayor a cero para continuar. Favor de volver a capturar')

while True:
    estaturaCapturada = float(input("Ingrese su estatura en metros: "))
    # Validar que el dato capturado no sea una cadena vacía
    if estaturaCapturada == '':
        print('Debe capturar un valor en metros. Favor de volver a capturar')
    # Hacer cast del valor capturado a un valor float
    estatura = float(estaturaCapturada)
    if estatura > 0:
        # Si es mayor a cero, continuar con el proceso
        break
    print('Debe ingresar un valor mayor a cero para continuar. Favor de volver a capturar')

# Mostrar los datos de la persona capturada
print('Tu nombre es', nombre, apellidoPaterno, apellidoMaterno)
print(f'Tu edad es {edad:.0f}, tu peeso es {peso:.3f} y tu estatura es {estatura:.2f}')

# Calcular el IMC peso / (estatura2)
imc = peso / (estatura * estatura)

# Mostrar el resultado del cálculo
print(f'De acuerdo a la informacion proporcionada, tu IMC es {imc:.3f}')
