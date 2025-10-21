#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 12:31:47 2021

@author: AE
"""

from glob import glob
import subprocess

subject_folders = glob('')

def subject_number(f):
    f1 = f.split('/')
    f2 = f1[-2].split('-')
    return f2[-1]

def heudiconv(sub):
    """
    heudiconv 
    -d 
    -s sub
    -f 
    -o 

    """
    dicom_dir = ['-d', '/*/*.dcm']
    subject = ['-s', sub]
    heuristic = ['-f', 'heuristic.py']
    converter = ['-c', 'dcm2niix']
    out_dir = ['-o', 'heudiconv']
    other = ['--overwrite']
    command_list = ['heudiconv'] + dicom_dir + subject + heuristic + converter + out_dir + other
    subprocess.run(command_list, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

for i in subject_folders:
    subject = subject_number(i)
    print('Processing '+str(subject)+ '. . .')
    heudiconv(subject)

