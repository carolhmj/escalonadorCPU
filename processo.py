#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Processo():
	"""Classe que representa um processo, e que guarda suas informações relevantes"""
	def __init__ (self,inputrow):
		self.chegada = inputrow[0]
		self.pid = inputrow[1]
		self.burst = inputrow[2]
		self.prioridade = inputrow[3]
		self.timeleft = self.burst
		self.historico = []
	def stringHistorico(self):
		"""Retorna uma string para visualização do histórico do processo"""
		s = ""
		for stamp in self.historico:
			s = s + "[inicio: " + str(stamp[0]) + " " + "final: " + str(stamp[1]) + "] "
		return s