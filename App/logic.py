import time
import csv
import os
csv.field_size_limit(2147483647)

data_dir=os.path.dirname(os.path.realpath(__file__)) + "/../Data"
import DataStructures.array_list as arr
import DataStructures.single_linked_list as sll

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {
        "array_list": arr.new_list(),
        "single_linked_list": sll.new_list()
    }
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    pedidos=catalog["array_list"]
    pedido_max=None
    pedido_min=None
    archivo_chocolates=data_dir + filename
    with open(archivo_chocolates, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            for key in row.keys():
                if row[key] is None or row[key].strip()=="":
                    row[key] = "Unknown"
            try:
                row["Amount"] = float(row["Amount"]) if  row["Amount"] != "Unknown" else 0.0
            except ValueError:
                row["Amount"] = 0.0
            try:
                row["Price_per_Box"]=float(row["Price_per_Box"]) if row["Price_per_Box"] != "Unknown" else 0.0
            except ValueError:
                row["Price_per_Box"]=0.0
            arr.add_last(pedidos,row)
            
            if pedido_min is None:
                pedido_min=row
            else:
                if row["Amount"]<pedido_min["Amount"]:
                    pedido_min=row
                elif row["Amount"]==pedido_min["Amount"] and row["Price_per_Box"]<pedido_min["Price_per_Box"]:
                    pedido_min=row
            if pedido_max is None:
                pedido_max=row
            else:
                if row["Amount"]>pedido_max["Amount"]:
                    pedido_max=row
                elif row["Amount"]==pedido_max["Amount"] and row["Price_per_Box"]>pedido_max["Price_per_Box"]:
                    pedido_max=row
    total_pedidos=arr.size(pedidos)
    primeros_5=arr.new_list()
    ultimos_5=arr.new_list()
    
    for i in range(1,min(6,total_pedidos+1)):
        arr.add_last(primeros_5,arr.get_element(pedidos,i))
    for i in range(max(1,total_pedidos-4),total_pedidos+1):
        arr.add_last(ultimos_5,arr.get_element(pedidos,i))
    
    return {
        "total": total_pedidos,
        "menor amount": pedido_min,
        "maximo amount": pedido_max,
        "primeros_5": primeros_5,
        "ultimos_5": ultimos_5
    }
    

# Funciones de consulta sobre el catálogo


def req_1(catalog,producto):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    count=0
    min_order=None
    max_order=None
    for pedido in catalog["array_list"]["elements"]:
        if pedido["Product"] == producto:
            count+=1
            suma_price+=pedido["Price_per_Box"]
            suma_discount+=pedido["Discount_pct"]
            suma_boxes+=pedido["Boxes_shipped"]
            suma_mrkt+=pedido["Marketing_Spend"]
            
            min_ppb=min(min_ppb,pedido["Price_per_Box"])
            max_ppb=max(max_ppb,pedido["Price_per_Box"])
            min_dis=min(min_dis,pedido["Discount_pct"])
            max_dis=max(max_dis,pedido["Discount_pct"])
            min_box=min(min_box,pedido["Boxes_shipped"])
            max_box=max(max_box,pedido["Boxes_shipped"])
            min_mrkt=min(min_mrkt,pedido["Marketing_Spend"])
            max_mrkt=max(max_mrkt,pedido["Marketing_Spend"])
            
            fecha=str(pedido["Order_Date"])
            contador_anio={}
            if "-" in fecha:
                anio=fecha.split("-")[0]
            else:
                fecha
            contador_anio[anio]=contador_anio.get(anio,0)+1
            
            if min_order is None:
                min_order=pedido
            else:
                if pedido["Amount"]<min_order["Amount"]:
                    min_order=pedido
                elif pedido["Amount"]==min_order["Amount"]:
                    if pedido["Marketing_Spend"]<min_order["Marketing_Spend"]:
                        min_order=pedido
            if max_order is None:
                max_order=pedido
            else:
                if pedido["Amount"]>max_order["Amount"]:
                    max_order=pedido
                elif pedido["Amount"]==max_order["Amount"]:
                    if pedido["Marketing_Spend"]>max_order["Marketing_Spend"]:
                        max_order=pedido
    if count==0:
        return None
    prom_ppb=suma_price/count
    prom_dis=suma_discount/count
    prom_box=suma_boxes/count
    prom_mrkt=suma_mrkt/count
    
    if contador_anio:
        anio_mas_pedidos=max(contador_anio,key=contador_anio.get)
    else:
        "Unknown"
    return {
        "promedio price_per_box": prom_ppb,
        "promedio discount": prom_dis,
        "promedio boxes_shipped": prom_box,
        "promedio marketing_spend": prom_mrkt,
        "año con más pedidos": anio_mas_pedidos,
        "pedido con menor amount": min_order,
        "pedido con mayor amount": max_order
    }

def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
