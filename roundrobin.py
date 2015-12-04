#!/usr/bin/env python
# -*- coding: utf-8 -*-

from inputReader import *
from processo import Processo
from collections import deque

class RoundRobin(object):
	"""Classe que representa um algoritmo de escalonamento Round Robin. Esse algoritmo
	define uma fatia de tempo para a execução de cada processo. Caso um processo não termine
	a execução durante a fatia, ele é recolocado no final da fila de espera"""
	def __init__(self, processos, quantum):
		super(RoundRobin, self).__init__()
		self.processos = sorted(processos, key=lambda x: x.chegada)
		self.quantum = quantum
	def executar(self):
		clock = 0
		indiceProx = 0
		plista = deque()
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
					proxChegada.timeleft = proxChegada.burst
					plista.append(proxChegada)
					#Agora que já colocamos esse processo na heap, podemos investigar os próximos processos
					#na lista de processos que chegarão
					indiceProx = indiceProx + 1

			print "clock: " + str(clock)

			if (processoAtual == None):
				print "não há um processo executando, vamos procurar um!"
				if (plista):
					print "temos uma lista de onde tirar!"
					processoAtual = plista.popleft()
					print "processo " + str(processoAtual.pid) + " começou!"	
					inicioProcessoAtual = clock
				else:
					print "não achamos um processo!"
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
					if (clock - inicioProcessoAtual == self.quantum):
						"""Depois de executar o processo atual, pode ser que o quantum de tempo alocado a ele tenha
						acabado, logo iremos checar isso"""

						processoAtual.historico.append((inicioProcessoAtual, clock))
						plista.append(processoAtual)
						processoAtual = None
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

	e = RoundRobin(processlist,4)
	e.executar()

	for p in processlist:
		print p.stringHistorico()

if __name__ == "__main__":
    main()	