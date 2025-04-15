"""Provide the primary functions."""
from .bitstring import *
import numpy as np
class coloring:
    def __init__(self, K, G = [[]]):
        """_summary_

        Args:
            K (_type_): Integer, number of colors
            G (list, optional): Adjacency matrix for nodes
        """
        self.K = K
        self.G = G
        self.Edges = []
        index = 0
        for i in range(len(self.G)):
            nodes = len(self.G[i])
            self.Edges.append(np.zeros(nodes, dtype=int))
            for j in range(i+1, nodes):
                self.Edges[index] = G[i][j]
                index += 1
        


