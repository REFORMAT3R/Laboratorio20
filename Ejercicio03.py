while True:
    N = int(input("Ingrese N (>=3) o 0 para salir: "))
    
    if N == 0:
        print("Programa finalizado.")
        break

    if N < 3:
        print("Error: N debe ser mayor o igual a 3.\n")
        continue

    # Crear matriz NxN
    matriz = [[0]*N for _ in range(N)]

    num = 1
    top = 0
    bottom = N - 1
    left = 0
    right = N - 1

    while num <= N*N:
        # izquierda → derecha
        i = left
        while i <= right:
            matriz[top][i] = num
            num += 1
            i += 1
        top += 1

        # arriba → abajo
        i = top
        while i <= bottom:
            matriz[i][right] = num
            num += 1
            i += 1
        right -= 1

        # derecha → izquierda
        if top <= bottom:
            i = right
            while i >= left:
                matriz[bottom][i] = num
                num += 1
                i -= 1
            bottom -= 1

        # abajo → arriba
        if left <= right:
            i = bottom
            while i >= top:
                matriz[i][left] = num
                num += 1
                i -= 1
            left += 1

    print("\nMatriz en espiral:")
    for fila in matriz:
        print(fila)
    print("------------------------\n")