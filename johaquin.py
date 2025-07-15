def menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca. ")
    print("2. Búsqueda por precio. ")
    print("3. Listado de productos. ")
    print("4. Salir")

menu()

productos = {
    "8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],
    "GF75HD": ["Asus", 15.6, "12GB", "DD", "1T", "Intel Core i3", "Nvidia GTX1050"],
    "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 5", "Nvidia GTX1050"] 
}
stock = {
    "8475HD": [387990, 10],
    "GF75HD": [749990, 2],
    "UWU131HD": [349990, 1]
}

def stock_marca(marca):
    marca = marca.lower()
    for modelo, datos in productos.items():
        try:
            if datos[0].lower() == marca:
                print(f"{modelo}: {stock[modelo][1]} unidades")
        except ValueError:
            print("no se encontraron modelos de esa marca")

def busqueda_precio(precio):
    try:
        p_min = int(p_min)
        p_max = int(p_max)
    except ValueError:
        print("Ingresa valores enteros")
        return
    resultado= []
    for modelo, (precio,cantidad) in stock.items():
        if p_min <= precio <= p_max and cantidad > 0:
            marca=productos[modelo][0]
            resultado.append(f"{marca}-{modelo}")
            if not resultado:
                print("no hay resultados en ese rango de precios")
        else:
            for r in sorted(resultado):
                print(r)
try:
    opcion = int(input("Ingresa una opción: "))
except ValueError:
    print(" Ingresa una opción valida: ")


if opcion == 1:
    marca = input("Ingresa una marca: ")
    stock_marca(marca)

elif opcion == 2:
    p_min = input("Ingresa el Precio minimo del producto: ")
    p_max = input("Ingresa el Precio maximo del producto: ")
    busqueda_precio(p_min, p_max)
    
    
elif opcion == 3:
    print(F"Lista {productos}")

elif opcion == 4:
    print("saliste")
