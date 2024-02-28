import gurobipy as gp
from gurobipy import GRB

# Criação do modelo de otimização com Gurobi
m = gp.Model("Maximizar_Rendimento")

# Variáveis de decisão para cada corte de carne, gordura e ossos da Ponta de Agulha (PA)
carne_pa = m.addVar(vtype=GRB.CONTINUOUS, name="Carne PA")
gordura_pa = m.addVar(vtype=GRB.CONTINUOUS, name="Gordura PA")
ossos_pa = m.addVar(vtype=GRB.CONTINUOUS, name="Ossos PA")

# Peso total da Ponta de Agulha (PA)
peso_pa = 35  # Em quilogramas

# Porcentagens de cada corte de carne, gordura e ossos em relação à Ponta de Agulha (PA)
porcentagem_carne_pa = 0.8
porcentagem_gordura_pa = 0.04
porcentagem_ossos_pa = 0.16

# Restrições para cada corte de carne, gordura e ossos da Ponta de Agulha (PA)
m.addConstr(carne_pa == peso_pa * porcentagem_carne_pa, "Restrição Carne PA")
m.addConstr(gordura_pa == peso_pa * porcentagem_gordura_pa, "Restrição Gordura PA")
m.addConstr(ossos_pa == peso_pa * porcentagem_ossos_pa, "Restrição Ossos PA")

# Objetivo do modelo (maximizar a quantidade total de carne)
m.setObjective(carne_pa, GRB.MAXIMIZE)

# Otimização do modelo
m.optimize()

# Impressão da solução
if m.status == GRB.OPTIMAL:
    print('Peso PA:',peso_pa)
    print('Carne PA:', carne_pa.x)
    print('Gordura PA:', gordura_pa.x)
    print('Ossos PA:', ossos_pa.x)
