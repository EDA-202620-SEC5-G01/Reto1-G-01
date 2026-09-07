def new_list():
    newlist = {
        "first":None,
        "last":None,
        "size":0,
    }
    return newlist


def add_first(my_list,element):
    if my_list["size"]==0:
        new_node={"info":element,"next":None}
        my_list["first"]=new_node
        my_list["last"]=new_node
    else:
        new_node={"info":element,"next":my_list["first"]}
        my_list["first"]=new_node
    my_list["size"]+=1
    return my_list

def add_last(my_list,element):
    new_node={"info":element,"next":None}
    if my_list["size"]==0:
        my_list["first"]=new_node
        my_list["last"]=new_node
    else:
        my_list["last"]["next"]=new_node
        my_list["last"]=new_node
    my_list["size"]+=1
    return my_list

def size(my_list):
    return my_list['size']

def first_element(my_list):
    first_element = my_list['first']['info']
    return first_element
    
def get_element(my_list,pos):
    searchpos=0
    node=my_list["first"]
    while searchpos<pos:
        node=node["next"]
        searchpos+=1
    return node["info"]

def is_present(my_list,element,cmp_function):
    is_in_array=False
    temp=my_list["first"]
    count=0
    while not is_in_array and temp is not None:
        if cmp_function(element,temp["info"])==0:
            is_in_array=True
        else:
            temp=temp["next"]
            count+=1
    if not is_in_array:
        count=-1
    return count

def is_empty(my_list):
    return my_list["size"]==0
def size(my_list):
    return my_list["size"]
def last_element(my_list):
    last_element = my_list['last']['info']
    return last_element
def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
        if my_list["first"] is None:
            my_list["last"] = None
    else:
        i = 0
        curr = my_list["first"]
        while i < pos - 1:
            curr = curr["next"]
            i += 1
        curr["next"] = curr["next"]["next"]
        if curr["next"] is None:
            my_list["last"] = curr
    my_list["size"] -= 1
    return my_list
def remove_first(my_list):
    if my_list["first"] is None:
        raise Exception('IndexError: list index out of range')
    removed_value = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    if my_list["first"] is None:
        my_list["last"] = None
    my_list["size"] -= 1
    return removed_value
def remove_last(my_list):
    if my_list["first"] is None:
        raise Exception('IndexError: list index out of range')
    removed_value = my_list["last"]["info"]
    if my_list["first"] == my_list["last"]:
        my_list["first"] = None
        my_list["last"] = None
    else:
        curr= my_list["first"]
        i=0
        while i < size(my_list) - 2:
            curr= curr["next"]
            i +=1
        curr["next"]= None
        my_list["last"]= curr
    my_list["size"] -=1
    return removed_value

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    curr= my_list["first"]
    i=0
    while i < pos:
        curr= curr["next"]
        i +=1  
    nuevo_nodo= {
        "info": element,
        "next": curr["next"]    
        }
    curr["next"]= nuevo_nodo
    my_list["size"] +=1
    return my_list
def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    curr= my_list["first"]
    i=0
    while i < pos:
        curr= curr["next"]
        i +=1  
    curr["info"]= new_info
    return my_list
def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= size(my_list) or pos2 < 0 or pos2 >= size(my_list):
        raise Exception('IndexError: list index out of range')
    get1= get_element(my_list, pos1)
    get2= get_element(my_list, pos2)
    change_info(my_list, pos1, get2)
    change_info(my_list, pos2, get1)
    return my_list  
def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= size(my_list) or num_elements < 0 or pos + num_elements > size(my_list):
        raise Exception('IndexError: list index out of range')
    new = new_list()
    curr= my_list["first"]
    i=0
    while i < pos:
        curr= curr["next"]
        i +=1
    i=0
    while i < num_elements:
        add_last(new, curr["info"])
        curr = curr["next"]
        i += 1

    return new
