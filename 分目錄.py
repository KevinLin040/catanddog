# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:25:14 2020

@author: user
"""

import os
import random
import shutil

def get_file_list_from_dir(datadir):
    all_files = os.listdir(os.path.abspath(datadir))
    data_files = list(filter(lambda file: file.endswith('.jpg'), all_files))
    return data_files

datadir = '../catanddog/PetImages'
dir_lists = os.listdir(datadir)

sample_num = 5000
rate = 0.7

for dir_list in dir_lists:
    if not os.path.exists('./img/training_set/{}'.format(dir_list)):
        os.makedirs('./img/training_set/{}'.format(dir_list))
    if not os.path.exists('./img/test_set/{}'.format(dir_list)):
        os.makedirs('./img/test_set/{}'.format(dir_list))
    
    dir_files = get_file_list_from_dir('{}/{}'.format(datadir,dir_list))
    if sample_num > len(dir_files):
        sample_num = len(dir_files)
    
    dir_files = dir_files[-(sample_num):]
    num = int(len(dir_files)*rate)
    for i, file in enumerate(dir_files, start=1):
        if i <= num:   
            shutil.copy('{}/{}/{}'.format(datadir,dir_list,file),'./img/training_set/{}'.format(dir_list))
        else:
            shutil.copy('{}/{}/{}'.format(datadir,dir_list,file),'./img/test_set/{}'.format(dir_list))
        print('復制分類目錄{}已完成{}/{}'.format(dir_list,i,len(dir_files)))
        

    

    

