import numpy as np

def normalizar_np(lista, modo):
    datos = np.array(lista, dtype=float)

    if modo not in ("minmax", "zscore", "unit"):
        return None

    if modo == "minmax":
        minimo = datos.min()
        maximo = datos.max()
        if maximo - minimo == 0:
            return np.zeros_like(datos).tolist()
        return ((datos - minimo) / (maximo - minimo)).tolist()

    elif modo == "zscore":
        media = datos.mean()
        des = datos.std()
        if des == 0:
            return np.zeros_like(datos).tolist()
        return ((datos - media) / des).tolist()

    elif modo == "unit":
        norma = np.linalg.norm(datos)
        if norma == 0:
            return np.zeros_like(datos).tolist()
        return (datos / norma).tolist()

# -----------------------------
# NORMALIZADOR
# -----------------------------

print("=== Normalizador con NumPy ===")
print("Modos disponibles: minmax, zscore, unit")
print("Escribe 'salir' para terminar.\n")

while True:

    modo = input("Modo de normalización: ")

    if modo == "salir":
        print("Programa finalizado.")
        break

    if modo not in ("minmax", "zscore", "unit"):
        print("Modo inválido.\n")
        continue

    texto = input("Ingresa números separados por espacios: ")

    partes = texto.split()
    lista = []

    valido = True
    for p in partes:
        if p.replace(".", "", 1).lstrip("+-").isdigit():
            lista.append(float(p))
        else:
            valido = False
            break

    if not valido:
        print("Entrada inválida.\n")
        continue

    resultado = normalizar_np(lista, modo)

    print("Resultado:", resultado)
    print("Original:", lista, "\n")