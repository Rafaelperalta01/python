import requests
from colorama import Fore, Style, init

init()

def obtener_peliculas_populares(api_key):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=es'
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos['results']

def obtener_generos(api_key):
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=es'
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos['genres']

def obtener_recomendaciones(api_key, genero):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=es&with_genres={genero}&sort_by=popularity.desc'
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos['results']

def imprimir_mensaje(mensaje, tipo):
    if tipo == 'usuario':
        print(f'{Fore.BLUE}{Style.BRIGHT}Usuario:{Style.RESET_ALL} {mensaje}')
    elif tipo == 'bot':
        print(f'{Fore.GREEN}{Style.BRIGHT}Bot:{Style.RESET_ALL} {mensaje}')

def main():
    api_key = "d77211d2c77e44c43e8a33695143e35f"  # Reemplaza con tu API Key

    generos = obtener_generos(api_key)
    imprimir_mensaje("Opciones de Género:", 'bot')
    for genero in generos:
        imprimir_mensaje(f"{genero['id']}: {genero['name']}", 'bot')

    genero_preferido = int(input(f'{Fore.BLUE}{Style.BRIGHT}Usuario:{Style.RESET_ALL} Por favor, elige el número correspondiente al género que te gusta: '))

    peliculas_populares = obtener_peliculas_populares(api_key)
    imprimir_mensaje("\nPelículas Populares:", 'bot')
    for pelicula in peliculas_populares:
        imprimir_mensaje(pelicula['title'], 'bot')

    imprimir_mensaje(f"\nRecomendaciones basadas en tu género preferido ({genero_preferido}):", 'bot')
    recomendaciones = obtener_recomendaciones(api_key, genero_preferido)
    for pelicula in recomendaciones:
        imprimir_mensaje(pelicula['title'], 'bot')

if __name__ == '__main__':
    main()
