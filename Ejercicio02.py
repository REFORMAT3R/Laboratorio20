while True:
    ingreso_mensual=float(input("Ingrese ingreso mensual (0 para salir): "))
    if ingreso_mensual==0:
        print("Programa finalizado.")
        break

    # 12 sueldos + 2 aguinaldos
    ingreso_anual=ingreso_mensual*14
    restante=ingreso_anual

    # Tramo 1: [0 – 20000] a 0%
    if restante > 20000:
        tramo1 = 20000
    else:
        tramo1 = restante
    imp1 = tramo1 * 0
    restante -= tramo1

    # Tramo 2: (20000 – 50000] a 10%
    if restante > 0:
        if restante > 30000:    # 50000 - 20000
            tramo2 = 30000
        else:
            tramo2 = restante
        imp2 = tramo2 * 0.10
        restante -= tramo2
    else:
        tramo2 = 0
        imp2 = 0

    # Tramo 3: (50000 – 100000] a 20%
    if restante > 0:
        if restante > 50000:    # 100000 - 50000
            tramo3 = 50000
        else:
            tramo3 = restante
        imp3 = tramo3 * 0.20
        restante -= tramo3
    else:
        tramo3 = 0
        imp3 = 0

    # Tramo 4: >100000 a 30%
    if restante > 0:
        tramo4 = restante
        imp4 = tramo4 * 0.30
    else:
        tramo4 = 0
        imp4 = 0

    total_impuesto = imp1 + imp2 + imp3 + imp4
    tasa_efectiva = (total_impuesto / ingreso_anual) * 100

    print("\n--- RESULTADOS ---")
    print("Ingreso anual:", ingreso_anual)
    print("Impuesto tramo 1 (0%):", imp1)
    print("Impuesto tramo 2 (10%):", imp2)
    print("Impuesto tramo 3 (20%):", imp3)
    print("Impuesto tramo 4 (30%):", imp4)
    print("TOTAL impuesto:", total_impuesto)
    print("Tasa efectiva (%):", tasa_efectiva)
    print("------------------\n")