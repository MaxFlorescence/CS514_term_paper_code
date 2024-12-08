import networkx as nx
from scipy import linalg as la
from typing import Any
from gerrychain.partition import Partition
import random

def repartition(partition: Partition) -> Partition:
    '''
        Returns a new partition by randomly recombining two parts and splitting them based on the fiedler_cut method.
    '''
    # Choose a random cut edge. partition['cut_edges'] is the set of edges that are cut by the partition,
    #   since random.choice() needs an index-able data structure, we convert it to a tuple first.
    cut_edge: tuple = random.choice(tuple(partition['cut_edges']))

    # Store the part indices that each endpoint of the two edges are in
    parts_to_merge = (partition.assignment[cut_edge[0]], partition.assignment[cut_edge[1]])
    
    # Merge the parts and get the subgraph on the merged nodes
    merged_nodes = [v for v in partition.graph.nodes if partition.assignment[v] in parts_to_merge]
    merged_subgraph = partition.graph.subgraph(merged_nodes).copy() # Making a new graph seems ESSENTIAL
    
    # Tell the chain to flip part indices to match the clusters obained above
    flips = fiedler_cut(merged_subgraph, parts_to_merge, randomize_weights=True)
    return partition.flip(flips)
    
def fiedler_cut(subgraph: nx.Graph,
                part_labels: tuple = (0, 1),
                randomize_weights: bool = False,
                normalize_laplacian: bool = False) -> dict:
    '''
        Assigns nodes in the subgraph to parts based on the sign of their corresponding value in the fiedler vector.
    '''
    node_list = list(subgraph.nodes)
    n = len(node_list)
        
    _, fv = fiedler(subgraph, randomize_weights, normalize_laplacian)
    
    # The partition is given by whether fv[x] >= 0.
    flips = {node_list[x]: part_labels[int(fv[x] >= 0)] for x in range(n)}
    return flips
    
def fiedler(graph: nx.Graph,
            randomize_weights: bool = False,
            normalize_laplacian: bool = False) -> tuple[float, Any]:
    '''
        Calculates the feidler value and vector for the given graph.
    '''
    if randomize_weights:
        # Make edge weight uniform random reals in the interval [0,1)
        for edge in graph.edges:
            graph.edges[edge]["weight"] = random.random() + 1

    # The Laplacian matrix of a graph is L = D - A, where A is the adjacency matrix and
    #   D is the diagonal matrix of node degrees.
    if normalize_laplacian:
        m = nx.normalized_laplacian_matrix(graph).todense()
    else:
        m = nx.laplacian_matrix(graph).todense()

    # Compute the eigenvectors corresponding to the first two eigenvalues
    eigvals, eigvecs = la.eigh(m, subset_by_index=[0,1])

    # The Fiedler vector is the one corresponding to the second eigenvalue, which 
    #   due to 0-based indexing is eigenvectors[:, 1]
    fval = eigvals[1]
    fvec = eigvecs[:, 1]
    
    return fval, fvec