#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import *
from inputReader import *
from processo import Processo
from priority import *

class FCFS(Priority):
	"""Classe que representa um escalonador FCFS que herda de Priority"""

	def __init__(self,processos):
		super(FCFS, self).__init__(processos)
	def prioridadeProcesso(self, processo):
		return 0


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

	e = FCFS(processlist)
	e.run()
	reporter (sys.argv, processlist)

if __name__ == "__main__":
     main()	
