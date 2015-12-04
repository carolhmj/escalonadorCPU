#!/usr/bin/env python
# -*- coding: utf-8 -*-

from processo import Processo
from inputReader import *
from heapq import *

class PriorityP(object):
	"""Classe que representa um escalonador por prioridade preemptivo. 
	Ele recebe uma lista de processos, e define sua função de prioridade
	como a própria prioridade do processo"""

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

					"""Insere o valor na heap. O critério de ordenação é primeiro a prioridade do processo,
					depois o tempo de chegada"""
					heappush(plista, (self.prioridadeProcesso(proxChegada), proxChegada.chegada, proxChegada))

					"""Agora que já colocamos esse processo na heap, passamos a verificar o próximo processo que
					deve chegar"""
					indiceProx = indiceProx + 1


			if (processoAtual == None):
				if (plista):
					a,b,processoAtual = heappop(plista)
					inicioProcessoAtual = clock

			if (processoAtual != None):
				"""Antes de executar o processo atual, pode ser que precisemos interrompê-lo em
				favor de outro processo com maior prioridade. Logo, vamos ver se o processo
				do topo do heap tem mais prioridade que ele"""

				if (plista and (self.prioridadeProcesso(plista[0][2]) < self.prioridadeProcesso(processoAtual) ) ):
					processoAtual.historico.append([inicioProcessoAtual, clock])

					a, b, processoAtual = heappushpop(plista, (self.prioridadeProcesso(processoAtual), processoAtual.chegada, processoAtual))
					inicioProcessoAtual = clock


				processoAtual.timeleft = processoAtual.timeleft - 1
				
				clock = clock + 1
				if (processoAtual.timeleft == 0):
					processoAtual.historico.append((inicioProcessoAtual, clock))
					processoAtual = None
					if (indiceProx == len(self.processos) and not plista):
						break
			else:
				clock = clock + 1

			

