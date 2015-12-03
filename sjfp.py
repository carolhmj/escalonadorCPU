#!/usr/bin/env python
# -*- coding: utf-8 -*-

from processo import Processo
from priorityP import PriorityP

class SJFP(PriorityP):
	"""Classe que representa um escalonador SJFP (Shortest Remaining Time First
	Preemptive). Ele é uma especialização do algoritmo PriorityP, e define a 
	prioridade de um processo como o tempo restante de execução"""
	def __init__(self, processos):
		super(SJFP, self).__init__(processos)
	def prioridadeProcesso(self, processo):
		return processo.timeleft

def main():
	f = open(sys.argv[1], 'rt')
	a = inputReader(f)
	processlist = []
	
	#print a

	for row in a:
		processlist.append(Processo(row))
	"""
	for i in processlist:
		print "chegada: " + str(i.chegada)
		print "pid: " + str(i.pid)
		print "burst: " + str(i.burst)
		print "prioridade: " + str(i.prioridade)
		print " " """

	e = SJFP(processlist)
	e.executar()

	for p in processlist:
		print p.stringHistorico()

if __name__ == "__main__":
    main()	
