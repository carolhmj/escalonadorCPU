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
			r.append(row)
	finally:
		f.close()
		r = [[int(j) for j in i] for i in r]
		return r
