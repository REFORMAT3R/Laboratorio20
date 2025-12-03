ingreso_mensual=float(input("Ingreso mensual: "))
ingreso_anual=ingreso_mensual*14

# Tramos
lim1=20000
lim2=50000
lim3=100000

imp1=imp2=imp3=imp4=0
restante=ingreso_anual

# Tramo 1: [0 - 20000], 0%
if restante>0:
    tramo=min(restante,lim1)
    imp1=tramo*0
    restante-=tramo

# Tramo 2: (20000 - 50000], 10%
if restante>0:
    tramo=min(restante,lim2-lim1)
    imp2=tramo*0.10
    restante-=tramo

# Tramo 3: (50000 - 100000], 20%
if restante>0:
    tramo=min(restante,lim3-lim2)
    imp3=tramo*0.20
    restante-=tramo

# Tramo 4: >100000, 30%
if restante>0:
    imp4=restante*0.30

total_imp=imp1+imp2+imp3+imp4
tasa_efectiva=(total_imp/ingreso_anual)*100

print("Ingreso anual:",ingreso_anual)
print("Impuesto tramo 1:",imp1)
print("Impuesto tramo 2:",imp2)
print("Impuesto tramo 3:",imp3)
print("Impuesto tramo 4:",imp4)
print("Total impuesto:",total_imp)
print("Tasa efectiva real:",tasa_efectiva,"%")