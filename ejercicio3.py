#Ejercicio 3

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

while True:
    operador = input("ingrese el nombre del operador: ").strip()
    if not operador.isalpha():
        print("Error: el nombre del operador debe contener solo letras.")
        continue
    break
while True:
    print("\n1) Reservar turno  2) Cancelar turno  3) Ver agenda del día  4) Ver resumen general  5) Cerrar sistema")
    opcion = input("Opción: ").strip()
    
    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue
    opcion_int = int(opcion)
    
    if opcion_int < 1 or opcion_int > 5:
        print("Error: opción fuera de rango.")
        continue
    
    if opcion_int == 1:
        # elegir dia!
        while True:
            dia = input("Elegir día (1=Lunes, 2=Martes): ").strip()
            if dia not in ['1', '2']:
                print("Error: ingrese 1 para Lunes o 2 para Martes.")
                continue
            break
        # pedir nombre del paciente
        while True:
            paciente = input("Ingrese el nombre del paciente: ").strip()
            if not paciente.isalpha():
                print("Error: el nombre del paciente debe contener solo letras.")
                continue
            break
        # verificar que no esté repetido en ese día
        if dia == '1':
            if paciente in [lunes1, lunes2, lunes3, lunes4]:
                print("Error: el paciente ya tiene un turno reservado el Lunes.")
                continue
            if lunes1 == "":
                lunes1 = paciente
            elif lunes2 == "":
                lunes2 = paciente
            elif lunes3 == "":
                lunes3 = paciente
            elif lunes4 == "":
                lunes4 = paciente
            else:
                print("Error: no hay turnos disponibles el Lunes.")
        else: 
            if paciente in [martes1, martes2, martes3]:
                print("Error: el paciente ya tiene un turno reservado el Martes.")
                continue
            if martes1 == "":
                martes1 = paciente
            elif martes2 == "":
                martes2 = paciente
            elif martes3 == "":
                martes3 = paciente
            else:
                print("Error: no hay turnos disponibles el Martes.")
        pass
    elif opcion_int == 2:
        # Logica para cancelar turno
        while True:
            dia = input("Elegir día para cancelar (1=Lunes, 2=Martes): ").strip()
            if dia not in ['1', '2']:
                print("Error: ingrese 1 para Lunes o 2 para Martes.")
                continue
            break
        while True:
            paciente = input("Ingrese el nombre del paciente: ").strip()
            if not paciente.isalpha():
                print("Error: el nombre del paciente debe contener solo letras.")
                continue
            break
        if dia == '1':
            if paciente == lunes1:
                lunes1 = ""
            elif paciente == lunes2:
                lunes2 = ""
            elif paciente == lunes3:
                lunes3 = ""
            elif paciente == lunes4:
                lunes4 = ""
            else:
                print("Error: el paciente no tiene un turno reservado el Lunes.")
        else:
            if paciente == martes1:
                martes1 = ""
            elif paciente == martes2:
                martes2 = ""
            elif paciente == martes3:
                martes3 = ""
            else:
                print("Error: el paciente no tiene un turno reservado el Martes.")
        pass
    elif opcion_int == 3:
        # Logica para ver agenda del día
            while True:
                dia = input("Elegir día para ver agenda (1=Lunes, 2=Martes): ").strip()
                if dia not in ['1', '2']:
                    print("Error: ingrese 1 para Lunes o 2 para Martes.")
                    continue
                break
            if dia == '1':
                print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
            else:
                print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")
            pass
    elif opcion_int == 4:
        # Logica para ver resumen general
        lunes_ocupados = 0
        martes_ocupados = 0
        for turno in [lunes1, lunes2, lunes3, lunes4]:
            if turno != "":
                lunes_ocupados += 1
        for turno in [martes1, martes2, martes3]:
            if turno != "":
                martes_ocupados += 1
        lunes_disponibles = 4 - lunes_ocupados
        martes_disponibles = 3 - martes_ocupados
        
        print(f"Lunes: {lunes_ocupados} turno ocupado, {lunes_disponibles} turnos disponibles.")
        print(f"Martes: {martes_ocupados} turno ocupado, {martes_disponibles} turnos disponibles.")
        
        if lunes_ocupados > martes_ocupados:
            print("El día con más turnos ocupados es: Lunes.")
        elif martes_ocupados > lunes_ocupados:
            print("El día con más turnos ocupados es: Martes.")
        else:
            print("Ambos días tienen la misma cantidad de turnos ocupados.")
        pass
    elif opcion_int == 5:
        print("Cerrando sistema.")
        break