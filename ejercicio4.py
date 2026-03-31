#Ejercicio 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0 

print("-Escape the room")

# validacion de nombre
nombre_agente = input("Ingrese su nombre de agente: ")
while not nombre_agente.isalpha() or nombre_agente == "":
    print("Error: El nombre debe contener solo letras y no estar vacio.")
    nombre_agente = input("Ingrese su nombre de agente: ")

# bucle principal
juego_activo = True

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and juego_activo:
    
    if alarma == True and tiempo <= 3:  # noqa: E712
        juego_activo = False
    else:
    
        print(f"\n--- ESTADO DE {nombre_agente.upper()} ---")
        print(f"Energía: {energia} | Tiempo: {tiempo} h | Cerraduras: {cerraduras_abiertas}/3")
        print(f"Alarma: {alarma} | Código: {codigo_parcial}")
        
        # Menú de acciones
        print("1. Forzar cerradura (-20 energía, -2 tiempo)")
        print("2. Hackear panel (-10 energía, -3 tiempo)")
        print("3. Descansar (+15 energía, -1 tiempo)")
        
        opcion = input("Elija una acción: ")
        
        while not opcion.isdigit() or (opcion != "1" and opcion != "2" and opcion != "3"):
            print("Error: Ingrese 1, 2 o 3.")
            opcion = input("Elija una acción: ")
        
        if opcion == "1":
    
            energia = energia - 20
            tiempo = tiempo - 2
            racha_forzar = racha_forzar + 1
            
            if racha_forzar >= 3:
                alarma = True
                print("Forzaste demasiado la cerradura. Alarma activada.")
            else:

                if energia < 40:
                    print("La energía es baja. Elija un numero de seguridad (1, 2 o 3):")
                    seguridad = input("> ")
                    while not seguridad.isdigit() or (seguridad != "1" and seguridad != "2" and seguridad != "3"):
                        seguridad = input("Opción inválida. Elija 1, 2 o 3: ")
                    
                    if seguridad == "3":
                        alarma = True
                        print("Perdiste! Activaste los sensores de movimiento.")
                
                if alarma == False:  # noqa: E712
                    cerraduras_abiertas = cerraduras_abiertas + 1
                    print("Una cerradura se ha abierto.")

        elif opcion == "2":
            # Hack al panel
            energia = energia - 10
            tiempo = tiempo - 3
            racha_forzar = 0 
            
            print("Iniciando hackeo...")
            # Bucle for de 4 pasos
            for i in range(4):
                codigo_parcial = codigo_parcial + "A"
                print(f"Descifrando: {codigo_parcial}")
            
            if len(codigo_parcial) >= 8:
                if cerraduras_abiertas < 3:
                    cerraduras_abiertas = cerraduras_abiertas + 1
                    print("¡Hackeo completado! Se abrió una cerradura remotamente.")

        elif opcion == "3":
            
            racha_forzar = 0 
            tiempo = tiempo - 1
            
            recuperacion = 15
            if alarma == True:  # noqa: E712
                recuperacion = recuperacion - 10
                print("Es difícil descansar con el ruido de la alarma...")
            
            energia = energia + recuperacion
    
            if energia > 100:
                energia = 100
            print(f"Has recuperado energía. Ahora tenés {energia}.")

# condiciones

if cerraduras_abiertas >= 3:
    print("\n*********************************")
    print(f"¡VICTORIA! {nombre_agente} logró abrir la bóveda.")
    print("*********************************")
elif alarma == True and tiempo <= 3:  # noqa: E712
    print("\n---------------------------------")
    print("DERROTA: El sistema se bloqueó por la alarma.")
    print("---------------------------------")
else:
    print("\n---------------------------------")
    print("DERROTA: Te quedaste sin tiempo o energía.")
    print(f"Estado final -> Energía: {energia}, Tiempo: {tiempo}")
    print("---------------------------------")