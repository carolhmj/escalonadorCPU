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


def selecionarAlgoritmo(args,processos):
	try:
		nomeAlgoritmo = args[2].lower()
	except IndexError:
		print "Algoritmo não especificado\nFinalizando..."
		sys.exit()
	if nomeAlgoritmo == "priority":
		return Priority(processos)
	elif nomeAlgoritmo == "priorityp":
		return PriorityP(processos)
	elif nomeAlgoritmo == "fcfs":
		return FCFS(processos)
	elif nomeAlgoritmo == "sjf":
		return SJF(processos)
	elif nomeAlgoritmo == "sjfp":
		return SJFP(processos)
	elif nomeAlgoritmo == "rr":
		try:
			return RoundRobin(processos,int(args[3]))
		except IndexError:
			print "Defina o quantum (terceiro argumento) para o algoritmo RoundRobin\nFinalizando..."
			sys.exit()
		except ValueError:
   			print "Valor do quantum não é um inteiro\nFinalizando"
			sys.exit()
	 
	print "Algoritmo não existe\nFinalizando..."
	sys.exit()

def main():
	try:
		f = open(sys.argv[1], 'rt')
	except IOError:
		print "O arquivo de entrada não existe.\nFinalizando..."
		sys.exit()
	reader = inputReader(f)
	a = reader.executar()
	processos = []
	for row in a:
		processos.append(Processo(row))

	algoritmo = selecionarAlgoritmo(sys.argv,processos)
	
	algoritmo.executar()

	reporter = outputWriter(sys.argv,processos)
	reporter.executar()

if __name__ == "__main__":
     main()	
