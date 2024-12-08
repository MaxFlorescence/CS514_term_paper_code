import csv, os, sys, json

def gather():
    if os.path.exists("all_data.json"): return
    
    data = {
        "algorithm": [],
        "project": [],
        "module": [],
        "coverage": [],
        "test_count": [],
        "mutants_generated": [],
        "mutants_surviving": []
    }
    
    for dir in sys.argv[1:]:
        for path, _, files in os.walk(os.path.abspath(dir)):
            for file in files:
                if "stats1.csv" in file:
                    print("Found", file)
                    algorithm = '_'.join(file.split("_")[:-1])
                    assert algorithm in ["DYNAMOSA", "MIO", "WHOLE_SUITE", "RANDOM"]
                    
                    project = os.path.basename(path).split('_')[0]
                    with open(os.path.join(path, file), 'r') as f:
                        reader = csv.reader(f)
                        next(reader, None) # skip headers
                        for row in reader:
                            data['algorithm'].append(algorithm)
                            data['project'].append(project)
                            data['module'].append(row[0])
                            data['coverage'].append(float(row[1]))
                            data['test_count'].append(int(row[2]))
                            data['mutants_generated'].append(int_or_zero(row[3]))
                            data['mutants_surviving'].append(int_or_zero(row[4]))
                        
    data['n'] = len(data['algorithm'])
    with open(os.path.abspath("./all_data.json"), 'w') as f:
        json.dump(data, f, indent=4)

def gather_faults():
    if os.path.exists("all_faults.json"): return
    
    full_data = {
        "DYNAMOSA": {},
        "MIO": {},
        "RANDOM": {},
        "WHOLE_SUITE": {}
    }
    
    for dir in sys.argv[1:]:
        for path, _, files in os.walk(os.path.abspath(dir)):
            for file in files:
                print("Found", file)
                if "faults_detected.csv"==file:
                    
                    with open(os.path.join(path, file), 'r') as f:
                        reader = csv.reader(f)
                        next(reader, None) # skip headers
                        for row in reader:
                            if row[1] not in full_data[row[0]]:
                                full_data[row[0]][row[1]] = [0,0]
                            else:
                                full_data[row[0]][row[1]][0] += (int(row[3]) if row[3]!="?" else 0)
                                full_data[row[0]][row[1]][1] += 1
    
    data = {
        "n": 0,
        "algorithm": [],
        "project": [],
        "faults_considered": [],
        "faults_detected": []
    }
    for alg,proj_data in full_data.items():
        for proj,bug_count in proj_data.items():
            data["n"] += 1
            data["algorithm"].append(alg)
            data["project"].append(proj)
            data["faults_considered"].append(bug_count[1])
            data["faults_detected"].append(bug_count[0]/bug_count[1])
                        
    with open(os.path.abspath("./all_faults.json"), 'w') as f:
        json.dump(data, f, indent=4)

def int_or_zero(x):
    if x == '': return 0
    return int(x)

if __name__=="__main__":
    gather_faults()