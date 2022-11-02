import os
import subprocess

ligands = os.listdir('ligands')
targets = os.listdir("targets")
configs = os.listdir('configs')

print(ligands)
print(targets)

for target in targets:
    print(target)
    for ligand in ligands:
        print(f"Docking {ligand} with {target}")
        process = subprocess.Popen(f'vina --receptor targets/{target} --ligand ligands/{ligand} --config configs/{target.split(".")[0] + ".conf"} --out output/{target}_{ligand}.pdbqt', shell=True)
        # print(process.stdout)
        process.wait()

