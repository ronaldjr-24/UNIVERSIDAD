# Diccionario con información personal
informacion_personal = {
    "Nombre": "Ronald Salazar",
    "Edad": 24,
    "Ciudad": "Napo-Archidona",
    "Profesion": "estudiando tecnología de la información "
}

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregarla con un número de teléfono ficticio
    informacion_personal["Telefono"] = "+593-0984495905"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Información personal:")
for key in informacion_personal:
    print(f"{key}: {informacion_personal[key]}")