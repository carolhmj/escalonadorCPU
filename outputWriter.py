#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

class outputWriter():
	def __init__(self,header,processos):
		self.processos = processos
		self.header = header
	def executar(self):
		report = open("estatisticas.txt",'a')
		linha = '==================================================================== \nParâmetros: ' + ' '.join(self.header) + '\n' + '====================================================================' + '\n'
		report.write(linha)
		
		self.processamentototal = self.processamentoTotal()
		self.tempototal = self.tempoTotal()
		
		linha = ( "{0:55} {1:10}".format("Tempo total de processamento:",self.processamentototal)) + '\n'
		report.write(linha)

		linha = ( "{0:55} {1:10.2f}".format("Percentual de utilizacao da CPU:",self.taxaUtilizacao())) + '%\n'
		report.write(linha)

		linha = ( "{0:55} {1:10.2f}".format("Media de throughput:",self.mediaVazao())) + '\n'
		report.write(linha)

		linha = ( "{0:55} {1:10.2f}".format("Media de turnaround:",self.mediaTurnaround())) + '\n'
		report.write(linha)

		linha = ( "{0:55} {1:10.2f}".format("Media de espera:",self.mediaEspera())) + '\n'
		report.write(linha)
		
		linha = ( "{0:55} {1:10.2f}".format("Media de resposta:",self.mediaResposta())) + '\n'
		report.write(linha)

		linha = ( "{0:55} {1:10.2f}".format("Media de trocas de contexto:",self.mediaTrocaContexto())) + '\n'
		report.write(linha)

		linha = ( "{0:55} {1:10}".format("Numero de processos:",self.numeroProcessos())) + '\n'
		report.write(linha)

	def processamentoTotal(self):
		r = 0
		for p in self.processos:
			r = r + p.burst	
		return r

	def tempoTotal(self):
		ttotal = 0
		for p in self.processos: 
			aux = p.historico[-1][1]
			if (ttotal < aux):
				ttotal = aux
		return ttotal

	def taxaUtilizacao(self):
		return ((self.processamentototal/self.tempototal)*100)

	def mediaVazao(self):
		return (len(self.processos)/self.tempototal)

	def mediaTurnaround(self):
		turntotal = 0

		for p in self.processos:
			turntotal = turntotal + (p.historico[-1][1] - p.chegada)

		return (turntotal/len(self.processos))

	def mediaEspera(self):
		esperatotal = 0
		for p in self.processos:
			esperatotal = esperatotal + (p.historico[0][0] - p.chegada)
			if len(p.historico) == 1:
				pass
			else:

				for i, h in enumerate(p.historico[1:], 1):
					esperatotal = esperatotal + (h[0] - p.historico[i-1][1])
		return (esperatotal/len(self.processos))

	def mediaResposta(self):
		respostatotal = 0
		for p in self.processos:
			respostatotal = respostatotal + (p.historico[0][0] - p.chegada)
		return (respostatotal/len(self.processos)) 

	def mediaTrocaContexto(self):
		trocatotal = 0
		for p in self.processos:
			trocatotal = trocatotal + len(p.historico) - 1
		return (trocatotal/len(self.processos))

	def numeroProcessos(self):
		return len(self.processos)
