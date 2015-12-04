#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from heapq import *
from inputReader import *
from outputWriter import *
from processo import Processo
from roundrobin import RoundRobin
from sjf import SJF
from priorityP import PriorityP
from priority import Priority
from fcfs import FCFS
from sjfp import SJFP

class Escalonador():

	def __init__(self, args):
		self.args = args
		self.processos = []
		self.algoritmo = self.selecionarAlgoritmo()

	def executar(self):
		try:
			f = open(self.args[1], 'rt')
		except IOError:
			print "O arquivo de entrada não existe.\nFinalizando..."
			sys.exit()
		reader = inputReader(f)
		a = reader.executar()

		for row in a:
			self.processos.append(Processo(row))

		algoritmo = selecionarAlgoritmo()
		
		algoritmo.executar()

		reporter = outputWriter(self.args,self.processos)
		reporter.executar()

	def selecionarAlgoritmo(self):
		try:
			nomeAlgoritmo = self.args[2].lower()
		except IndexError:
			print "Algoritmo não especificado\nFinalizando..."
			sys.exit()
		if nomeAlgoritmo == "priority":
			return Priority(self.processos)
		elif nomeAlgoritmo == "priorityp":
			return PriorityP(self.processos)
		elif nomeAlgoritmo == "fcfs":
			return FCFS(self.processos)
		elif nomeAlgoritmo == "sjf":
			return SJF(self.processos)
		elif nomeAlgoritmo == "sjfp":
			return SJFP(self.processos)
		elif nomeAlgoritmo == "rr":
			try:
				return RoundRobin(self.processos,int(self.args[3]))
			except IndexError:
				print "Defina o quantum (terceiro argumento) para o algoritmo RoundRobin\nFinalizando..."
				sys.exit()
			except ValueError:
	   			print "Valor do quantum não é um inteiro\nFinalizando"
				sys.exit()
		 
		print "Algoritmo não existe\nFinalizando..."
		sys.exit()

if __name__ == "__main__":
     e = Escalonador(sys.argv)
     e.executar
