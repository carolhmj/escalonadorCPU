#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import *
from inputReader import *
from processo import Processo
from priority import *

class SJF(Priority):
	"""Classe que representa um algoritmo de escalonamento Shortest Job First. Esse algoritmo
	executa o processo que está mais próximo de terminar."""

	def __init__(self,processos):
		super(SJF, self).__init__(processos)
	def prioridadeProcesso(self, processo):
		return processo.timeleft
