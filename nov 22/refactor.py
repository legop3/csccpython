# refactor.py
# daniel roberts
# 11/22/2022
# some basic function refactoring

import random

def shuffle_str(this_string):
    str_list=[]
    for i in range(0,len(this_string),1):
        str_list.append(this_string[i])
    # print("list is",str_list)
    random.shuffle(str_list)
    # print("shuffled list",str_list)
    new_str=""
    for i in range(0,len(this_string),1):
        new_str=new_str+str_list[i]
    # print("new string",new_str)
    return(new_str)

def shuffle_alpha():
    the_str="abcdefghijklmnopqrstuvwxyz"
    rand_alpha=shuffle_str(the_str)
    return(rand_alpha)

my_str="python is fun!"
print("my string is",my_str)
rand_str=shuffle_str(my_str)
print("back in main, random string",rand_str)

rand_str=shuffle_alpha()
print("random alphabet",rand_str)