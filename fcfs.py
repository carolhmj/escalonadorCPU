#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import *
from inputReader import *
from processo import Processo
from priority import *

class FCFS(Priority):
	"""Classe que representa um escalonador FCFS que herda de Priority"""

	def __init__(self,processos):
		super(FCFS, self).__init__(processos)
	def prioridadeProcesso(self, processo):
		return 0

