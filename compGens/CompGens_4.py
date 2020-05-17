# CompGens4.py
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
import FunctionsCompGens as fn

if __name__ == "__main__":
    fn.clean_1()
    
    arq1 = input('file 01: .txt > ')
    file1 = '.\\data\\' + arq1 + '.txt'
    print(file1)
    
    arq2 = input('file 02: .txt > ')
    file2 = '.\\data\\' + arq2 + '.txt'
    print(file2)
    
    gene1=fn.count_words(file1)
    gene2=fn.count_words(file2)

    num_base_1 = len(gene1)
    num_base_2 = len(gene2)
    
    if num_base_1 >= num_base_2:
        tot = num_base_1 
    else:
        tot = num_base_2
        
    print('arq1 num_base > ',num_base_1)
    print('arq2 num_base > ',num_base_2)
    print('tot > ',tot)
    
    pg.init()
    
    #screen_1 = [1780, 560]
    #screen_1 = [1280, 560]
    screen_1 = [900, 560]
    #screen_1 = [640, 680]

    screen = pg.display.set_mode(screen_1, 0, 32)
    screen.fill((100, 100, 100))
  
    x=2
    y=0
    direc='R'

    a1=0; c1=0; g1=0; t1=0; n1=0
    c = 0
    ct = 0
    g1_err = {}
    g2_err = {}
    diff = {}
    
    for n in range(tot):
        
        f_g1_err = False
        f_g2_err = False
        
        ct+=1
        
        fn.check_events()
        
        if  n < len(gene1):
            b1 = gene1[n]
        else:
            b1 = None
            
        if  n < len(gene2):
            b2 = gene2[n]
        else:
            b2 = None
 
        b1, g1_err, f_g1_err = fn.test_b1(b1, g1_err, f_g1_err, n)
            
        b2, g2_err, f_g2_err = fn.test_b2(b2, g2_err, f_g2_err, n)
            
        color, diff = fn.color_dif(b1, b2, f_g1_err, f_g2_err, diff, n)
        
        c, x = fn.increm(direc, c, x)
        
        pos = fn.cursor(x,y) 
        
        for i in range(1,17):
             screen.set_at(pos[i], color)

        pg.display.update()
    
        tot_scr = screen_1[0]
        
        c, y, direc, x = fn.way(c, y, direc, x, tot_scr)
    
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                
                for _ in range(5):
                    print()
                
                print(ct) 
                print('g1 err > ',g1_err)
                print('g2 err > ',g2_err)
                print('diff >', diff)
                print('diff >',len(diff))
                
                e=input('input q to exit > ')
                
                if e=='q':
                    for _ in range(5):
                        print()
                    exit()
                    


