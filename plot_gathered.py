import matplotlib.pyplot as plt
import json, os, sys
import scipy as sp

def make_lambda(vStr):
    maybe = lambda x: x
    if vStr[0] == '!':
        vStr = vStr[1:]
        maybe = lambda x: not(x)
        
    if ',' in vStr:
        vals = vStr.split(',')
        return lambda x: maybe(str(x) in vals)
    elif len(vStr)>1 and vStr[1] == '=':
        val = float(vStr[2:])
        if vStr[0] == '<':
            return lambda x: maybe(x <= val)
        elif vStr[0] == '>':
            return lambda x: maybe(x >= val)
    elif len(vStr)>0 and vStr[0] in '<>':
        val = float(vStr[1:])
        if vStr[0] == '<':
            return lambda x: maybe(x < val)
        elif vStr[0] == '>':
            return lambda x: maybe(x > val)
    else:
        return lambda x: maybe(str(x) == vStr)

def filter_scale(data, key, filters=[], scale=1.0) -> tuple[list, float, float]:
    ret = []
    corresponding_data = []
    minVal = None
    maxVal = None
    parsed_filters = [(k, make_lambda(v)) for k,v in filters]
    
    for i,v in enumerate(data[key]):
        if all([f(data[k][i]) for k,f in parsed_filters]):
            val = v*scale
            if minVal == None or minVal > val: minVal = val
            if maxVal == None or maxVal < val: maxVal = val
            ret.append(val)
            corresponding_data.append({k: v[i] for k,v in data.items() if isinstance(v, list) and k != key})
            
    if minVal == None or maxVal == None: minVal = maxVal = 0
    
    return ret, corresponding_data, minVal, maxVal

def load_data(path, derive_metrics=[]):
    with open(os.path.abspath(path), 'r') as f:
        data = json.load(f)
    
    for input_keys, output_key, function in derive_metrics:
        data[output_key] = [
            function(*[data[k][i] for k in input_keys])
            for i in range(data['n'])
        ]
        
    return data

def load_data_with_mutation_stats(path):
    return load_data(path, derive_metrics=[
        (["mutants_generated", "mutants_surviving"], "mutants_killed", lambda g,s: g-s),
        (["mutants_generated", "mutants_killed"], "mutation_score", lambda g,k: k/g if g != 0 else 0)
    ] if path=="all_data.json" else [])

alg_color = {
    "DYNAMOSA": "lightskyblue",
    "MIO": "plum",
    "RANDOM": "yellowgreen",
    "WHOLE_SUITE": "navajowhite"
}

def ind(alg, grouping):
    for i,g in enumerate(grouping):
        if alg in g: return i
    return -1

def plot_box(variable, varName, plot_to_alg, outName, file):
    data = load_data_with_mutation_stats(file)
    
    algorithms = sorted(list(set(data['algorithm']))) # ["DYNAMOSA", "MIO", "WHOLE_SUITE", "RANDOM"]
    if plot_to_alg == []:
        plot_to_alg = [algorithms]
        alg_to_plot = {a: 0 for a in algorithms}
    else:
        alg_to_plot = {a: ind(a, plot_to_alg) for a in algorithms}
    groups = len(plot_to_alg)
    x_pad = 0.5**len(plot_to_alg)
        
    variable_data = [[
        filter_scale(data, variable, [("algorithm", alg)])[0]
        for alg in group
    ] for group in plot_to_alg]
    
    fig, axs = plt.subplots(ncols=groups, width_ratios=[len(g) for g in plot_to_alg])
    try:
        axs = list(axs)
    except:
        axs = [axs]
    title = f'{varName} vs Algorithm'
    fig.supylabel(varName)
    fig.supxlabel("Algorithm")
    for i,ax in enumerate(axs):
        ax.set_xlim(left=1-x_pad, right=len(plot_to_alg[i])+x_pad)
    
    for i in range(groups):
        for j,a in enumerate(plot_to_alg[i]):
            redist_values = [v for v in filter_scale(data, variable, [("algorithm", a), ("project", "redistricting")])[0]]
            if len(redist_values) == 0: continue
            
            plot = alg_to_plot[a]
            redist_y = sp.ndimage.median(redist_values)
            redist_x = [j+1]
            axs[plot].scatter(redist_x, redist_y, marker="x", color="red", zorder=2)

        algs = plot_to_alg[i]
        bplot = axs[i].boxplot(x=variable_data[i], patch_artist=True, labels=algs, zorder=1)
        
        for patch, color in zip(bplot['boxes'], [alg_color[a] for a in algs]):
            patch.set_facecolor(color)
        for median in bplot['medians']:
            median.set_color('red')
    
    fig.suptitle(title)
    fig.set_layout_engine("tight")
    
    save_path = os.path.join('figures', outName)
    fig.savefig(os.path.abspath(save_path))
    
def u_test(variable, file, althyp='two-sided'):
    data = load_data_with_mutation_stats(file)
        
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
            ("test_count", "Number of Tests Generated", [["DYNAMOSA", "MIO", "WHOLE_SUITE"], ["RANDOM"]], "test_count-box_plots.png")
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
    else: # print data subset (sys.argv == [filePath variableName key1 value1 key2 value2 ...])
        data = load_data_with_mutation_stats(sys.argv[1])
        filtered_data = filter_scale(data, sys.argv[2], [
            (sys.argv[i], sys.argv[i+1]) for i in range(3, len(sys.argv), 2)
        ])
        for d,c in zip(*filtered_data[:2]):
            print('   ', d, c)
        print(len(filtered_data[0]), 'items found')