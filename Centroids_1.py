# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:37:03 2018
This points extends the starting point to a single coordinate which is the centroid of all the points

@author: sania
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#load the data
#OX = []
#OY = []
#goes frome 0 to ...
findx = 0
tindx = 23
totindx = tindx-findx
#200m_1.csv   0-103
#200m_2.csv
#200m_3.csv
#poitns1.csv  0-159
#points2.csv  0-157
#points3.csv  0-150
#points4.csv  0-156
#points5.csv  0-142
#points6.csv  0-153
#points7.csv  0-154
#points8.csv  0-143
df = pd.read_csv('200m_1.csv')
data = df.as_matrix()
data_O = df.as_matrix()


def oiginal_plots():
    global data_O
    data_O = data_O[findx:tindx,:]
    slope = np.ones((tindx-findx,1))
    intercept = np.ones((tindx-findx,1))
    data_O = np.hstack([data_O,slope])
    data_O = np.hstack([data_O,intercept])
    
    for x in range(findx, tindx):
        #tranlating the x coordinates to 0
        #data[x,3] = data[x,3] - data[x,1]
        #data[x,1] = data[x,1] - data[x,1]
        #translating the y coordinates to 0
        #data[x,2] = data[x,2] - data[x,0]
        #data[x,0] = data[x,0] - data[x,0]
        #calculating the slope of all the lines
        data_O[x,4] = (data_O[x,2] - data_O[x,0])/(data_O[x,3] - data_O[x,1])
        #calculating the intercept(negative)
        data_O[x,5] = -(data_O[x,0]- data_O[x,4]*data_O[x,1])
        #data[x,5] = -(data[x,1]- data[x,4]*data[x,0])
    
    
    OX = data_O[:,0]
    OY = data_O[:,1]
    DX = data_O[:,2]
    DY = data_O[:,3]
    Da = data_O[:,4]
    Db = data_O[:,5]
    n = np.arange(tindx-findx)+1
    plt.plot([OY,DY],[OX,DX], marker='o',markevery=(1,DY.size),color='#f07810', zorder=2,markeredgecolor='red')#label='Origin Points')
    for i, txt in enumerate(n):
        plt.annotate(txt ,xy = (DY[i],DX[i]))
    plt.grid()
    plt.figure()
    plt.show()
    
    plt.scatter(Da,Db,color='#e01171')
    for i, txt in enumerate(n):
        plt.annotate(txt, (Da[i],Db[i]))

    plt.legend(loc = 'best')
    plt.grid()
    plt.figure()
    plt.show()

def centroid_1():
    global data 
    data = data[findx:tindx,:]
    #print(data[:,0])
    #sum of all the columns
    a = data.sum(axis = 0 )
    print(a[0])
    print(a[0]/(tindx-findx))
    print(a[1]/(tindx-findx))
    avg_OX = a[0]/(tindx-findx)
    avg_OY = a[1]/(tindx-findx)
    #add extra colums 
    data= data[findx:tindx,:]
    slope = np.ones((tindx-findx,1))
    intercept = np.ones((tindx-findx,1))
    data = np.hstack([data,slope])
    data = np.hstack([data,intercept])
    for x in range(findx, tindx):
        #bring the origins to the centroid
        data[x,0] = avg_OX
        data[x,1] = avg_OY
        #calculating the slope of all the lines
        data[x,4] = (data[x,2] - data[x,0])/(data[x,3] - data[x,1])
        #calculating the intercept(negative)
        data[x,5] = -(data[x,0]- data[x,4]*data[x,1])
        #data[x,5] = -(data[x,1]- data[x,4]*data[x,0])
        
    
    OX = data[:,0]
    OY = data[:,1]
    DX = data[:,2]
    DY = data[:,3]
    Da = data[:,4]
    Db = data[:,5]
    n = np.arange(tindx-findx)+1
    plt.plot([OY,DY],[OX,DX], marker='o',markevery=(1,DY.size),color='#947CB0', zorder=2,markeredgecolor='red')#label='Origin Points')
    for i, txt in enumerate(n):
        plt.annotate(txt ,xy = (DY[i],DX[i]))
    
    plt.grid()
    plt.figure()
    plt.show()
    
    plt.scatter(Da,Db)
    for i, txt in enumerate(n):
        plt.annotate(txt, (Da[i],Db[i]))
    plt.legend(loc = 'best')
    plt.grid()
    plt.show()
    
oiginal_plots()
centroid_1()