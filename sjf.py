#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import *
from inputReader import *
from processo import Processo
from priority import *

class SJF(Priority):
	"""Classe que representa um escalonador FCFS que herda de Priority"""

	def __init__(self,processos):
		super(SJF, self).__init__(processos)
	def prioridadeProcesso(self, processo):
		return processo.timeleft