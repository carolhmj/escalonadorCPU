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
