salario_base=1200
horas_extras=10
pago_hora_extra=15
bono=200
afp=10
salud=7

salario_bruto=salario_base+(horas_extras*pago_hora_extra)+bono
descuentos=(salario_base*afp/100)+(salario_base*salud/100)
salario_neto=salario_bruto-descuentos

print("Salario bruto:",salario_bruto)
print("Descuentos totales:",descuentos)
print("Salario neto:",salario_neto)