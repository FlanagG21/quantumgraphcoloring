"""Provide the primary functions."""
from .bitstring import *
import matplotlib.pyplot as plt
import numpy as np
from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer

def color(k, G=[[]]):
    """_summary_

    Args:
        k (_type_): number of colors to color the graph
        G (list, optional): adjacency matrix of the graph to be colored.
    """
    sim = Aer.get_backend('qasm_simulator')
    circuit = circuitGenerator(k, G)
    job = sim.run(circuit, shots = 1000)
    counts = job.result().get_counts()
    print(counts)
    print('The solutions, if there are any, are the ones without', k,"leading 0's")
    print('n*k matrix can be rebuilt reading right to left, starting a new line every', k, "bits")



def circuitGenerator(nColors, G = [[]]):
    """_summary_

    Args:
        G (list, optional): Adjacency matrix for nodes
    Returns: 
        the circuit that will color the graph.
    """
    edges = getEdges(G)
    numNodes = len(G)
    nc = nColors + 1
    nn2=round((numNodes-1)*numNodes/2)
    sc=round(nc*numNodes)
    sg=round(nc*numNodes + nn2)
    nqbits=sc + 2*nn2
    q = QuantumRegister(nqbits)
    c=ClassicalRegister(nColors*numNodes)
    qc = QuantumCircuit(q,c)
    for n in range(nn2):
        if edges[n] == 1:
            qc.x(sg+n)
    s=0
    for n in range(numNodes):
        for k in range(nColors):
            qc.h(s+k)
        s=s+nc
    s=0
    for n in range(numNodes):
        for k in range(nColors-1):
            for l in range(k+1,nColors):
                qc.ccx (s+k,s+l,s+nColors)
                qc.cx (s+nColors,s+k)
                qc.reset(s+nColors)
        for k in range(nColors):
            qc.x(s+k) 
        cb=list(range(s,s+nColors) )
        qc.mcx (cb,s+nColors)
        for k in range(nColors):
            qc.x(s+k) 
        qc.cx (s+nColors,s+nColors-1)
        qc.reset(s+nColors)
        s=s+nc
    for k in range(nColors):
        s=nc*numNodes
        for n1 in range(numNodes-1):
            for n2 in range(n1+1,numNodes):
                n11=nc*n1+k 
                n22=nc*n2+k 
                qc.ccx(n11,n22,s) 
                s=s+1
    for n in range(sc,sc+nn2):
        for node in range(numNodes):
            qnode=nc*node
            qnc=qnode+nColors
        for k in range(nColors):
            cb=[n,n+nn2,qnode+k]
            qc.mcx (cb,qnc)
            cb=[n,n+nn2,qnc]
            qc.mcx (cb,qnode+k)
            qc.reset(qnc)
    cb=0
    for n in range(numNodes):
        s=n*(nColors+1)
        for k in range(nColors):
            qb=s+k
            qc.measure(qb,cb)
            cb=cb+1
    return qc



def getEdges(G = [[]]):
    """_summary_

    Args:
        G (list, optional): Adjacency matrix for nodes
    Returns: 
        a list of the Edges of the graph
    """
    edges = []
    for i in range(len(G)):
        nodes = len(G[i])
        for j in range(i+1, nodes):
            edges.append(G[i][j])
    return edges