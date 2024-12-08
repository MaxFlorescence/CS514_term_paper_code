import matplotlib.pyplot as plt
import json, os, sys
import scipy as sp
        
def filter_scale(data, key, filters=[], scale=1.0) -> tuple[list, float, float]:
    ret = []
    minVal = None
    maxVal = None
    
    for i,v in enumerate(data[key]):
        if all([data[k][i] == v for k,v in filters]):
            val = v*scale
            if minVal == None or minVal > val: minVal = val
            if maxVal == None or maxVal < val: maxVal = val
            ret.append(val)
            
    if minVal == None or maxVal == None: minVal = maxVal = 0
    
    return ret, minVal, maxVal

def load_data(path, derive_metrics=[]):
    with open(os.path.abspath(path), 'r') as f:
        data = json.load(f)
    
    for input_keys, output_key, function in derive_metrics:
        data[output_key] = [
            function(*[data[k][i] for k in input_keys])
            for i in range(data['n'])
        ]
        
    return data

alg_color = {
    "DYNAMOSA": "lightskyblue",
    "MIO": "plum",
    "RANDOM": "yellowgreen",
    "WHOLE_SUITE": "navajowhite"
}

def plot_box(variable, varName, algorithms, outName, file):
    data = load_data(file, derive_metrics=[
        (["mutants_generated", "mutants_surviving"], "mutants_killed", lambda g,s: g-s),
        (["mutants_generated", "mutants_killed"], "mutation_score", lambda g,k: k/g if g != 0 else 0)
    ] if file=="all_data.json" else [])
    
    if algorithms == []:
        algorithms = sorted(list(set(data['algorithm']))) # ["DYNAMOSA", "MIO", "WHOLE_SUITE", "RANDOM"]
        
    variable_data = [
        filter_scale(data, variable, [("algorithm", a)])[0]
        for a in algorithms
    ]
    
    fig, ax = plt.subplots()
    title = f'{varName} vs Algorithm'
    ax.set_ylabel(varName)
    ax.set_xlabel('Algorithm')
    
    for i,a in enumerate(algorithms):
        redist_values = [v for v in filter_scale(data, variable, [("algorithm", a), ("project", "redistricting")])[0]]
        if len(redist_values) == 0: continue
        
        redist_y = sp.ndimage.median(redist_values)
        redist_x = [i+1]
        ax.scatter(redist_x, redist_y, marker="x", color="red", zorder=2)

    bplot = ax.boxplot(x=variable_data, patch_artist=True, labels=algorithms, zorder=1)
    for patch, color in zip(bplot['boxes'], [alg_color[a] for a in algorithms]):
        patch.set_facecolor(color)
        
    for median in bplot['medians']:
        median.set_color('red')
    
    fig.suptitle(title)
    fig.set_layout_engine("tight")
    
    save_path = os.path.join('figures', outName)
    fig.savefig(os.path.abspath(save_path))
    
def u_test(variable, file, althyp='two-sided'):
    data = load_data(file, derive_metrics=[
        (["mutants_generated", "mutants_surviving"], "mutants_killed", lambda g,s: g-s),
        (["mutants_generated", "mutants_killed"], "mutation_score", lambda g,k: k/g if g != 0 else 0)
    ] if file=="all_data.json" else [])
        
    algorithms = sorted(list(set(data['algorithm']))) # ["DYNAMOSA", "MIO", "WHOLE_SUITE", "RANDOM"]
    variable_data = [
        filter_scale(data, variable, [("algorithm", a)])[0]
        for a in algorithms
    ]
    
    stats = {}
    for i in range(0,len(algorithms)):
        for j in range(0,len(algorithms)):
            if i==j: continue
            if althyp=='two-sided' and i>j: continue
            comp = '!=' if althyp=='two-sided' else '<'
            
            stats[f"{algorithms[i]} {comp} {algorithms[j]}"] = sp.stats.mannwhitneyu(
                x=variable_data[i],
                y=variable_data[j],
                alternative=althyp
            )
            
    with open(os.path.abspath(f"stats/u_test-{variable}.json"), 'w') as f:
        json.dump(stats, f, indent=4)
        
if __name__=='__main__':
    if sys.argv[1] == "1": # box plots except fault detection
        for var,varName,algs,fileName in [
            ("coverage", "Branch Coverage", [], "branch_coverage-box_plots.png"),
            ("mutants_killed", "Mutants Killed", [], "mutants_killed-box_plots.png"),
            ("mutation_score", "Mutation Score", [], "mutation_score-box_plots.png"),
            ("test_count", "Number of Tests Generated", ["DYNAMOSA", "MIO", "WHOLE_SUITE"], "test_count-no_random-box_plots.png"),
            ("test_count", "Number of Tests Generated", ["RANDOM"], "test_count-only_random-box_plots.png")
        ]:
            plot_box(var, varName, algs, fileName, "all_data.json")
    elif sys.argv[1] == "2": # fault detection box plots
        for var,varName,algs,fileName in [
            ("faults_detected", "Fault Detection Ability", [], "fault_detection_ability-box_plots.png")
        ]:
            plot_box(var, varName, algs, fileName, "all_faults.json")
    elif sys.argv[1] == "3": # u test values
        for var in ["coverage", "mutants_killed", "mutation_score", "test_count"]:
            u_test(var, "all_data.json")