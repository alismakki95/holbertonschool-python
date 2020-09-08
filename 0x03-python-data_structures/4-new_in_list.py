#!/usr/bin/python3
def new_in_list(my_list, idx, element):
 if idx <0  or (len (my_list)) -1 <idx :
     return my_list
 else:
     new_list=my_list.copy()
     new_list[idx]=element
     return print(new_list)
