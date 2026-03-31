#Ejercicio 1
cliente = input("Ingrese el nombre del cliente: ").strip()

while cliente == "" or not cliente.isalpha():
    print("Nombre no válido. Por favor, ingrese un nombre válido.")
    cliente = input("Ingrese el nombre del cliente: ").strip()  
    
cantidad_str = input("Ingrese la cantidad de productos a comprar: ").strip()

while not cantidad_str.isdigit() or int(cantidad_str) <= 0:
    print("Cantidad no válida. Por favor, ingrese una cantidad válida.")
    cantidad = input("Ingrese la cantidad de productos a comprar: ").strip()  

cantidad = int(cantidad_str)
total_sin_descuento = 0
total_con_descuento = 0.0
ahorro = 0.0

for i in range(1, cantidad + 1):
    
    precio_str = input(f"Producto {i} - precio: ").strip()
    
    while not precio_str.isdigit() or int(precio_str) <= 0:
        print("Precio no válido. Por favor, ingrese un precio válido.")
        precio_str = input(f"Producto {i} - precio: ").strip()
        
    precio_int = int(precio_str)
    
    descuento = input("Ingrese s / n si tiene descuento: ").strip().lower()
    
    while descuento not in ['s', 'n']:
        print("Entrada no válida. Por favor, ingrese 's' para sí o 'n' para no.")
        descuento = input("Ingrese s / n si tiene descuento").strip().lower()
    
    total_sin_descuento += precio_int
    
    if descuento == 's':
        precio_final = precio_int * 0.9  # Aplicar descuento del 10%
    else:
        precio_final = precio_int  # Sin descuento

    total_sin_descuento += precio_int    
    total_con_descuento += precio_final
    ahorro = total_sin_descuento - total_con_descuento
    promedio = total_con_descuento / cantidad
    
print(f"Total sin descuento: ${total_sin_descuento:.2f}")
print(f"Total con descuento: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
