import gurobipy as gp
from gurobipy import GRB

# Criação do modelo de otimização com Gurobi
m = gp.Model("Maximizar_Rendimento")

# Variáveis de decisão
carne_traseiro = m.addVar(vtype=GRB.CONTINUOUS, name="Carne Traseiro")
carne_dianteiro = m.addVar(vtype=GRB.CONTINUOUS, name="Carne Dianteiro")
carne_ponta_agulha = m.addVar(vtype=GRB.CONTINUOUS, name="Carne Ponta de Agulha")

# Peso total da carcaça
peso_total_carcaça = 250

# Rendimentos de carne especificados
rendimento_carne_traseiro = 0.48
rendimento_carne_dianteiro = 0.38
rendimento_carne_ponta_agulha = 0.14

# Restrições
m.addConstr(carne_traseiro + carne_dianteiro + carne_ponta_agulha == peso_total_carcaça, "Restrição de peso total")

m.addConstr(carne_traseiro == peso_total_carcaça * rendimento_carne_traseiro, "Restrição de peso Traseiro")
m.addConstr(carne_dianteiro == peso_total_carcaça * rendimento_carne_dianteiro, "Restrição de peso Dianteiro")
m.addConstr(carne_ponta_agulha == peso_total_carcaça * rendimento_carne_ponta_agulha, "Restrição de peso Ponta de Agulha")

# Rendimento da carcaça
rendimento_carcaça = m.addVar(vtype=GRB.CONTINUOUS, name="Rendimento da Carcaça")
m.addConstr(rendimento_carcaça == (carne_traseiro + carne_dianteiro + carne_ponta_agulha) / peso_total_carcaça, "Rendimento da Carcaça")

# Objetivo
# Maximizar o rendimento total em carne
m.setObjective(carne_traseiro + carne_dianteiro + carne_ponta_agulha, GRB.MAXIMIZE)

# Otimização do modelo
m.optimize()

# Impressão da solução
if m.status == GRB.OPTIMAL:
    print('Rendimento da carcaça:', rendimento_carcaça.x * peso_total_carcaça)
    print('Rendimento total em carne:', m.objVal)
    print('Rendimento em carne Traseiro:', carne_traseiro.x)
    print('Rendimento em carne Dianteiro:', carne_dianteiro.x)
    print('Rendimento em carne Ponta de Agulha:', carne_ponta_agulha.x)
