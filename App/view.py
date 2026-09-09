import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
import time
import App.logic as logic
from tabulate import tabulate
import DataStructures.array_list as arr
import DataStructures.single_linked_list as sll

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    control=logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    filename="chocolate_sale_100_elementos.csv"
    print("Cargando información de los archivos ....\n")
    start_time=logic.get_time()
    res=logic.load_data(control,filename)
    end_time=logic.get_time()
    tiempo=logic.delta_time(start_time,end_time)
    print("Reporte de carga de datos")
    print("--------------------------")
    print(f"Tiempo de ejecución: {tiempo} ms")
    print(f"Total de pedidos: {res['total_pedidos']}\n")
    
    def columnas(pedido):
        return[
            pedido.get("Order_ID",""),
            pedido.get("Product",""),
            pedido.get("Country",""),
            pedido.get("Channel",""),
            pedido.get("Order_Date",""),
            pedido.get("Price_per_Box",""),
            pedido.get("Amount","")
        ]
    cabeceras=["Order_ID","Product","Country","Channel","Order_Date","Price_per_Box","Amount"]
    
    print("--Pedidos con mayor y menor amount--")
    tabla_extremos=[
        ["Menor"]+columnas(res["pedido_min"]),
        ["Mayor"]+columnas(res["pedido_max"])
    ]
    print(tabulate(tabla_extremos,headers=["Tipo"]+cabeceras,tablefmt="grid"))
    print("\n")
    print("--Primeros 5 pedidos--")
    tabla_primeros=[]
    total_primeros=arr.size(res["primeros_5"])
    for i in range(0,total_primeros):
        pedido=arr.get_element(res["primeros_5"],i)
        tabla_primeros.append(columnas(pedido))
    print(tabulate(tabla_primeros,headers=cabeceras,tablefmt="grid"))
    print("\n")
    print("--Últimos 5 pedidos--")
    tabla_ultimos=[]
    total_ultimos=arr.size(res["ultimos_5"])
    for i in range(0,total_ultimos):
        pedido=arr.get_element(res["ultimos_5"],i)
        tabla_ultimos.append(columnas(pedido))
    print(tabulate(tabla_ultimos,headers=cabeceras,tablefmt="grid"))
    print("\n")
    return res

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    producto=input(f"Ingrese el nombre del producto a buscar: ").strip()
    start_time=logic.get_time()
    res=logic.req_1(control,producto)
    end_time=logic.get_time()
    
    tiempo=logic.delta_time(start_time,end_time)
    if res is None:
        print(f"No se encontró ningún pedido con el producto '{producto}'")
        return
    
    print(f"Tiempo de ejecución: {tiempo} ms")
    print(f"Total de pedidos con el producto '{producto}': {res['count']}")
    print(f"Año con mas pedidos: {res['year_max']}")
    tabla_stats = [
        ["Precio por caja (USD)", f"${res['avg_price']:.2f}", f"${res['min_price']:.2f}", f"${res['max_price']:.2f}"],
        ["Descuento (%)", f"{res['avg_discount']:.2f}%", f"{res['min_discount']:.2f}%", f"{res['max_discount']:.2f}%"],
        ["Cajas enviadas", f"{res['avg_boxes']:.2f}", f"{res['min_boxes']}", f"{res['max_boxes']}"],
        ["Inversión en Mercadeo (USD)", f"${res['avg_marketing']:.2f}", f"${res['min_marketing']:.2f}", f"${res['max_marketing']:.2f}"]
    ]
    headers=["Caracteristicas", 'Promedio','Minimo', 'Maximo']
    print(tabulate(tabla_stats, headers=headers, tablefmt="grid"))
    print('\n')
    def datos_pedido(pedido):
        return [
            pedido.get("Order_ID", ""),
            pedido.get("Country", ""),
            pedido.get("Order_Date", ""),
            f"${float(pedido.get('Price_per_Box', 0)):.2f}",
            f"${float(pedido.get('Marketing_Spend', 0)):.2f}",
            f"${float(pedido.get('Amount', 0)):.2f}"

        ]
    tabla_pedidos=[
        ["Menor"]+datos_pedido(res["pedido_min_amount"]),
        ["Mayor"]+datos_pedido(res["pedido_max_amount"])]
    print("--Pedidos con mayor y menor amount--")
    print(tabulate(tabla_pedidos, headers=["Tipo","Order_ID", "Country", "Order_Date", "Price_per_Box", "Marketing_Spend", "Amount"], tablefmt="grid"))
    


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    min_price = float(input("Ingrese el precio mínimo por caja: "))
    max_price = float(input("Ingrese el precio máximo por caja: "))

    start_time = logic.get_time()
    res = logic.req_2(control, min_price, max_price)
    end_time = logic.get_time()
    tiempo = logic.delta_time(start_time, end_time)

    print("\n--- Resultados Requerimiento 2 ---")
    print(f"Tiempo de ejecución: {tiempo} ms")
    print(f"Cantidad de pedidos en el rango: {res['count']}")

    if res['count'] > 0:
        print(f"Promedio Discount_Pct: {res['promedio_discount']:.2f}%")
        print(f"Promedio Marketing_Spend: ${res['promedio_marketing']:.2f}")
        print(f"Promedio Price_per_Box: ${res['promedio_price']:.2f}\n")

        cabeceras = ["Tipo", "Product", "Country", "Channel", "Order_Date", "Price_per_Box", "Amount"]
        
        def cols(pedido):
            return [
                pedido.get("Product", "Unknown"),
                pedido.get("Country", "Unknown"),
                pedido.get("Channel", "Unknown"),
                pedido.get("Order_Date", "Unknown"),
                f"${float(pedido.get('Price_per_Box', 0)):.2f}",
                f"${float(pedido.get('Amount', 0)):.2f}"
            ]

        tabla = [
            ["Más Reciente"] + cols(res["recent_order"]),
            ["Menor Amount"] + cols(res["min_amount_order"]),
            ["Mayor Amount"] + cols(res["max_amount_order"])
        ]
        
        print(tabulate(tabla, headers=cabeceras, tablefmt="grid"))
    else:
        print("No se encontraron pedidos en ese rango de precios.")


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    filtro = input("Ingrese el filtro ('MENOR' o 'MAYOR'): ").strip().upper()
    if filtro not in ["MENOR", "MAYOR"]:
        print("Filtro inválido. Debe ser 'MENOR' o 'MAYOR'.")
        return
        
    producto = input("Ingrese el nombre del producto: ").strip()
    fecha_inicial = input("Ingrese la fecha inicial (YYYY-MM-DD): ").strip()
    fecha_final = input("Ingrese la fecha final (YYYY-MM-DD): ").strip()

    start_time = logic.get_time()
    res = logic.req_5(control, filtro, producto, fecha_inicial, fecha_final)
    end_time = logic.get_time()
    tiempo = logic.delta_time(start_time, end_time)

    print("\n--- Resultados Requerimiento 5 ---")
    print(f"Tiempo de ejecución: {tiempo} ms")
    print(f"Filtro seleccionado: {filtro}")
    print(f"Total pedidos que cumplen filtro: {res['count']}")

    if res['count'] > 0:
        print("\nPromedios del grupo filtrado:")
        print(f"Promedio Price_per_Box: ${res['promedio_price']:.2f}")
        print(f"Promedio Boxes_Shipped: {res['promedio_boxes']:.2f}")
        print(f"Promedio Marketing_Spend: ${res['promedio_marketing']:.2f}\n")

        print(f"--- Detalles del Pedido con {filtro} Monto ---")
        target = res["target_order"]
        cabeceras = ["Price_per_Box", "Boxes_Shipped", "Amount", "Channel", "Order_Date", "Marketing_Spend"]
        tabla = [[
            f"${float(target.get('Price_per_Box', 0)):.2f}",
            target.get('Boxes_Shipped', 'Unknown'),
            f"${float(target.get('Amount', 0)):.2f}",
            target.get("Channel", "Unknown"),
            target.get("Order_Date", "Unknown"),
            f"${float(target.get('Marketing_Spend', 0)):.2f}"
        ]]
        print(tabulate(tabla, headers=cabeceras, tablefmt="grid"))
    else:
        print("No se encontraron pedidos con esas características.")


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 5:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
