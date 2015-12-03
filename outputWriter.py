#!/usr/bin/env python
# -*- coding: utf-8 -*-

def processamentoTotal(processos):
	r = 0
	for p in processos:
		r = r + p.burst	
	return r

def taxaUtilizacao(processos,ptotal):
	ttotal = 0
	for p in processos: 
		aux = p.historico[-1][1]
		if (ttotal < aux):
			ttotal = aux
	return ((ptotal/ttotal)*10)

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
		if len(p.historico) == 1:
			pass
		else: 
			for i, h in enumerate(p.historico[1:]):
				esperatotal = esperatotal + (h[0] - p.historico[i-1][1])

	return (esperatotal/len(processos))


def reporter(header,processos):
	report = open("estatisticas.txt",'w')
	linha = '==================================================================== \nParâmetros de execução: ' + ' '.join(header) + '\n' + '====================================================================' + '\n'
	report.write(linha.format())
