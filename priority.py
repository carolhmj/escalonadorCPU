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
	def executar(self):
		clock = 0
		indiceProx = 0
		plista = []
		processoAtual = None
		inicioProcessoAtual = 0
	
		while(True):

			"""Verificamos o valor da lista de processos ordenados por
			tempo de chegada, para sabermos se o processo chegou nesse
			momento"""

			if (indiceProx < len(self.processos)):

				"""Insere o valor na heap. O critério de ordenação é primeiro a prioridade do processo,
					depois o tempo de chegada"""
				proxChegada = self.processos[indiceProx]

				"""Agora que já colocamos esse processo na heap, passamos a verificar o próximo processo que
					deve chegar"""
				if (proxChegada.chegada == clock):
					proxChegada.timeleft = proxChegada.burst
					heappush(plista,(self.prioridadeProcesso(proxChegada), proxChegada.chegada, proxChegada))
					indiceProx = indiceProx + 1
								
			
			if (processoAtual == None):
				if (plista):
					a,b,processoAtual = heappop(plista)
					inicioProcessoAtual = clock

			if (processoAtual != None):
				processoAtual.timeleft = processoAtual.timeleft - 1
				
				clock = clock + 1
				if (processoAtual.timeleft == 0):
					processoAtual.historico.append((inicioProcessoAtual, clock))
					processoAtual = None
					if (indiceProx == len(self.processos) and not plista):
						break
			else:
				clock = clock + 1

