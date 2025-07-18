productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], }

def stock_marca (marca):
    total_stock= 0 
    encontrado= False
    for modelo_id, datos_producto in productos.items():
        if datos_producto[0].lower()==marca.lower():
            encontrado= True
            if modelo_id in stock:
                total_stock += stock[modelo_id][1]
    if encontrado:
        print(f"stock total de {marca}:{total_stock}")
    else:
        print(f"no se encontraron productos de la marca '{marca}'.")
def busqueda_precio (p_min,p_max):
    resultados=[]
    for modelo_id,datos_stock in stock.items():
        precio= datos_stock[0]
        stock=datos_stock[1]
        if p_min<=precio<=p_max and stock>0:
            marca=productos[modelo_id][0]
            tipo_producto=productos[modelo_id][1]
            resultados.append(f"{marca}---{tipo_producto}(modelo:{modelo_id})")
    if resultados:
        resultados.sort()
        print("productos disponibles en el rango de precios: ")
        for resultado in resultados:
            print(resultado)
    else:
        print("no hay productos en el rango de precios")
def actualizar_precio(modelo,precio):
    if modelo in stock:
        stock[modelo][0]=precio
        return True
    else:
        return False
def mostrar_menu():
    print("****MENU PRINCIPAL****")
    print("1) stock marca ")
    print("2) busqueda por precio ") 
    print("3) actualizar precio ")
    print("4) salir ")
def main():
    while True:
        mostrar_menu()
        opcion = input(" seleccione una opcion del menu ")
        if opcion=="1":
            marca_busqueda=input("ingrese la marca a buscar :") 
            stock_marca(marca_busqueda)
        elif opcion=="2":
            while True:
                try:
                    min_precio_str=input("ingrese el precio minimo")
                    max_precio_str=input("ingrese el precio maximo")
                    p_min=int(min_precio_str)
                    p_max=int(max_precio_str)
                    busqueda_precio=(p_min,p_max)
                    break
                except ValueError:
                    print()
        elif opcion=="3":
            while True:
                modelo_actualizar=input("ingrese el codigo del producto a actualizar ( ej:8475HD ):").upper()
                try:
                    nuevo_precio_str=input("ingrese el nuevo precio: ")
                    nuevo_precio=int(nuevo_precio_str)
                    if actualizar_precio(modelo_actualizar, nuevo_precio):
                        print("precio actualizado !")
                    else:
                        print(" el modelo no existe !") 
                    respuesta=input("¿ desea actualizar otro? (si/no):").lower()
                    if respuesta != 'si':
                        break
                except ValueError:
                    print("debe ingresar un valor entrero para el  precio ")
        elif opcion=='4':
            print("programa finalizado")
            break
        else:
            print("opcion no valida , porfavor ingrese opcion entre (1-4) ")       
main()
    