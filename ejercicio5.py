#Ejercicio 5
vida_jugador = 100 
vida_enemigo = 100 
pociones = 3       
ataque_pesado_base = 15 
danio_enemigo = 12      
turno_gladiador = True  

print("--- Bienvenido a la Arena ---")

# Validacion del nombre (Paso 1)
# Solo letras y no vacio usando isalpha() y while
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha() or nombre == "":
    print("Error: Solo se permiten letras y no puede estar vacio.")
    nombre = input("Nombre del Gladiador: ")

print("=== INICIO DEL COMBATE ===")

# Se repite mientras ambos tengan vida (HP > 0)
while vida_jugador > 0 and vida_enemigo > 0:
    
    # Mostrar estado actual de la batalla
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    
    print("Elige accion:")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")
    
    opcion = input("Opcion: ")
    
    # validacion del menu
    # debe ser numero y estar entre 1 y 3
    while not opcion.isdigit() or (opcion != "1" and opcion != "2" and opcion != "3"):
        print("Error: Ingrese un numero valido (1, 2 o 3).")
        opcion = input("Opcion: ")

    
    if opcion == "1":
        # accion A
        danio_final = float(ataque_pesado_base)
        
        # golpe Critico (si vida enemigo < 20)
        if vida_enemigo < 20:
            danio_final = ataque_pesado_base * 1.5 # resultado float
            print("¡GOLPE CRITICO!")
            
        vida_enemigo = vida_enemigo - danio_final
        print(f"¡Atacaste al enemigo por {danio_final} puntos de danio!")
        
    elif opcion == "2":
        # accion B
        print(">> ¡Inicias una rafaga de golpes!")
        for i in range(3):
            vida_enemigo = vida_enemigo - 5
            print("> Golpe conectado por 5 de danio")
            
    elif opcion == "3":
        # accion C
        if pociones > 0:
            vida_jugador = vida_jugador + 30

            if vida_jugador > 100:
                vida_jugador = 100
            pociones = pociones - 1
            print(f"Te has curado. Vida actual: {vida_jugador}. Pociones restantes: {pociones}")
        else:
            print("¡No quedan pociones! Pierdes el turno intentando buscar una.")
#turno enemigo
    if vida_enemigo > 0:
        vida_jugador = vida_jugador - danio_enemigo
        print(f">> ¡El enemigo te ataco por {danio_enemigo} puntos de danio!")

# resultados finales
if vida_jugador > 0:
    print("\n*********************************")
    print(f"¡Victoria! {nombre} ha ganado la batalla.")
    print("*********************************")
else:
    print("\n---------------------------------")
    print("Derrota.")
    print("---------------------------------")
