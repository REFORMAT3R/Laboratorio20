def normalizar(lista, modo):
    # Crear copia
    datos = lista[:]

    # Validar modo
    if modo not in ("minmax", "zscore", "unit"):
        return None  

    # Calcular valores básicos
    minimo = min(datos)
    maximo = max(datos)
    media = sum(datos) / len(datos)

    # Desviación estándar
    suma = 0
    for x in datos:
        suma += (x - media) ** 2
    desviacion = (suma / len(datos)) ** 0.5

    # Norma del vector (unit)
    norma = 0
    for x in datos:
        norma += x ** 2
    norma = norma ** 0.5

    # Normalizaciones
    resultado = []

    if modo == "minmax":
        if maximo - minimo == 0:
            return [0 for _ in datos]
        for x in datos:
            resultado.append((x - minimo) / (maximo - minimo))

    elif modo == "zscore":
        if desviacion == 0:
            return [0 for _ in datos]
        for x in datos:
            resultado.append((x - media) / desviacion)

    elif modo == "unit":
        if norma == 0:
            return [0 for _ in datos]
        for x in datos:
            resultado.append(x / norma)

    return resultado

# -----------------------------
# NORMALIZADOR
# -----------------------------

print("=== Normalizador de listas ===")
print("Modos: minmax, zscore, unit")
print("Escribe 'salir' para terminar.\n")

while True:

    modo = input("Modo de normalización: ")

    if modo == "salir":
        print("Programa finalizado.")
        break

    # si el modo no es válido, repetir
    if modo not in ("minmax", "zscore", "unit"):
        print("Modo inválido\n")
        continue

    # pedir lista
    texto = input("Ingresa números separados por espacios: ")

    # convertir manualmente 
    partes = texto.split()
    lista = []

    # Validación básica 
    es_valida = True
    for p in partes:
        if p.replace(".", "", 1).lstrip("+-").isdigit():
            lista.append(float(p))
        else:
            es_valida = False
            break

    if not es_valida:
        print("Entrada inválida, intenta otra vez.\n")
        continue

    resultado = normalizar(lista, modo)

    print("Resultado:", resultado)
    print("Original:", lista, "\n")