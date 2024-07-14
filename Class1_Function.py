#First module 

def add():
    print('This function will add values.')

def mult():
    print('This function will multiplicate values.')

def find_index(to_find, item):
    for i, value in enumerate(to_find):
        if value == item:
            return 1 
    return -1 