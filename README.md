# escalonadorCPU

##Simulador de vários algoritmos de escalonamento de CPU em Python.
Algoritmos implementados:
- Priority
- Priority Preemptive
- First Come, First Served
- Round Robin
- Shortest Job First
- Shortest Job First Preemptive

##Como executar:
    python escalonador.py [algoritmo] [quantum]

onde [algoritmo] pode ser:
- priority
- priorityp
- fcfs
- fjs
- fjsp
- rr

e [quantum] é um inteiro, aplicável somente ao algoritmo Round Robin.

##Saída
A saída do programa é um relatório acumulado no arquivo "estatisticas.txt" da pasta raiz. Se o arquivo não existe, é criado. Se existe, o novo relatório é adicionado no final.
Exemplo de relatório de uma execução:
````
==================================================================== 
Parâmetros: escalonador.py tests/input.txt priority
====================================================================
Tempo total de processamento:                                    8
Percentual de utilizacao da CPU:                            100.00%
Media de throughput:                                          0.38
Media de turnaround:                                          3.67
Media de espera:                                              1.00
Media de resposta:                                            1.00
Media de trocas de contexto:                                  0.00
Numero de processos:                                             3
````
