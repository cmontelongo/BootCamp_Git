import requests as req
import json
import os
import errno
from PIL import Image
import urllib.request
# Se aprendió a importar librerias que me ayudan a manejar objetos dentro de python

# Indico el directorio donde guardaré los json encontrados
directorio = 'pokedex'

# Buscar que el directorio exista o sea accesible
try:
    CURR_DIR = os.path.dirname(os.path.realpath(__file__))
    os.mkdir(CURR_DIR+directorio)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

# Hacer un bucle infinito para pedir al menos un Pokémon por buscar
while (True):
    buscaPokemon = input("¿Que Pokémon deseas buscar? ")

    # Indicar la url dnde se podrá consultar la información del Pokémon indicado por el usuario,
    # ésta búsqueda se realiza con todas las letras en minúsculas, de lo contrario siempre marcará que no encuentra el personaje
    API_POKEMON = 'https://pokeapi.co/api/v2/pokemon/'+buscaPokemon.lower()

    # Invocar la url
    respuesta = req.get(API_POKEMON)

    # Validar cual es la respuesta del request, para validar si se podrá procesar o marcar mensaje de error
    if respuesta.status_code == 404 :
        print(f"NO se encontró al Pokémon {buscaPokemon}")
    elif respuesta.status_code != 200:
        print(f"ERROR al realizar la consulta del Pokémon {buscaPokemon}")
    else:
        # Por omisión se continúa con el procesamiento de los datos obtenidos del request
        informacionEncontrada = respuesta.json()
        try:
            # Intentar extraer la información de acuerdo al json recibido, 
            # si no existen los nodos esperados, marcará una excepción, pero se le indicará al usuario.
            peso = informacionEncontrada['weight']
            estatura = informacionEncontrada['height']
            listadoMovimientos = []     # Arreglo para almacenar los movimientos del Pokémon
            for mov in informacionEncontrada['moves']:
                listadoMovimientos.append(mov['move']['name'])
            listadoHabilidades = []     # Arreglo para almacenar las habilidades del Pokémon
            for hab in informacionEncontrada['abilities']:
                listadoHabilidades.append(hab['ability']['name'])
            url_imagen = informacionEncontrada['sprites']['front_default']  # URL de la imagen default del Pokémon
            continuar = True    # Se indica con valor TRUE para indicar que no hubo excepciones
        except:
            continuar = False
            print(f"ERROR al procesar la información del Pokémon {buscaPokemon}. Intente más tarde o con otro Pokémon.")

        if continuar:
            # Solo continuar si no hay excepción y la bandera está como TRUE
            #   lo que nos indica que sí se pudo procesar la información necesaria para el usuario
            # Mostrar en pantalla la información encontrada del Pokémon
            print(f"""
Nombre del Pokémon buscado: {buscaPokemon}
Su peso es de {peso}
Su estatura es de: {estatura}
Los movimientos pueden ser:""")
            for mov in listadoMovimientos:
                print(f"\t- {mov}")
            print("Sus habilidades son:")
            for hab in listadoHabilidades:
                print(f"\t- {hab}")

            # Generar como lectura un archivo con extensión Json,
            # se agregará todo el json encontrado desde la url que se consultó al inicio del proceso
            with open('./'+directorio+'/'+buscaPokemon+'.json', 'w') as f_agenda:
                json.dump(informacionEncontrada, f_agenda, indent=2)

            print(f"Datos guardados en {buscaPokemon}.json\n")

            # Mostrar la imágen encontrada del Pokémon consultado
            urllib.request.urlretrieve(url_imagen, "pokemon.png")
            img = Image.open("pokemon.png").resize((200,200))
            img.show()

    # Preguntar al usuario si desea realizar otra consulta
    siguiente = input("ATENCIÓN: ¿Desea consultar otro Pokémon (si ó no)? ")
    if siguiente.lower() != "si" and siguiente.lower() != "s":
        break
