#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:20:45 2020

@author: emirimorita
"""

# PREDICTION FUNCTION
# import libraries
import os
import pandas as pd
import numpy as np
import pickle
import csv  
from pathlib import Path

# predict
def dip_predict(file):
    #os.chdir(dir)
    # read test_x csv
    raw_test_x = pd.read_csv(file, encoding='utf-8')            
    # store workID
    workID = raw_test_x['お仕事No.']
    # prep test_x
    colnames_84 = pd.read_csv("app/test_python/colnames_84.csv", 
    encoding='utf-8', squeeze=True)   
    x_test = raw_test_x[colnames_84]
    x_test = x_test.fillna(-999) # fill missing values
    x_test = np.array(x_test) 

    # make prediction
    with open("app/test_python/model.dump", 'rb') as f: # load model
        rfr = pickle.load(f)
    y_pred = rfr.predict(x_test)     
    output = pd.DataFrame({'お仕事No.' : workID, '応募数 合計' : y_pred})
    return output.to_csv('app/CSV_files/output.csv', index=False)
    



