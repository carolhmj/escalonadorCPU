#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division


def processamentoTotal(processos):
	r = 0
	for p in processos:
		r = r + p.burst	
	return r

def tempoTotal(processos):
	ttotal = 0
	for p in processos: 
		aux = p.historico[-1][1]
		if (ttotal < aux):
			ttotal = aux
	return ttotal

def taxaUtilizacao(ptotal,ttotal):
	return ((ptotal/ttotal)*100)

def mediaVazao(processos,ttotal):
	return (len(processos)/ttotal)

def mediaTurnaround(processos):
	turntotal = 0
	for p in processos:
		turntotal = turntotal + (p.historico[-1][1] - p.historico[0][0])

	return (turntotal/len(processos))

def mediaEspera(processos):
	esperatotal = 0
	for p in processos:
		esperatotal = esperatotal + (p.historico[0][0] - p.chegada)
		if len(p.historico) == 1:
			pass
		else:
			for i, h in enumerate(p.historico[1:]):
				esperatotal = esperatotal + (h[0] - p.historico[i-1][1])
				

	return (esperatotal/len(processos))

def mediaResposta(processos):
	respostatotal = 0
	for p in processos:
		respostatotal = respostatotal + (p.historico[0][0] - p.chegada)
	return (respostatotal/len(processos)) 

def mediaTrocaContexto(processos):
	trocatotal = 0
	for p in processos:
		trocatotal = trocatotal + len(p.historico) - 1
	return (trocatotal/len(processos))

def numeroProcessos(processos):
	return len(processos)

def outputWriter(header,processos):
	report = open("estatisticas.txt",'a')
	linha = '==================================================================== \nParâmetros: ' + ' '.join(header) + '\n' + '====================================================================' + '\n'
	report.write(linha)
	
	processamentototal = processamentoTotal(processos)
	tempototal = tempoTotal(processos)
	
	linha = ( "{0:55} {1:10}".format("Tempo total de processamento:",processamentototal)) + '\n'
	report.write(linha)

	linha = ( "{0:55} {1:10.2f}".format("Percentual de utilizacao da CPU:",taxaUtilizacao(processamentototal,tempototal))) + '%\n'
	report.write(linha)

	linha = ( "{0:55} {1:10.2f}".format("Media de throughput:",mediaVazao(processos,tempototal))) + '\n'
	report.write(linha)

	linha = ( "{0:55} {1:10.2f}".format("Media de turnaround:",mediaTurnaround(processos))) + '\n'
	report.write(linha)

	linha = ( "{0:55} {1:10.2f}".format("Media de espera:",mediaEspera(processos))) + '\n'
	report.write(linha)
	
	linha = ( "{0:55} {1:10.2f}".format("Media de resposta:", mediaResposta(processos))) + '\n'
	report.write(linha)

	linha = ( "{0:55} {1:10.2f}".format("Media de trocas de contexto:", mediaTrocaContexto(processos))) + '\n'
	report.write(linha)

	linha = ( "{0:55} {1:10}".format("Numero de processos:", numeroProcessos(processos))) + '\n'
	report.write(linha)
	
	report.write("\n\n")