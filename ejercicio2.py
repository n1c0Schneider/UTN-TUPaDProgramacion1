#Ejercicio 2

usuario : str = "alumno"
clave : str = "python123"
intentos : int = 3

for intento in range(1, intentos + 1):
    usuario_input = input(f"Intento {intento}/{intentos} - Usuario: ").strip()
    clave_input = input("Clave: ").strip()
    
    if usuario_input == usuario and clave_input == clave:
        print("Acceso concedido.")
        while True:
            print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
            opcion = input("Opción: ").strip()
            
            if not opcion.isdigit():
                print("Error: ingrese un número válido")
                continue
            opcion_int = int(opcion)
            
            if opcion_int < 1 or opcion_int > 4:
                print("Error: opción fuera de rango")
                continue
            
            if opcion_int == 1:
                print("Inscripto")
                
            elif opcion_int == 2:
                nueva_clave = input("Ingrese nueva clave: ").strip()
                confirmacion_clave = input("Confirme nueva clave: ").strip()
                
                if len(nueva_clave) < 6:
                    print("Error: la nueva clave debe tener mínimo 6 caracteres")
                    continue
                
                if nueva_clave != confirmacion_clave:
                    print("Error: las claves no coinciden")
                    continue
                
                clave = nueva_clave
                print("Clave cambiada")
            elif opcion_int == 3:
                print("Vamos exitos!")
            elif opcion_int == 4:
                print("Saliendo del programa")
                break
        break
    else:
        print("Error: credenciales inválidas")
