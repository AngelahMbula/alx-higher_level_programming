#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiples = my_list[:]
    for count, i in enumerate(my_list):
        if my_list[i] % 2 == 0:
            multiples[count] = True
        else:
            multiples[count] = False
    return (multiples)
