#!/usr/bin/env python

from operator import itemgetter

# Get the max (key,count) from a dict like  my_dict = {'a':20,'b':1,'c':50}
# It will return --> (c,50)
def get_max_distr_dict(my_dict):
    vect = my_dict.items()
    if len(vect) !=0:
        vect.sort(key=itemgetter(1),reverse=True)
        return vect[0]
    return None

def normalize_pos(pos):
    pos = pos.lower()
    new_pos = pos
    if pos in ['adj']:
        new_pos = 'a'
    elif pos in ['adverb']:
        new_pos = 'r'
    elif pos in ['anypos']:
        new_pos = '*'
    elif pos in ['noun']:
        new_pos = 'n'
    elif pos in ['verb']:
        new_pos = 'p'
    return new_pos

