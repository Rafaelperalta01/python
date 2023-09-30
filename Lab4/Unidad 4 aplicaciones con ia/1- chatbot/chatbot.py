import requests

def obtener_clima(ciudad, pais, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={api_key}&units=metric'
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos

def main():
    api_key = "ec4ecff568c4a417dbbb6879e615afd0"

    while True:
        ciudad = input("Ingresa el nombre de la ciudad (o escribe 'salir' para salir): ")
        if ciudad.lower() == 'salir':
            break
        pais = input("Ingresa el nombre del país: ")
        datos_clima = obtener_clima(ciudad, pais, api_key)

        if datos_clima['cod'] == '404':
            print(f"No se pudo encontrar la ciudad de {ciudad}, {pais}")
        else:
            clima = datos_clima['weather'][0]['description']
            temperatura = datos_clima['main']['temp']
            print(f'El clima en {ciudad}, {pais} es {clima} con una temperatura de {temperatura}°C.')

if __name__ == '__main__':
    main()
