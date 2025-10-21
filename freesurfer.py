#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 07:49:15 2020

Freesurfer for HOME data

@author: edm9fd
"""
from glob import glob
from nipype.interfaces.freesurfer import ReconAll
import os

def extract_subject_number(f):
    f1 = f.split('/')
    f2 = f1[-1].split('_')
    return f2[0]


def recon_all(sub, sub_dir):
    reconall = ReconAll()
    reconall.inputs.subject_id = sub
    reconall.inputs.directive = 'all'
    reconall.inputs.subjects_dir = sub_dir
    reconall.inputs.T1_files = glob('/mnt/elysium/IRC805/morph/t1w/'+str(sub)+'/*.nii.gz')[0]
    #reconall.inputs.T2_file = glob('/mnt/elysium/IRC805/freesurfer/t2w/'+str(sub)+'/*.nii.gz')[0]
    #reconall.inputs.use_T2 = True
    reconall.inputs.parallel = True
    reconall.inputs.hires = True
    reconall.inputs.openmp = 10
    reconall.run()    


def remove_completed_folders(subdir, folderlist):
    removing = glob.glob(subdir + '/*')
    for i in removing:
        folderlist = folderlist.remove(i)
    return folderlist
 
    
SUBJECTS_DIR = '/mnt/elysium/IRC805/morph/freesurfer/'
t1w_folders = glob('/mnt/elysium/IRC805/morph/t1w/*')


completed = []
for i in t1w_folders:
    s = extract_subject_number(i)
    if os.path.isdir(SUBJECTS_DIR + '/' + str(s)):
        print('Skipping '+str(s))
        next
    else:
        print(str(s))
        recon_all(s, SUBJECTS_DIR)
        outfile = open('/mnt/elysium/IRC805/status/freesurfer_complete.txt', 'a')
        outfile.write(str(s)+' \n')
        outfile.close()
        
