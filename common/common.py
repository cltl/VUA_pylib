#!/usr/bin/env python

from operator import itemgetter

def get_max_distr_dict(my_dict):
    vect = my_dict.items()
    if len(vect) !=0:
        vect.sort(key=itemgetter(1),reverse=True)
        return vect[0]
    return None

my_dict = {'a':20,'b':1,'c':50}
print get_max_distr_dict(my_dict)