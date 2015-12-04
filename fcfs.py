#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import *
from inputReader import *
from processo import Processo
from priority import *

class FCFS(Priority):
	"""Classe que representa um escalonador First Come First Serve. 
	Esse algoritmo executa os processos na ordem em que eles chegam. Ele
	é uma especialização do algoritmo Priority, com a prioridade constante 
	para todos os processos"""

	def __init__(self,processos):
		super(FCFS, self).__init__(processos)
	def prioridadeProcesso(self, processo):
		return 0

