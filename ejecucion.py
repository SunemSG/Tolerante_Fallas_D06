import pickle

# Guardar
def guardar_estado(archivo, estado):
    with open(archivo, 'wb') as f:
        pickle.dump(estado, f)

# Cargar
def cargar_estado(archivo):
    with open(archivo, 'rb') as f:
        estado = pickle.load(f)
    return estado

if __name__ == "__main__":
    estado_actual = {
        'contador': 1,
        'nombre': 'Archivo',
    }

    # Guardar el estado actual en un archivo
    guardar_estado('estado.pickle', estado_actual)

    # Cargar el estado desde el archivo
    estado_cargado = cargar_estado('estado.pickle')

    # Mostrar el estado cargado
    print("Estado cargado:")
    print(estado_cargado)
