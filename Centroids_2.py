# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 18:01:17 2018

@author: Zodiac
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:37:03 2018

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
tindx = 20
totindx = tindx-findx
#200m_1.csv   0-103
#200m_2.csv   0-22
#200m_3.csv   0-22
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

def centroid_2():
    global data
    global df
    data = data[findx:tindx,:]
    data_df = pd.DataFrame(data)
    #print(data_df)
    #find the min and max X coordinates
    max_OX = data_df[1].max()
    min_OX = data_df[1].min()
    print("Max OX is: ",max_OX)
    print("Min OX is: ",min_OX)
    #use the section formula to calculte the quartiles
    OX_1 = (1*max_OX + 3*min_OX) / 4
    OX_2 = (3*max_OX + 1*min_OX) / 4
    print("OX_1 is : ",OX_1)
    print("OX_2 is : ",OX_2)
    
    #find the min and max y coordinates
    max_OY = data_df[0].max()
    min_OY = data_df[0].min()
    print("Max OY is: ",max_OY)
    print("Min OY is: ",min_OY)
    #use the sectiona formula to caculate the quartiles
    OY_1 = (3*max_OY + 1*min_OY) / 4
    OY_2 = (1*max_OY + 3*min_OY) / 4
    print("OY_1 is : ",OY_1)
    print("OY_2 is : ",OY_2)
    
    #find the mid-poit of the box
    mid_OX = (max_OX + min_OX) / 2
    mid_OY = (max_OY + min_OY) / 2
    
    plt.plot([mid_OX,mid_OX],[max_OY,min_OY],'red')
    plt.plot([min_OX,max_OX],[mid_OY,mid_OY],'red')
    
    plt.plot([min_OX,max_OX,max_OX,min_OX,min_OX],[min_OY,min_OY,max_OY,max_OY,min_OY],'yellow')
    
    plt.scatter(OX_1,OY_2)
    plt.scatter(OX_2,OY_2)
    plt.scatter(OX_1,OY_1)
    plt.scatter(OX_2,OY_1)
    
    OX = data[:,0]
    OY = data[:,1]
    DX = data[:,2]
    DY = data[:,3]
    n = np.arange(tindx-findx)+1
    plt.plot([OY,DY],[OX,DX], marker='o',markevery=(1,DY.size),color='#947CB0', zorder=2,markeredgecolor='red')#label='Origin Points')
    for i, txt in enumerate(n):
        plt.annotate(txt ,xy = (DY[i],DX[i]))
        plt.annotate(txt ,xy = (OY[i],OX[i]))
        
    plt.grid()
    plt.figure()
    plt.show()
    
    #changing the values in data
    for x in range(findx, tindx):
        if (data[x,1]>=min_OX and data[x,1]<mid_OX):
            if(data[x,0]>=min_OY and data[x,0]<mid_OY):
                data[x,0] = OY_2
                data[x,1] = OX_1
                print("Point {} is in the 3rd region".format(x+1))
            else:
                data[x,0] = OY_1
                data[x,1] = OX_1
                print("Point {} is in the 1st region".format(x+1))
        else:
            if(data[x,0]>=min_OY and data[x,0]<mid_OY):
                data[x,0] = OY_2
                data[x,1] = OX_2
                print("Point {} is in the 4th region".format(x+1))
            else:
                data[x,0] = OY_1
                data[x,1] = OX_2
                print("Point {} is in the 2nd region".format(x+1))
                
    plt.plot([mid_OX,mid_OX],[max_OY,min_OY],'red')
    plt.plot([min_OX,max_OX],[mid_OY,mid_OY],'red')
    
    plt.plot([min_OX,max_OX,max_OX,min_OX,min_OX],[min_OY,min_OY,max_OY,max_OY,min_OY],'yellow')
    
    plt.scatter(OX_1,OY_2)
    plt.scatter(OX_2,OY_2)
    plt.scatter(OX_1,OY_1)
    plt.scatter(OX_2,OY_1)
    
    slope = np.ones((tindx-findx,1))
    intercept = np.ones((tindx-findx,1))
    data = np.hstack([data,slope])
    data = np.hstack([data,intercept])
    
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
        plt.annotate(txt ,xy = (OY[i],OX[i]))
    plt.grid()
    plt.figure()
    plt.show()
    
    
    for x in range(findx, tindx):
        #calculating the slope of all the lines
        data[x,4] = (data[x,2] - data[x,0])/(data[x,3] - data[x,1])
        #calculating the intercept(negative)
        data[x,5] = -(data[x,0]- data[x,4]*data[x,1])
        #data[x,5] = -(data[x,1]- data[x,4]*data[x,0])
    
   
    plt.scatter(Da,Db)
    for i, txt in enumerate(n):
        plt.annotate(txt, (Da[i],Db[i]))
    plt.legend(loc = 'best')
    plt.grid()
    plt.show()

    
oiginal_plots()
centroid_2()