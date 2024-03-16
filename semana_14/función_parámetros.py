# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado al monto total de la compra.

    Parámetros:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float): El porcentaje de descuento a aplicar (por defecto 10%).

    Retorna:
        float: El monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamada a la función con diferentes precios de compra
monto_compra1 = 99.99
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

print('\n  Resultados: 1 ')
print(f" Monto total de compra realizado es: ${monto_compra1}")
print(f" Descuento aplicado es: ${descuento1:.2f}")
print(f" Monto final a pagar por el cliente es: ${monto_final1:.2f}")

# Llamada a la función con otro precio de compra y un porcentaje de descuento específico
monto_compra2 = 199.50
porcentaje_descuento2 = 20
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final_2 = monto_compra2 - descuento2

print('\n Resultados: 2 ')
print(f" Monto total de compra realizado es: ${monto_compra2}")
print(f" Porcentaje de descuento es: {porcentaje_descuento2}%")
print(f" Descuento aplicado es: ${descuento2:.2f}")
print(f" Monto final a pagar por el cliente es: ${monto_final_2:.2f}")

print('\n')
