# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 22:07:44 2017

@author: Prathyusha Mallela
"""

#assignement 2.1
def read_commasep_num_provide_list(comma_sep_num):
    num_list=list(comma_sep_num);#converts the tuple of numbers into list
    return num_list;

comma_sep_num=5,6,7,8
s=read_commasep_num_provide_list(comma_sep_num);
print("The list of comma separated numbers ",s);