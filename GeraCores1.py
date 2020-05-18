# GeraCores1.py
# Copyright 2020 Octavio Nogueira
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# encoding: utf-8
from typing import Tuple, List
import pygame as pg
from sys import exit
import FunctionsGeraCores as fn

if __name__ == "__main__":
    arq = input('file name: .txt > ')
    
    filename = '.\\data\\' + arq + '.txt'
    
    gene1=fn.count_words(filename)

    num_base = len(gene1)
    print(num_base)

    pg.init()
    
    s_x = 900
    s_y = 560
    
    screen = pg.display.set_mode((s_x, s_y), 0, 32)
    screen.fill((100, 100, 100))
  
    x=2
    y=0
    direc='R'

    a1=0; c1=0; g1=0; t1=0; n1=0
    c = 0
    ct = 0
    
    for g in gene1:
        
        ct+=1
        
        fn.check_events()
    
        color = fn.color_nuc(g)
        
        if g == 'a':            #adenine
            a1+=1
        elif g == 'c':          #cytosine
            c1+=1
        elif g == 'g':          #guanine
            g1+=1
        elif g == 't':          #thymine
            t1+=1
        else:
            n1+=1               #err
            print('err', ct)
            
        if direc == 'R':
            c+=1
            x+=4
        elif direc == 'L':
            c-=1
            x-=4
        
        pos = fn.cursor(x,y) 
        
        for i in range(1,17):
             screen.set_at(pos[i], color)

        pg.display.update()
    
        if c > (s_x/4)-4:
            y+=4
            direc='L'
            x+=4
         
        elif c < 1:
            y+=4
            direc='R'
            x-=4
            
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                
                for _ in range(5):
                    print()
                
                print('adenine a: '+str(a1), 'cytosine c: '+str(c1),
                        'guanine g: '+str(g1), 'thymine t: '+str(t1),
                        'invalid: '+str(n1),'tot: '+str(a1+c1+g1+t1))
                
                e=input('input q to exit > ')
                
                if e=='q':
                    for _ in range(5):
                        print()
                    exit()
                    
