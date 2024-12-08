import os
from gerrychain import Partition
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Any

SIZE_FACTOR = 6.697E-3

def draw_graph(is_custom: bool,
               partition: Partition,
               graph: nx.Graph,
               k: int,
               node_size: float,
               node_shape: str,
               show_graph: bool,
               file_name: str|None = None) -> None:
    '''
        If is_custom is True, then draws the partition's graph.
        Otherwise, draws the given graph using the k, node_size, and node_shape parameters, as well as the partition's assignment.
        
        If a filename is given, saves the plot to the file. Otherwise displays it.
    '''
    fig = plt.figure()
    
    if is_custom:
        partition.plot(cmap='tab20')
    else:
        nx.draw(
            G = graph,
            pos = nx.get_node_attributes(graph, 'pos'),
            node_color = [partition.assignment[n] for n in graph.nodes],
            cmap = 'tab20',
            vmin = 0,
            vmax = k-1,
            node_size = node_size,
            node_shape = node_shape
        )
        fig.gca().set_aspect("equal")
        
    if file_name != None:
        path, _ = os.path.split(file_name)
        if not os.path.exists(path):
            os.makedirs(path)
        
        plt.savefig(file_name)

    if show_graph:
        print("plt.show()")

    plt.close()

def grid_graph(n: int, m: int) -> tuple[nx.Graph, float]:
    '''
    Returns a tuple containing a graph and a node size.
    
    The graph is a networkx grid graph of size `n`x`m`, it's nodes have added properties with keys:
    - 'pos': cartesian coordinates of the node's position
    
    The node size is calculated based on the size of the graph.
    '''
    n = min(n, 10)
    m = min(m, 10)
    graph = nx.grid_graph((n, m))
    
    positions = {}
    labels = {}
    for i,v in enumerate(graph.nodes):
        i_str = str(i)
        positions[i_str] = v
        labels[v] = i_str
        
    nx.relabel_nodes(graph, labels, copy=False)
    nx.set_node_attributes(graph, positions, 'pos')
    nx.set_node_attributes(graph, 1, 'pop')
    
    size = int(n*m * SIZE_FACTOR)
    
    return graph, size

def triangular_graph(n: int, m: int) -> tuple[nx.Graph, float]:
    '''
    Returns a tuple containing a graph and a node size.
    
    The graph is a networkx triangular lattice graph of size `n`x`m`.
    The node size is calculated based on the size of the graph.
    '''
    n = min(n, 10)
    m = min(m, 10)
    graph = nx.triangular_lattice_graph(n, m)
    nx.relabel_nodes(graph, {v:str(i) for v,i in enumerate(graph.nodes)}, copy=False)
    nx.set_node_attributes(graph, 1, 'pop')
    
    size = int((n+1)*(m/2+1) * SIZE_FACTOR)
    
    return graph, size

def stripes(nodelist: list[Any],
            k: int,
            mapping: Callable[[Any], float]) -> dict[Any, int]:
    '''
        Returns an assignment that partitions `g.nodes` into `k` stripes based on the nodes' relative order under
        the `mapping`.
    '''
    values = np.array([mapping(v) for v in nodelist])
    unique_vals = np.unique(values)
    
    val_index = {x: i for i,x in enumerate(unique_vals)}
    scaling = k / (len(unique_vals)-1)
    
    rescale = lambda x, k: min(int(val_index[x] * scaling), k-1)
    return {nodelist[i]: rescale(values[i], k) for i in range(len(nodelist))}