#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import *
from inputReader import *
from processo import Processo
from priority import *

class SJF(Priority):
	"""Classe que representa um escalonador FCFS que herda de Priority"""

	def __init__(self,processos):
		super(SJF, self).__init__(processos)
	def prioridadeProcesso(self, processo):
		return processo.timeleft


def main():
	f = open(sys.argv[1], 'rt')
	a = inputReader(f)
	processlist = []
	
	print a

	for row in a:
		processlist.append(Processo(row))
	"""
	for i in processlist:
		print "chegada: " + str(i.chegada)
		print "pid: " + str(i.pid)
		print "burst: " + str(i.burst)
		print "prioridade: " + str(i.prioridade)
		print " " """

	e = SJF(processlist)
	e.run()

if __name__ == "__main__":
     main()	
