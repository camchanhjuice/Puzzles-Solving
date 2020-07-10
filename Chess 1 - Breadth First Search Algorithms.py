# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 04:22:54 2020

@author: PC
"""

import numpy as np
import random as rd
class Board:
    
    def __init__(self,size,start,end,stops): #Start and stop coordinate
        
        self.size = size
        self.end = end
        self.stops = stops
        self.start = start
    
    def chessboard(self):
        rd.seed(20)
        create = np.asarray(a= [0]*self.size*self.size)
        for x in range(self.stops):
            A = rd.randrange(0,len(create))
            create[A] = 1
        create = create.reshape(self.size,self.size)
        create[self.start[0]][self.start[1]] = 2
        create[self.end[0]][self.end[1]] = 3
        return create

    def find_solution(self):
        ''' Possible moves '''
        moves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
        paths = [[self.start[0],self.start[1]]]
        exists = [[self.start[0],self.start[1]]]
        n = 0
        
        while [self.end[0], self.end[1]] not in exists:
            n += 1
        
            for move in moves:
                
                if move[0] + paths[0][0] >= 0\
                and move[0] + paths[0][0] <= self.size -1\
                and move[1] + paths[0][1] >= 0\
                and move[1] + paths[0][1] <= self.size -1:
                
                #print(move)
                    if [paths[0][0]+move[0],paths[0][1]+move[1]] not in exists:
                        oke =[paths[0][0]+move[0],paths[0][1]+move[1]]
                        #print(oke)
                        if self.chessboard()[oke[0]][oke[1]] == 0 \
                            or self.chessboard()[oke[0]][oke[1]] == 3:
                            exists.append(oke)
                            paths.append(oke)
                            #print(oke)
                            #print(oke)
                            
            paths.remove(paths[0])
            exists.append(n)
            
                            
            
        return exists

        
    
new = Board(6,(0,0),(4,4),10)
print(new.chessboard())
print(new.find_solution())
            