"""
Simulación de cajero automático
Lenguaje: Python 3
Versión simple: todo el código está en un solo bloque,
sin funciones y sin listas ni diccionarios.
Cada usuario es un conjunto de variables independientes.
"""

# ---------------------------------------------------------
# Datos quemados de cada usuario (la tarjeta es el usuario)
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

# ---------------------------------------------------------
# Validación del PIN (máximo 3 intentos) usando WHILE
# ---------------------------------------------------------
intentos = 0

if tarjeta_valida == True:
    while intentos < 3 and autenticado == False:
        pin_ingresado = input("Ingrese su PIN (4 dígitos): ").strip()
        intentos = intentos + 1

        if pin_ingresado == pin_correcto:
            autenticado = True
            print("\nBienvenido(a), " + tarjeta.capitalize() + ".\n")
        else:
            if intentos < 3:
                print("PIN incorrecto. Le quedan " + str(3 - intentos) + " intento(s).\n")
            else:
                print("Ha superado el número de intentos permitidos. Tarjeta bloqueada.\n")
else:
    print("Tarjeta no reconocida. Operación cancelada.\n")

# ---------------------------------------------------------
# Menú principal (solo si la autenticación fue correcta)
# Usamos DO WHILE (simulado con while True + break)
# ---------------------------------------------------------
if autenticado == True:

    salir = False

    while salir == False:  # equivale a un DO WHILE: el menú se muestra al menos una vez

        print("----- MENÚ CAJERO -----")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Cambiar PIN")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()
        print()

        # SWITCH (en Python se llama MATCH): dirige cada opción del menú
        match opcion:

            case "1":
                # Consultar saldo: solo mostramos el valor según el usuario
                if tarjeta == "cindy":
                    print("Su saldo disponible es: $" + str(saldo_cindy) + "\n")
                elif tarjeta == "juan":
                    print("Su saldo disponible es: $" + str(saldo_juan) + "\n")
                elif tarjeta == "rafa":
                    print("Su saldo disponible es: $" + str(saldo_rafa) + "\n")
                elif tarjeta == "jean":
                    print("Su saldo disponible es: $" + str(saldo_jean) + "\n")

            case "2":
                # Depositar dinero: DO WHILE hasta ingresar un monto válido
                monto_valido = False

                while monto_valido == False:
                    monto_texto = input("Ingrese el monto a depositar: ")

                    if monto_texto.replace(".", "", 1).isdigit() == False:
                        print("Debe ingresar un valor numérico válido.\n")
                    else:
                        monto = float(monto_texto)

                        if monto <= 0:
                            print("El monto debe ser mayor a cero.\n")
                        else:
                            # IF/ELIF para saber a qué saldo sumarle el depósito
                            if tarjeta == "cindy":
                                saldo_cindy = saldo_cindy + monto
                                print("Depósito exitoso. Nuevo saldo: $" + str(saldo_cindy) + "\n")
                            elif tarjeta == "juan":
                                saldo_juan = saldo_juan + monto
                                print("Depósito exitoso. Nuevo saldo: $" + str(saldo_juan) + "\n")
                            elif tarjeta == "rafa":
                                saldo_rafa = saldo_rafa + monto
                                print("Depósito exitoso. Nuevo saldo: $" + str(saldo_rafa) + "\n")
                            elif tarjeta == "jean":
                                saldo_jean = saldo_jean + monto
                                print("Depósito exitoso. Nuevo saldo: $" + str(saldo_jean) + "\n")

                            monto_valido = True  # condición de salida del do while

            case "3":
                # Retirar dinero: DO WHILE hasta que el retiro sea válido
                retiro_valido = False

                while retiro_valido == False:
                    monto_texto = input("Ingrese el monto a retirar: ")

                    if monto_texto.replace(".", "", 1).isdigit() == False:
                        print("Debe ingresar un valor numérico válido.\n")
                    else:
                        monto = float(monto_texto)

                        # Obtenemos el saldo actual del usuario según corresponda
                        if tarjeta == "cindy":
                            saldo_actual = saldo_cindy
                        elif tarjeta == "juan":
                            saldo_actual = saldo_juan
                        elif tarjeta == "rafa":
                            saldo_actual = saldo_rafa
                        elif tarjeta == "jean":
                            saldo_actual = saldo_jean

                        # IF / ELIF / ELSE: validamos monto y saldo suficiente
                        if monto <= 0:
                            print("El monto debe ser mayor a cero.\n")
                        elif monto > saldo_actual:
                            print("Saldo insuficiente para realizar el retiro.\n")
                        else:
                            if tarjeta == "cindy":
                                saldo_cindy = saldo_cindy - monto
                                print("Retiro exitoso. Nuevo saldo: $" + str(saldo_cindy) + "\n")
                            elif tarjeta == "juan":
                                saldo_juan = saldo_juan - monto
                                print("Retiro exitoso. Nuevo saldo: $" + str(saldo_juan) + "\n")
                            elif tarjeta == "rafa":
                                saldo_rafa = saldo_rafa - monto
                                print("Retiro exitoso. Nuevo saldo: $" + str(saldo_rafa) + "\n")
                            elif tarjeta == "jean":
                                saldo_jean = saldo_jean - monto
                                print("Retiro exitoso. Nuevo saldo: $" + str(saldo_jean) + "\n")

                            retiro_valido = True  # condición de salida del do while

            case "4":
                # Cambiar PIN: DO WHILE hasta que el nuevo PIN sea válido y coincida
                pin_actualizado = False

                while pin_actualizado == False:
                    nuevo_pin = input("Ingrese el nuevo PIN (4 dígitos): ").strip()
                    confirmar_pin = input("Confirme el nuevo PIN: ").strip()

                    if nuevo_pin.isdigit() == False or len(nuevo_pin) != 4:
                        print("El PIN debe tener exactamente 4 dígitos numéricos.\n")
                    elif nuevo_pin != confirmar_pin:
                        print("Los PIN ingresados no coinciden. Intente de nuevo.\n")
                    else:
                        # Actualizamos el PIN según el usuario autenticado
                        if tarjeta == "cindy":
                            pin_cindy = nuevo_pin
                        elif tarjeta == "juan":
                            pin_juan = nuevo_pin
                        elif tarjeta == "rafa":
                            pin_rafa = nuevo_pin
                        elif tarjeta == "jean":
                            pin_jean = nuevo_pin

                        print("PIN actualizado correctamente.\n")
                        pin_actualizado = True  # condición de salida del do while

            case "5":
                print("Gracias por usar el cajero. ¡Hasta luego!\n")
                salir = True  # condición que rompe el while principal

            case _:
                # "_" representa el caso por defecto (default) del switch
                print("Opción no válida. Intente nuevamente.\n")

else:
    if tarjeta_valida == True:
        print("No fue posible iniciar sesión. Programa finalizado.")