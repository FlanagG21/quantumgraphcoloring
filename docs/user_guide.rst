User Guide
===============

quantumgraphcoloring has two ways to obtain a coloring of a graph:
.. code-block:: python
    quantumgraphcoloring.potentialColors(k, G)

This method prints a list of potential k colorings of graph G, some of which will not fully color the graph
    Args:
        k (int): number of colors to color the graph
        G (list, optional): adjacency matrix of the graph to be colored. Defaults to [[]].
    Returns:
        a dictionary with the observed coloring encodings as keys, and the number of times observed at of 1000 runs as the values

In order to obtain a coloring take any one of the keys that does not have k leading zero's and read right to left. 
Starting a new row every k bits.

alternatively you could run 
.. code-block:: python
    quantumgraphcoloring.getColoringMatrix(k, key, G)

to gets the n*k coloring matrix. 

    Args:
        k (int): the number of colors.
        key (list, optional):  a list of bits, in this case the key you wish to turn into the n*k coloring matrix
        G (list, optional): Adjacency matrix for the graph. Defaults to [[]].
    Returns:
        the n*k coloring matrix
to get the coloring matrix

The other way of getting a coloring is to use

.. code-block:: python
    quantumgraphcoloring.color(k, G)

which prints a colored graph

    Args:
        k (int): the number of colors to try
        G (list, optional): Adjacency matrix for the graph. Defaults to [[]].

If you wish to get the full quantum circuit used for coloring use:
.. code-block:: python
    quantumgraphcoloring.circuitGenerator(nColors, G = [[]])

This method generates a quantum circuit for coloring the graph G in nColors
    Args:
    
        G (list, optional): Adjacency matrix for the graph. Defaults to [[]].
    Returns: 
        the circuit that will color the graph.

lastly you can use:
.. code-block:: python
    getEdges(G = [[]])
    
to get the list of edges from the adjacency matrix G
    Args:
        G (list, optional): Adjacency matrix for nodes, Defaults to [[]].
    Returns: 
        a list of the Edges of the graph