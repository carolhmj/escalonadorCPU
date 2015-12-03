#!/usr/bin/env python
# -*- coding: utf-8 -*-

from escalonador import *
from heapq import *

"""Classe que representa um escalonador por prioridade preemptivo. 
Ele recebe uma lista de processos, e possui uma maneira de retornar as 
prioridades de determinado processo"""
class PriorityP():
	def __init__(self, processos):
		self.processos = sorted(processos, key=lambda x: x.chegada)
	def prioridadeProcesso(self, processo):
		return processo.prioridade
	def executar(self):
		clock = 0
		indiceProx = 0
		plista = []
		processoAtual = None
		inicioProcessoAtual = 0

		while (True):
			"""Verificamos o valor da lista de processos ordenados por
			tempo de chegada, para sabermos se o processo chegou nesse
			momento"""
			if (indiceProx < len(self.processos)):
				proxChegada = self.processos[indiceProx]
				if (proxChegada.chegada == clock):
					print "chegou o processo " + str(proxChegada.pid)
					#Insere o valor na heap. O critério de ordenação é primeiro a prioridade do processo,
					#depois o tempo de chegada
					heappush(plista, (self.prioridadeProcesso(proxChegada), proxChegada.chegada, proxChegada))
					#Agora que já colocamos esse processo na heap, podemos investigar os próximos processos
					#na lista de processos que chegarão
					indiceProx = indiceProx + 1

			print "clock: " + str(clock)

			if (processoAtual == None):
				print "não há um processo executando, vamos procurar um!"
				if (plista):
					print "temos uma lista de onde tirar!"
					a,b,processoAtual = heappop(plista)
					print "processo " + str(processoAtual.pid) + " começou!"	
					inicioProcessoAtual = clock
				else:
					print "não achamos um processo!"

			if (processoAtual != None):
				"""Antes de executar o processo atual, pode ser que precisemos interrompê-lo em
				favor de outro processo com maior prioridade. Logo, vamos ver se o processo
				do topo do heap tem mais prioridade que ele"""

				if (plista and (self.prioridadeProcesso(plista[0][2]) < self.prioridadeProcesso(processoAtual) ) ):
					print "processo " + str(processoAtual.pid) + " preemptado em favor do processo " + str(plista[0][2].pid)
					processoAtual.historico.append([inicioProcessoAtual, clock])

					a, b, processoAtual = heappushpop(plista, (self.prioridadeProcesso(processoAtual), processoAtual.chegada, processoAtual))
					inicioProcessoAtual = clock


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

	e = PriorityP(processlist)
	e.executar()

	for p in processlist:
		print p.stringHistorico()

if __name__ == "__main__":
    main()	