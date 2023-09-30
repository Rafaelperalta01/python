from flask import Flask, render_template, request
from google.cloud import translate
import os
app = Flask(__name__)

# Configura tu clave de API de Google Cloud Translation
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'first-outlet-363914-dcad0c58a6da.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    texto = request.form['texto']
    idioma_origen = request.form['idioma_origen']
    idioma_destino = request.form['idioma_destino']

    # Inicia el cliente de Google Cloud Translation
    client = translate.TranslationServiceClient()

    # Construye la solicitud de traducción
    parent = f"projects/first-outlet-363914"  # Reemplaza con tu ID de proyecto
    response = client.translate_text(
        parent=parent,
        contents=[texto],
        mime_type="text/plain",
        source_language_code=idioma_origen,
        target_language_code=idioma_destino,
    )

    # Obtiene la traducción
    traduccion = response.translations[0].translated_text
    
    return render_template('index.html', texto=texto, traduccion=traduccion, idioma_origen=idioma_origen, idioma_destino=idioma_destino)

if __name__ == '__main__':
    app.run(debug=True)
def obtener_codigo_idioma(nombre_idioma):
    # Mapeo de nombres de idiomas a códigos de idioma
    mapeo_idiomas = {
        'español': 'es',
        'inglés': 'en'
        # Agrega más idiomas y sus códigos según sea necesario
    }

    # Convertir a minúsculas y eliminar espacios extras
    nombre_idioma = nombre_idioma.lower().strip()

    # Obtener el código del idioma si está en el mapeo
    codigo_idioma = mapeo_idiomas.get(nombre_idioma)

    return codigo_idioma
codigo_espanol = obtener_codigo_idioma('español')  # Devuelve 'es'
codigo_ingles = obtener_codigo_idioma('inglés')  # Devuelve 'en'
codigo_frances = obtener_codigo_idioma('francés')  # Devuelve None (ya que no está en el mapeo)
