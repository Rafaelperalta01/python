filename = 'Prueba.txt'

try:
    with open('./Textos/' + filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "El archivo " + filename + " no existe"
    print(msg)
else:
    palabras = contents.split()
    num_palabras = len(palabras)
    print("El archivo " + filename + " contiene: " + str( num_palabras) + " palabras")