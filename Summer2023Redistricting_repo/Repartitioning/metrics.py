from gerrychain.partition import Partition
from gerrychain.updaters import cut_edges
import networkx as nx
import numpy as np
from typing import Callable, Any

def cut_edge_count(partition: Partition) -> int:
    return len(cut_edges(partition))
            
def disparity(partition: Partition, use_population: bool = False) -> float:
    '''
    Computes the maximum disparity of the `partition`.
    
    This equals the size of the largest part divided by the size of the smallest part.
    '''
    max_part, min_part = extreme_parts(partition, use_population)
    return max_part/min_part

def deviation(partition: Partition, target: float, use_population: bool = False) -> float:
    '''
    Computes the deviation from target of the `partition`.
    
    This equals the maximum distance of any part from the target divided by the ideal.
    '''
    parts = extreme_parts(partition, use_population)
    return max(abs(p - target) for p in parts) / target
    
def extreme_parts(partition: Partition, use_population: bool = False) -> tuple[int, int]:
    '''
    Returns the sizes of the largest and smallest parts of the partition.
    '''
    max_part = -1
    min_part = partition.graph.order() + 1
    
    for part in partition.parts.values():
        size = len(part) if not use_population else sum(
            partition.graph.nodes[n]['pop'] for n in part
        )
        
        if max_part < size:
            max_part = size
        if min_part > size:
            min_part = size
            
    return max_part, min_part

def contiguous(partition: Partition):
    '''
    Implementation of `gerrychain.constraints.contiguous` since that seems to crash a lot.
    '''
    for part in partition.parts.values():
        if not nx.is_connected(partition.graph.subgraph(part)): # type: ignore
            return False
        
    return True

def producing_spanning_trees(partition: Partition, log: bool = True) -> float|int:
    # Clelland et al's P_D for arbitrary k
    '''
    Counts the number of producing spanning trees of the `partition`.
    
    A "producing spanning tree" of a k-partition is a spanning tree of the partition's parent graph for which cutting
    exactly k-1 edges results in the partition.
    
    If `log` is true, returns the natural logarithm of the count.
    '''
    return -1
    # factors = []
    
    # # number of spanning trees in each part
    # for part in partition.parts:
    #     subgraph = partition.graph.subgraph(part)
    #     T = round(nx.total_spanning_tree_weight(subgraph, weight=None)) # type: ignore
    #     factors.append(T)
    
    # # number of ways to split a full spanning tree into the parts
    # part_graph = nx.MultiGraph([
    #     (partition.assignment[u], partition.assignment[v])
    #     for u,v in filter(partition.crosses_parts, partition.graph.edges)
    # ])
    # T = round(nx.total_spanning_tree_weight(part_graph, weight=None))
    # factors.append(T)
    
    # if log:
    #     return np.sum(np.log(factors), dtype=float)
    # else:
    #     return np.prod(factors, dtype=int)

def round(n: float) -> int:
    return int(n + 0.5)

def map_to_updater(name: str,
                   target_size: float|None = None,
                   target_population: float|None = None) -> Callable[[Partition], Any]:
    if name == 'cut edges':
        return cut_edge_count
    elif name == 'size disparity':
        return disparity
    elif name == 'population disparity':
        return lambda p: disparity(p, use_population=True)
    elif name == 'size deviation':
        if target_size == None:
            raise Exception(f'target_size parameter must be defined for updater "{name}"!')
        return lambda p: deviation(p, target_size)
    elif name == 'population deviation':
        if target_population == None:
            raise Exception(f'target_population parameter must be defined for updater "{name}"!')
        return lambda p: deviation(p, target_population, use_population=True)
    elif name == 'contiguous':
        return contiguous
    elif name == 'producing spanning trees':
        return lambda p: producing_spanning_trees(p, log=False)
    elif name == 'log producing spanning trees':
        return producing_spanning_trees
    else:
        raise Exception(f'Unknown updater "{name}"!')

available = [
    'cut edges', 'size disparity', 'population disparity', 'size deviation', 'population deviation', 'contiguous',
    'producing spanning trees', 'log producing spanning trees'
]