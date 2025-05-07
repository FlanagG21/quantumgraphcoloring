"""
Unit and regression test for the quantumgraphcoloring package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer
import quantumgraphcoloring as qGC


def test_quantumgraphcoloring_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "quantumgraphcoloring" in sys.modules
    
def test_getEdges():
    """test of the getEdges method in quantumgraphcoloring
    """
    edges1 = qGC.getEdges([[0,1,1],[1,0,1],[1,1,0]])
    edges2 = qGC.getEdges([[0,1,0],[1,0,1],[0,1,0]])
    assert(edges1 == [1,1,1])
    assert(edges2 == [1, 0, 1])
    
def test_getColoringMatrix():
    """test of the getColoringMatrix method in quantumgraphcoloring
    """
    colorMatrix1 = qGC.getColoringMatrix(2, [1,0,0,1,1,0], [[0, 1, 0],[1, 0, 1], [0, 1, 0]])
    assert(colorMatrix1 == [[0,1],[1,0],[0,1]])\
        
def test_potentialColorings():
    c = qGC.potentialColors(2, [[0,1],[1,0]])
    c = set(c.keys())
    assert(c == set(['0001', '0110', '1001', '0010']))
