# FunctionsCompGens.py
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
import sys
import pygame as pg

def clean_1():
    for _ in range(5):
        print()

def count_words(filename):
    try:
        with open(filename, 'r') as f_obj:
            contents = f_obj.read()
        
    except  FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
        exit()
 
    else:
        words = contents.split()
        
        gene = []
        gene1 = []
        
        for w in(words):
            if w.isalpha() and w.islower():
                gene.append(w)
                for b in w:
                    gene1.append(b) 
        
        num_words = len(words)
        #print(num_words)
        #print(gene1)
        return gene1

def color_nuc(g):
    
    if g == 'a':            #adenine
        color = (0,0,255)   #blue
    elif g == 'c':          #cytosine
        color = (255,0,0)   #red
    elif g == 'g':          #guanine
        color = (0,255,0)   #green
    elif g == 't':          #thymine
        color = (255,255,0) #yellow
    else:
        color = (0,0,0)     #black
        print('err', g)     
        
    return color

def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

def cursor(x,y):
    pos={1:(x,y),2:(x+1, y),3:(x, y+1),4:(x+1, y+1),5:(x+1, y+2),
         6:(x+2, y),7:(x+2, y+1),8:(x+2, y+2),9:(x, y+2),10:(x, y+3),
         11:(x+1, y+3),12:(x+2, y+3),13:(x+3, y+3),14:(x+3, y),
         15:(x+3, y+1),16:(x+3, y+2)}
    return pos

def color_dif(b1,b2,f_g1_err,f_g2_err,diff,n):
 
    if b1 == b2 and b1 != None and b2 != None:
        color = (0,255,0)    #green
        
    elif b1 != b2 and b1 != None and b2 != None:
        color = (255,0,0)    #red
        diff[n] = (b1,b2)

    elif b1 == None and b2 != None and  not f_g1_err and not f_g2_err:
        color = (255,255,0)  #yellow

    elif b1 != None and b2 == None and  not f_g1_err and not f_g2_err:
        color = (255,255,0)  #yellow
            
    elif b1 == None or b2 == None and f_g1_err or f_g2_err:
        color = (0,0,0)      #black
        f_g1_err = False
        f_g2_err = False

    return color, diff

def test_b1(b1, g1_err, f_g1_err, n):
    
    if (b1 != 'a' and b1 != 'g' and b1 != 't' and b1 != 'c' 
                  and b1 != None):
        g1_err[n] = b1 
        b1 = None
        f_g1_err = True
        
    return  b1, g1_err, f_g1_err    
        
 
def test_b2(b2, g2_err, f_g2_err, n):
       
    if (b2 != 'a' and  b2 != 'g' and b2 != 't' and b2 != 'c' 
                  and b2 != None):
        g2_err[n] = b2 
        b2 = None
        f_g2_err = True
            
    return  b2, g2_err, f_g2_err  


def increm(direc, c, x):
    
    if direc == 'R':
        c+=1
        x+=4
    elif direc == 'L':
        c-=1
        x-=4
    return c, x


def way(c, y, direc, x, tot_scr):
    
    tot_x = int((tot_scr/4)-4)
   
    if c > tot_x:
        y+=4
        direc='L'
        x+=4
         
    elif c < 1:
        y+=4
        direc='R'
        x-=4
    return c, y, direc, x
