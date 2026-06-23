"""
Simulación de cajero automático
Lenguaje: Python 3
"""

# ---------------------------------------------------------
# "BASE DE DATOS" del cajero
# La tarjeta es el mismo nombre de usuario.
# Cada usuario tiene: PIN de 4 dígitos y saldo inicial.
# ---------------------------------------------------------
usuarios = {
    "cindy": {"pin": "1234", "saldo": 1500.0},
    "juan":  {"pin": "4321", "saldo": 800.0},
    "rafa":  {"pin": "5678", "saldo": 2300.0},
    "jean":  {"pin": "9876", "saldo": 500.0},
}

MAX_INTENTOS = 3  # intentos permitidos para ingresar el PIN

