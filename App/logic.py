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
    pedidos_sll = catalog["single_linked_list"]
    pedido_max=None
    pedido_min=None
    archivo_chocolates=data_dir + "/" + filename
    with open(archivo_chocolates, encoding="utf-8-sig") as file:
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
            try:
                row["Discount_Pct"]=float(row["Discount_Pct"]) if row["Discount_Pct"] != "Unknown" else 0.0
            except ValueError:
                row["Discount_Pct"]=0.0
            try:
                row["Boxes_Shipped"]=int(row["Boxes_Shipped"]) if row["Boxes_Shipped"] != "Unknown" else 0.0
            except ValueError:
                row["Boxes_Shipped"]=0.0
            try:
                row["Marketing_Spend"]=float(row["Marketing_Spend"]) if row["Marketing_Spend"] != "Unknown" else 0.0
            except ValueError:
                row["Marketing_Spend"]=0.0
            arr.add_last(pedidos,row)
            sll.add_last(pedidos_sll, row)
            
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
    
    for i in range(0,min(5,total_pedidos)):
        arr.add_last(primeros_5,arr.get_element(pedidos,i))
    for i in range(max(0,total_pedidos-5),total_pedidos):
        arr.add_last(ultimos_5,arr.get_element(pedidos,i))
    
    return {
        "total_pedidos": total_pedidos,
        "pedido_min": pedido_min,
        "pedido_max": pedido_max,
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
    suma_price=0
    suma_discount=0
    suma_boxes=0
    suma_mrkt=0
    min_ppb=None
    max_ppb=None
    min_dis=None
    max_dis=None
    min_box=None
    max_box=None
    min_mrkt=None
    max_mrkt=None
    contador_anio={}
    for i in range(0,arr.size(catalog["array_list"])):
        pedido=arr.get_element(catalog["array_list"],i)
        if pedido["Product"] == producto:
            count+=1
            suma_price+=pedido["Price_per_Box"]
            suma_discount+=pedido["Discount_Pct"]
            suma_boxes+=pedido["Boxes_Shipped"]
            suma_mrkt+=pedido["Marketing_Spend"]
            
            if min_ppb is None:
                min_ppb=pedido["Price_per_Box"]
            else:
                min_ppb=min(min_ppb,pedido["Price_per_Box"])
            if max_ppb is None:
                max_ppb=pedido["Price_per_Box"]
            else:
                max_ppb=max(max_ppb,pedido["Price_per_Box"])
            if min_dis is None:
                min_dis=pedido["Discount_Pct"]
            else:
                min_dis=min(min_dis,pedido["Discount_Pct"])
            if max_dis is None:
                max_dis=pedido["Discount_Pct"]
            else:
                max_dis=max(max_dis,pedido["Discount_Pct"])
            if min_box is None:
                min_box=pedido["Boxes_Shipped"]
            else:
                min_box=min(min_box,pedido["Boxes_Shipped"])
            if max_box is None:
                max_box=pedido["Boxes_Shipped"]
            else:
                max_box=max(max_box,pedido["Boxes_Shipped"])
            if min_mrkt is None:
                min_mrkt=pedido["Marketing_Spend"]
            else:
                min_mrkt=min(min_mrkt,pedido["Marketing_Spend"])
            if max_mrkt is None:
                max_mrkt=pedido["Marketing_Spend"]
            else:
                max_mrkt=max(max_mrkt,pedido["Marketing_Spend"])
            
            fecha=str(pedido["Order_Date"])
            if "-" in fecha:
                anio=fecha.split("-")[0]
            else:
                anio="Unknown"
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
        anio_mas_pedidos="Unknown"
    return {
        "avg_price": prom_ppb,
        "avg_discount": prom_dis,
        "avg_boxes": prom_box,
        "avg_marketing": prom_mrkt,
        "year_max": anio_mas_pedidos,
        "pedido_min_amount": min_order,
        "pedido_max_amount": max_order,
        "min_price": min_ppb,
        "max_price": max_ppb,
        "min_discount": min_dis,
        "max_discount": max_dis,
        "min_boxes": min_box,
        "max_boxes": max_box,
        "min_marketing": min_mrkt,
        "max_marketing": max_mrkt,
        "count": count
    }

def req_2(catalog, min_price, max_price):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    count = 0
    suma_discount = 0.0
    suma_marketing = 0.0
    suma_price = 0.0
    recent_order = None
    min_amount_order = None
    max_amount_order = None

    # Uso estricto de la estructura array_list
    lista_pedidos = catalog["array_list"]
    total_pedidos = arr.size(lista_pedidos)

    for i in range(total_pedidos):
        pedido = arr.get_element(lista_pedidos, i)
        ppb = pedido["Price_per_Box"]
        
        if min_price <= ppb <= max_price:
            count += 1
            amount = pedido["Amount"]
            
            suma_discount += pedido["Discount_Pct"]
            suma_marketing += pedido["Marketing_Spend"]
            suma_price += ppb

            # Pedido más reciente. Desempate: mayor Amount
            if recent_order is None:
                recent_order = pedido
            else:
                if pedido["Order_Date"] > recent_order["Order_Date"]:
                    recent_order = pedido
                elif pedido["Order_Date"] == recent_order["Order_Date"]:
                    if amount > recent_order["Amount"]:
                        recent_order = pedido

            # Pedido menor Amount. Desempate: menor Price_per_Box
            if min_amount_order is None:
                min_amount_order = pedido
            else:
                min_amt = min_amount_order["Amount"]
                if amount < min_amt:
                    min_amount_order = pedido
                elif amount == min_amt:
                    if ppb < min_amount_order["Price_per_Box"]:
                        min_amount_order = pedido

            # Pedido mayor Amount. Desempate: menor Price_per_Box
            if max_amount_order is None:
                max_amount_order = pedido
            else:
                max_amt = max_amount_order["Amount"]
                if amount > max_amt:
                    max_amount_order = pedido
                elif amount == max_amt:
                    if ppb < max_amount_order["Price_per_Box"]:
                        max_amount_order = pedido

    if count == 0:
        return {"count": 0}

    return {
        "count": count,
        "promedio_discount": suma_discount / count,
        "promedio_marketing": suma_marketing / count,
        "promedio_price": suma_price / count,
        "recent_order": recent_order,
        "min_amount_order": min_amount_order,
        "max_amount_order": max_amount_order
    }


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
    count=0
    


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
