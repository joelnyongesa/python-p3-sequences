#!/usr/bin/env python3

def print_fibonacci(length):
    my_list = []
    a = 0  
    b = 1  

    for i in range(0,length):
        if length == 0:
            return my_list
        else:
            my_list.append(a)
            c = a + b
            a = b
            b = c
    return print(my_list)
