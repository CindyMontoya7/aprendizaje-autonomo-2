"""
Trabajo autónomo de cajero automático
Lenguaje: Python 3
"""
# ---------------------------------------------------------
# "BASE DE DATOS" del cajero
# La tarjeta es el mismo nombre de usuario.
# Cada usuario tiene: PIN de 4 dígitos y saldo inicial.
# UNIVERSIDAD INTERNACIONAL DEL ECUADOR
# CINDY MARGARITA MONTOYA
# MAYO 2026
# ---------------------------------------------------------

pin_cindy = "1234"
saldo_cindy = 1500.0

pin_juan = "4321"
saldo_juan = 800.0

pin_rafa = "5678"
saldo_rafa = 2300.0

pin_jean = "9876"
saldo_jean = 500.0

# ---------------------------------------------------------
# Variables de control
# ---------------------------------------------------------
tarjeta = input("Ingrese su tarjeta (usuario): ").strip().lower()

# Variables que vamos a usar según el usuario que inició sesión
pin_correcto = ""
autenticado = False
tarjeta_valida = False

# IF / ELIF / ELSE: identificamos si la tarjeta existe y cuál es su PIN correcto
if tarjeta == "cindy":
    pin_correcto = pin_cindy
    tarjeta_valida = True
elif tarjeta == "juan":
    pin_correcto = pin_juan
    tarjeta_valida = True
elif tarjeta == "rafa":
    pin_correcto = pin_rafa
    tarjeta_valida = True
elif tarjeta == "jean":
    pin_correcto = pin_jean
    tarjeta_valida = True
else:
    tarjeta_valida = False