#!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv
import sys

def inputReader(arquivo): 
	f = arquivo
	r = []
	try:
	    reader = csv.reader(f)
	    for row in reader:
	    	row2 = []
	    	for i in row:
	    		row2.append(int(i))
			r.append(row2)
	finally:
		f.close()
		return r
