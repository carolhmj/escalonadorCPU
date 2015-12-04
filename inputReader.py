#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sys


"""Leitor de inputs"""
class inputReader():
	def __init__(self,arquivo):
		self.arquivo = arquivo

	def executar(self): 
		r = []
		try:
		    reader = csv.reader(self.arquivo)
		    for row in reader:
				r.append(row)
		finally:
			self.arquivo.close()
			r = [[int(j) for j in i] for i in r]
			return r