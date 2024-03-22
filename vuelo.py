vuelo = {
    "Aerolinea": "Avianca",
    "Vuelo": "AV3102",
    "Origen": "CTG",
    "Destino": "MDE",
    "Tipo_Maleta": ['Cabina', 'Mano', 'Bodega']
}

print("Valores del diccionario:")
for key, value in vuelo.items():
    print(f"{key}: {value}")

print("\nValores de Tipo_Maleta:")
for maleta in vuelo["Tipo_Maleta"]:
    print(maleta)