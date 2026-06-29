"""
Trabajo autónomo de cajero automático
Lenguaje: Python 3
"""
# Datos de cada usuario: su PIN y su saldo
# UNIVERSIDAD INTERNACIONAL DEL ECUADOR
# CINDY MARGARITA MONTOYA
# JUNIO 2026

pin_cindy = "1234"
saldo_cindy = 1500.0

pin_juan = "4321"
saldo_juan = 800.0

pin_rafa = "5678"
saldo_rafa = 2300.0

pin_jean = "9876"
saldo_jean = 500.0

# Tupla con los usuarios que existen en el cajero
# (uso tupla porque estos nombres no cambian en el programa)
usuarios_validos = ("cindy", "juan", "rafa", "jean")

print("UNIVERSIDAD INTERNACIONAL DEL ECUADOR")
print("CINDY MARGARITA MONTOYA")
print("JUNIO 2026")
print("----- BIENVENIDO AL CAJERO AUTOMÁTICO -----\n")
tarjeta = input("Hola buen día, por favor ingrese su tarjeta (usuario): ").strip().lower()

pin_correcto = ""
autenticado = False
tarjeta_valida = False

# Con "in" reviso si lo que escribió el usuario está dentro de la tupla
if tarjeta in usuarios_validos:
    tarjeta_valida = True
else:
    tarjeta_valida = False

# Si la tarjeta existe, busco cuál es su PIN correcto
if tarjeta_valida == True:
    if tarjeta == "cindy":
        pin_correcto = pin_cindy
    elif tarjeta == "juan":
        pin_correcto = pin_juan
    elif tarjeta == "rafa":
        pin_correcto = pin_rafa
    elif tarjeta == "jean":
        pin_correcto = pin_jean

# Pido el PIN hasta 3 veces como máximo
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

# Menú del cajero, solo entra si el usuario ya inició sesión
if autenticado == True:

    salir = False

    while salir == False:  # el menú se muestra al menos una vez
        print("----- MENÚ CAJERO -----")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Cambiar PIN")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()
        print()

        match opcion:

            case "1":
                # Solo muestro el saldo del usuario que inició sesión
                if tarjeta == "cindy":
                    print("Su saldo disponible es: $" + str(saldo_cindy) + "\n")
                elif tarjeta == "juan":
                    print("Su saldo disponible es: $" + str(saldo_juan) + "\n")
                elif tarjeta == "rafa":
                    print("Su saldo disponible es: $" + str(saldo_rafa) + "\n")
                elif tarjeta == "jean":
                    print("Su saldo disponible es: $" + str(saldo_jean) + "\n")

            case "2":
                # Pido el monto hasta que sea válido
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
                            # Sumo el monto al saldo del usuario que inició sesión
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

                            monto_valido = True

            case "3":
                # Pido el monto hasta que el retiro sea válido
                retiro_valido = False

                while retiro_valido == False:
                    monto_texto = input("Ingrese el monto a retirar: ")

                    if monto_texto.replace(".", "", 1).isdigit() == False:
                        print("Debe ingresar un valor numérico válido.\n")
                    else:
                        monto = float(monto_texto)

                        # Reviso el saldo del usuario que inició sesión
                        if tarjeta == "cindy":
                            saldo_actual = saldo_cindy
                        elif tarjeta == "juan":
                            saldo_actual = saldo_juan
                        elif tarjeta == "rafa":
                            saldo_actual = saldo_rafa
                        elif tarjeta == "jean":
                            saldo_actual = saldo_jean

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

                            retiro_valido = True

            case "4":
                # Pido el nuevo PIN hasta que sea válido y coincida con la confirmación
                pin_actualizado = False

                while pin_actualizado == False:
                    nuevo_pin = input("Ingrese el nuevo PIN (4 dígitos): ").strip()
                    confirmar_pin = input("Confirme el nuevo PIN: ").strip()

                    if nuevo_pin.isdigit() == False or len(nuevo_pin) != 4:
                        print("El PIN debe tener exactamente 4 dígitos numéricos.\n")
                    elif nuevo_pin != confirmar_pin:
                        print("Los PIN ingresados no coinciden. Intente de nuevo.\n")
                    else:
                        # Guardo el nuevo PIN del usuario que inició sesión
                        if tarjeta == "cindy":
                            pin_cindy = nuevo_pin
                        elif tarjeta == "juan":
                            pin_juan = nuevo_pin
                        elif tarjeta == "rafa":
                            pin_rafa = nuevo_pin
                        elif tarjeta == "jean":
                            pin_jean = nuevo_pin

                        print("PIN actualizado correctamente.\n")
                        pin_actualizado = True

            case "5":
                print("Gracias por usar el cajero. ¡Hasta luego!\n")
                salir = True

            case _:
                # Cualquier otra opción que no sea del 1 al 5
                print("Opción no válida. Intente nuevamente.\n")

else:
    if tarjeta_valida == True:
        print("No fue posible iniciar sesión. Programa finalizado.")
