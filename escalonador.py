#!/usr/bin/env python
# -*- coding: utf-8 -*-

from inputReader import *
from heapq import *
import time

class Priority():
	def __init__(self,processos):
		self.processos = sorted(processos, key=lambda x: x.chegada)
	def run(self):
		clock = 0
		indiceProx = 0
		plista = []
		processoAtual = None
		inicioProcessoAtual = 0

		print "antes do while: "
		for i in self.processos:
			print "chegada: " + str(i.chegada)
			print "pid: " + str(i.pid)
			print "burst: " + str(i.burst)
			print "prioridade: " + str(i.prioridade)
			print " "

		time.sleep(3)
		while(True):

			proxChegada = self.processos[indiceProx]
			print "indiceProx do começo: " + str(indiceProx)
			print "proxChegada.chegada: " + str(proxChegada.chegada)
			print "proxChegada.pid: " + str(proxChegada.pid)
			print "clock: " + str(clock)
			time.sleep(1)

			if (proxChegada.chegada == clock):
				heappush(plista,(proxChegada.prioridade,proxChegada.chegada,proxChegada))
				print "tamanho da plista: " + str(len(plista))
				indiceProx = indiceProx + 1
				print "indiceProx: " + str(indiceProx)


			if ((processoAtual == None) and (plista)):
				a,b,processoAtual = heappop(plista)
				inicioProcessoAtual = clock
			elif (processoAtual != None):
				processoAtual.timeleft = processoAtual.timeleft - 1
				if (processoAtual.timeleft == 0):
					processoAtual.historico.append((inicioProcessoAtual,clock))
					processoAtual = None
				if (indiceProx == len(self.processos)):
					break

			clock = clock + 1

#class Escalonador():
#	def __init__(self,processos,algoritmo):
#		self.processos = processos
#		self.algoritmo = algoritmo
		

class Processo():
	def __init__ (self,inputrow):
		self.chegada = inputrow[0]
		self.pid = inputrow[1]
		self.burst = inputrow[2]
		self.prioridade = inputrow[3]
		self.timeleft = self.burst
		self.historico = []


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

	e = Priority(processlist)
	#e.run()

	

if __name__ == "__main__":
     main()