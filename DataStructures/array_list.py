def new_list():
    newlist = {
        'elements':[],
        'size':0
    }
    return newlist

def add_first(my_list,element):
    my_list['elements'].insert(0,element)
    my_list['size']+=1
    return my_list

def add_last(my_list,element):
    my_list['elements'].append(element)
    my_list['size']+=1
    return my_list


def size(my_list):
    return my_list['size']


def first_element(my_list):
    return my_list['elements'][0]

def get_element(my_list,pos):
    return my_list['elements'][pos]

def is_present(my_list,element,cmp_function):
    size=my_list['size']
    if size>0:
        keyexist=False
        for keypos in range(0,size):
            info=my_list["elements"][keypos]
            if cmp_function(element,info)==0:
                keyexist=True
                break
        if keyexist:
            return keypos
    return -1


def is_empty(my_list):
    return my_list['size'] == 0

def last_element(my_list):
    return my_list['elements'][-1]


def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list['size']:
        raise IndexError("List index out of range")
    my_list['elements'].pop(pos)
    my_list['size'] -= 1
    return my_list

def remove_first(my_list):
    if my_list['size'] == 0:
        raise IndexError("List index out of range")
    element = my_list['elements'].pop(0)
    my_list['size'] -= 1
    return element


def remove_last(my_list):
    if my_list['size'] == 0:
        raise IndexError("List index out of range")
    element = my_list['elements'].pop()
    my_list['size'] -= 1
    return element

def insert_element(my_list, element, pos):
    my_list['elements'].insert(pos, element)
    my_list['size'] += 1
    return my_list
def change_info(my_list, pos, new_info):
    my_list['elements'][pos] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    element_1 = get_element(my_list,pos_1)
    element_2 = get_element(my_list,pos_2)
    
    my_list['elements'][pos_1] = element_2
    my_list['elements'][pos_2] = element_1
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list['size']:
        raise IndexError("list index out of range") 
    sub_list = new_list()
    sub_list['elements'] =  my_list['elements'][pos_i:num_elements+pos_i]
    sub_list['size'] = len(sub_list["elements"])
    return sub_list