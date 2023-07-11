import requests

def obtener_clima(ciudad):
    # clave de API de OpenWeatherMap
    api_key = '...'

    # solicitud a la API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"
    response = requests.get(url)
    datos_clima = response.json()

    # Datos del clima
    if datos_clima['cod'] == '404':
        print("Ciudad no encontrada.")
    else:
        clima_actual = datos_clima['weather'][0]['description']
        temperatura = datos_clima['main']['temp']
        humedad = datos_clima['main']['humidity']
        velocidad_viento = datos_clima['wind']['speed']
        nubes = datos_clima['clouds']['all']
        hora = datos_clima['dt']

        print(f"En {ciudad}:")
        print(f"Clima actual: {clima_actual}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Humedad: {humedad}%")
        print(f"Velocidad del viento: {velocidad_viento} m/s")
        print(f"Cobertura de nubes: {nubes}%")
        print(f"Hora local: {hora}")

        if 'rain' in datos_clima:
            print("Está lloviendo.")
        elif 'sun' in datos_clima:
            print("Hace sol.")

# Pedir una ciudad
ciudad = input("Ingrese el nombre de la ciudad: ")

# Llamo a la función para mostrar los datos
obtener_clima(ciudad)
