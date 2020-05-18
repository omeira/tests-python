# FunctionsGeraCores.py
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
        print(num_words)
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

