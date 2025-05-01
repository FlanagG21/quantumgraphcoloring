"""Provide the primary functions."""
from .bitstring import *
import numpy as np
from qiskit import *


def color(k, G = [[]]):
    """_summary_

    Args:
        G (list, optional): Adjacency matrix for nodes
    Returns: 
        a list of Edges
    """
    edges = getEdges(G)
    numNodes = len(G[0])
    startAncilas = (k + 1) * numNodes #sc
    numPairs = round((numNodes-1)*numNodes/2)
    startGraph = round((k + 1) * numNodes + numPairs) #sg
    q = QuantumRegister(startAncilas + 2*numPairs)
    c=ClassicalRegister(k*numNodes)
    circuit = QuantumCircuit(q,c)
    for n in range(numNodes):
        if edges[n] == 1:
            circuit.x(startGraph + n)
    a = 0
    for n in range(numNodes):
        for c in range(k):
            circuit.h(a+c)
        a=a+k
    s = 0
    for n in range(numNodes):
        for c in range(k - 1):
            for i in range(c + 1, k):
                circuit.ccx(s + c, s+i, s+k)
                circuit.cx(s+k, s+c)
                circuit.reset(s+k)
        for c in range(k):
            circuit.x(s+c)
        cb = list(range(s, s+k))
        circuit.mcx(cb, s+k)
        for c in range(k):
            circuit.x(s+k)
        circuit.cx(s+k, s+k-1)
        circuit.reset(s+k)
        s = s + k+1
    for c in range(k):
        s = (k+1) * numNodes
        for n1 in range(numNodes - 1):
            for n2 in range(n1 + 1,numNodes):
                n11 = (k+1) * n1 + c
                n22 = (k+1) *n2 + c
                circuit.ccx(n11,n22,s)
                s = s+1
    for n in range(startAncilas, startAncilas + numPairs):
        for node in range(numNodes):
            qnode = (k+1) * node
            qnc = qnode + k
            for c in range(k):
                cb = [n, n + numPairs, qnode + c]
                circuit.mcx(cb, qnc)
                cb = [n, n+numPairs, qnc]
                circuit.mcx(cb, qnode + c)
                circuit.reset(qnc)
    cb = 0
    for n in range(numNodes):
        s = n*k
        for c in range(k):
            qb = s +k
            circuit.measure(qb, cb)
            cb = cb+1
    print('end of measures')
    print(circuit)



def getEdges(G = [[]]):
    """_summary_

    Args:
        G (list, optional): Adjacency matrix for nodes
    Returns: 
        a list of Edges
    """
    edges = []
    index = 0
    for i in range(len(G)):
        nodes = len(G[i])
        edges.append(np.zeros(nodes, dtype=int))
        for j in range(i+1, nodes):
            edges[index] = G[i][j]
            index += 1
    return edges