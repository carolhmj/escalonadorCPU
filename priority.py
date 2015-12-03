#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import *
from inputReader import *
from outputWriter import *
from processo import Processo

class Priority(object):
	"""Classe que representa um escalonador de prioridade não-preemptivo.
	Ele recebe uma lista de processos, e define sua função de prioridade
	como a própria prioridade do processo"""

	def __init__(self,processos):
		self.processos = sorted(processos, key=lambda x: x.chegada)
	def prioridadeProcesso(self, processo):
		return processo.prioridade
	def run(self):
		clock = 0
		indiceProx = 0
		plista = []
		processoAtual = None
		inicioProcessoAtual = 0
		"""
		print "antes do while: "
		for i in self.processos:
			print "chegada: " + str(i.chegada)
			print "pid: " + str(i.pid)
			print "burst: " + str(i.burst)
			print "prioridade: " + str(i.prioridade)
			print " "
		"""
		while(True):

			if (indiceProx < len(self.processos)):
				proxChegada = self.processos[indiceProx]
				if (proxChegada.chegada == clock):
					proxChegada.timeleft = proxChegada.burst
					heappush(plista,(self.prioridadeProcesso(proxChegada), proxChegada.chegada, proxChegada))
					#print "tamanho da plista: " + str(len(plista))
					indiceProx = indiceProx + 1
					#print "indiceProx: " + str(indiceProx)			
			
			print "clock: " + str(clock) 

			if (processoAtual == None):
				print "não há um processo executando, vamos procurar um!"
				if (plista):
					print "temos uma lista de onde tirar!"
					a,b,processoAtual = heappop(plista)
					print "processo " + str(processoAtual.pid) + " começou!"	
					inicioProcessoAtual = clock

			if (processoAtual != None):
				print "executando o processo " + str(processoAtual.pid)
				processoAtual.timeleft = processoAtual.timeleft - 1
				print "falta " + str(processoAtual.timeleft) + " para ele acabar"

				clock = clock + 1
				if (processoAtual.timeleft == 0):
					processoAtual.historico.append((inicioProcessoAtual, clock))
					processoAtual = None
					if (indiceProx == len(self.processos) and not plista):
						break
			else:
				clock = clock + 1

			print "\n\n"

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
	e.run()
	reporter(sys.argv,processlist)

if __name__ == "__main__":
     main()	