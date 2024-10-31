def proyecto():
        
        clientes = []
        # Entrada de datos para 3 clientes
        for i in range(3):
                print(f"Ingrese los datos para el Cliente {i + 1}:")
                nombre = input("Nombre: ")
                numero_cuenta = input("Número de Cuenta: ")
                deuda = float(input("Monto de la Deuda: "))

                # Cálculos
                MI = (deuda * 30) // 100  # Monto de Interés, división entera
                DI = deuda + MI           # Deuda más Interés
                PM = DI // 12             # Pago Mínimo, división entera

                # Almacenar los datos del cliente en un diccionario
                cliente = {
                        "nombre": nombre,
                        "numero_cuenta": numero_cuenta,
                        "deuda": deuda,
                        "monto_interes": MI,
                        "deuda_total": DI,
                        "pago_minimo": PM
                }

                # Agregar el diccionario al arreglo de clientes
                clientes.append(cliente)

        # Salida de datos y cálculos
        print("\nDatos y Cálculos de los Clientes:")
        for i, cliente in enumerate(clientes):
                print(f"\nCliente {i + 1}:")
                print(f"Nombre: {cliente['nombre']}")
                print(f"Número de Cuenta: {cliente['numero_cuenta']}")
                print(f"Deuda Original: {cliente['deuda']}")
                print(f"Monto de Interés (MI): {cliente['monto_interes']}")
                print(f"Deuda Total con Interés (DI): {cliente['deuda_total']}")
                print(f"Pago Mínimo Mensual: {cliente['pago_minimo']}")
proyecto()