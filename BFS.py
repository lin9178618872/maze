# -*- coding: utf-8 -*-
"""
Created on Sat May  8 19:24:19 2021



import numpy as np
#In maze, 0 represent the wall,which mean we cannot go
#8represent the access, and 1 represent we can go
#888 means the exit
maze = '''
0	0	0	0	0	0	0	0	0	0
0	8	1	0	1	1	1	0	0	0
0	1	1	0	1	1	1	0	888	0
0	1	1	1	1	0	0	1	1	0
0	1	0	0	0	1	1	1	1	0
0	1	1	1	0	1	0	1	1	0
0	1	0	1	1	1	0	1	1	0
0	1	0	0	0	1	0	1	1	0
0	0	1	1	1	1	1	1	1	0
0	0	0	0	0	0	0	0	0	0'''
data = np.array(maze.split(), dtype = int).reshape((10,10))
 
 
def four_dir(data):
    """
    this function is to find the data that the place never go, and record where it go
    """
    path = {}
    a, b = np.where(data > 0)
    for x,y in zip(a, b):
        index = str(x) + str(y)
        if data[x, y+1] > 0:            #whether it can go we the east or not
            path[index] = [str(x)+str(y+1)]
        if data[x+1, y] > 0:            #whether it can go we the south or not
            if index in path:
                path[index] += [str(x+1)+str(y)]
            else:
                path[index] = [str(x+1)+str(y)]
        #data[i, j-1]
        if data[x, y-1] > 0:            #whether it can go we the west or not
            if index in path:
                path[index] += [str(x)+ str(y-1)]
            else:
                path[index] = [str(x)+ str(y-1)]
        #data[i-1, j]
        if data[x-1, y] > 0:            #whether it can go we the north or not
            if index in path:
                path[index] += [str(x-1)+str(y)]
            else:
                path[index] = [str(x-1) +str(y)]
    return path
 
def move_on(exit_index):
    save = ['11']   # save the first level information
    while True:     
        save_sec = []      #save the scond level information
        for index in save: #save the arrivial location, and save to layer_sec
            save_sec += direction[index]
            if exit_index in direction[index]:
                forward_step = index
        if exit_index in save_sec: break
        save = save_sec
    return forward_step
 
if __name__ == '__main__':
    direction = four_dir(data)
    
    goal = ['28']
    while True:
        forward_step = move_on(goal[-1])
        goal += [forward_step]
        if forward_step == '11':
            break
    step = goal[::-1][:-1]
    for ind in step:
        data[int(ind[0]), int(ind[1])] = -8
    print(data)
    print(step)
