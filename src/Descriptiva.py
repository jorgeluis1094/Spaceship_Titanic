#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:34:40 2022

@author: jorge
"""
# esto es un comentario

import pandas as pd
import numpy as np
from plotnine import *

############################ Cargue de datos #################################
filename_train = './DATA/train.csv'
filename_test = './DATA/test.csv'
filename_sample_sub = './DATA/sample_submission.csv'

data_train = pd.read_csv(filename_train, header=0)
data_test = pd.read_csv(filename_test, header=0)
data_sample_sub = pd.read_csv(filename_sample_sub, header=0)
##############################################################################


# Data manipulation before making bar plot
HomePlanet_count = pd.DataFrame(data_train['HomePlanet'].value_counts()).reset_index()
HomePlanet_count.columns = ['HomePlanet','Count']
HomePlanet_count

# Create a bar plot
b = (
    ggplot(data = HomePlanet_count)+
    geom_bar(aes(x = 'HomePlanet',
                 y = 'Count'),
             fill = np.where(HomePlanet_count['HomePlanet'] == 'Earth', '#c22d6d', '#80797c'),
             stat = 'identity')+
    geom_text(aes(x = 'HomePlanet',
                  y = 'Count',
                  label = 'Count'),
              nudge_y = 0.7)+
    labs(title = 'Bar plot of Countries that Won Olympics',
         subtitle = '1896 - 2016')+
    xlab('Country')+
    ylab('Frequency')+
    scale_x_discrete(limits = HomePlanet_count['HomePlanet'].tolist())+
    theme_bw()    
)

print(b)
