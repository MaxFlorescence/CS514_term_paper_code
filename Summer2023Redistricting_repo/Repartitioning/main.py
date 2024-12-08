from redistricting import Redistricting
#from gerrychain import Graph
import os
from datetime import datetime

K = 7
TRIALS = 30
OUT = os.path.join('data', datetime.today().strftime("%Y-%m-%d"))
N_GRID = 56
N_TRI = 78

def main():
    #co_graph = Graph.from_file('../CO_graph/co_precincts.shp')
    updaters = ['cut edges', 'size disparity', 'size deviation', 'population disparity', 'population deviation', 'contiguous']
    
    for prop,steps in [("specrecom", 400), ("speckmeans", 1), ("revrecom", 40000)]:
        for i in range(TRIALS):
            desc = f"trial {i:02}"
            
            grid_graph(prop, desc, steps, updaters)
            triangular_graph(prop, desc, steps, updaters)
            #colorado_graph(co_graph, prop, desc, steps, updaters)
            
            if prop == "speckmeans": break
    
def grid_graph(prop: str, description: str, steps: int, updaters: list[str]):
    r = Redistricting(
        graph = "grid",
        k = K,
        assignment = "row",
        proposal = prop, # type: ignore
        steps = steps,
        single_updaters = updaters,
        h = N_GRID,
        w = N_GRID
    )
    r.run(
        plot_interval = 0 if prop=='speckmeans' else steps,
        output_parent = OUT,
        description = description
    )
    
def triangular_graph(prop: str, description: str, steps: int, updaters: list[str]):
    r = Redistricting(
        graph = "triangular",
        k = K,
        assignment = "row",
        proposal = prop, # type: ignore
        steps = steps,
        single_updaters = updaters,
        h = N_TRI,
        w = N_TRI
    )
    r.run(
        plot_interval = 0 if prop=='speckmeans' else steps,
        output_parent = OUT,
        description = description
    )
    
# def colorado_graph(co_graph: Graph, prop: str, description: str, steps: int, updaters: list[str]):
#     r = Redistricting(
#         graph = co_graph,
#         k = K,
#         assignment = "CD116FP",
#         proposal = prop, # type: ignore
#         steps = steps,
#         single_updaters = updaters,
#         population_key = 'TOTPOP',
#         graph_name = 'Colorado'
#     )
#     r.run(
#         plot_interval = 0 if prop=='speckmeans' else steps,
#         output_parent = OUT,
#         description = description
#     )
    
if __name__=='__main__':
    main()