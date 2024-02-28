import gurobipy as gp
from gurobipy import GRB

# Criação do modelo de otimização com Gurobi
m = gp.Model("Maximizar_Rendimento")

# Variáveis de decisão para cada corte de carne, gordura e ossos do dianteiro
acém = m.addVar(vtype=GRB.CONTINUOUS, name="Acém")
pescoço = m.addVar(vtype=GRB.CONTINUOUS, name="Pescoço")
cupim = m.addVar(vtype=GRB.CONTINUOUS, name="Cupim")
peito = m.addVar(vtype=GRB.CONTINUOUS, name="Peito")
paleta = m.addVar(vtype=GRB.CONTINUOUS, name="Paleta")
músculo_dianteiro = m.addVar(vtype=GRB.CONTINUOUS, name="Músculo Dianteiro")
retalhos_dianteiro = m.addVar(vtype=GRB.CONTINUOUS, name="Retalhos Dianteiro")
gordura_dianteiro = m.addVar(vtype=GRB.CONTINUOUS, name="Gordura Dianteiro")
ossos_dianteiro = m.addVar(vtype=GRB.CONTINUOUS, name="Ossos Dianteiro")

# Peso total do dianteiro
peso_dianteiro = 95  # Em quilogramas

# Porcentagens de cada corte de carne, gordura e ossos em relação ao dianteiro
porcentagem_acém = 0.158
porcentagem_pescoço = 0.134
porcentagem_cupim = 0.025
porcentagem_peito = 0.114
porcentagem_paleta = 0.202
porcentagem_músculo_dianteiro = 0.061
porcentagem_retalhos_dianteiro = 0.034
porcentagem_gordura_dianteiro = 0.082
porcentagem_ossos_dianteiro = 0.189

# Restrições para cada corte de carne, gordura e ossos do dianteiro
m.addConstr(acém == peso_dianteiro * porcentagem_acém, "Restrição Acém")
m.addConstr(pescoço == peso_dianteiro * porcentagem_pescoço, "Restrição Pescoço")
m.addConstr(cupim == peso_dianteiro * porcentagem_cupim, "Restrição Cupim")
m.addConstr(peito == peso_dianteiro * porcentagem_peito, "Restrição Peito")
m.addConstr(paleta == peso_dianteiro * porcentagem_paleta, "Restrição Paleta")
m.addConstr(músculo_dianteiro == peso_dianteiro * porcentagem_músculo_dianteiro, "Restrição Músculo Dianteiro")
m.addConstr(retalhos_dianteiro == peso_dianteiro * porcentagem_retalhos_dianteiro, "Restrição Retalhos Dianteiro")
m.addConstr(gordura_dianteiro == peso_dianteiro * porcentagem_gordura_dianteiro, "Restrição Gordura Dianteiro")
m.addConstr(ossos_dianteiro == peso_dianteiro * porcentagem_ossos_dianteiro, "Restrição Ossos Dianteiro")

# Objetivo do modelo (maximizar a quantidade total de carne)
m.setObjective(acém + pescoço + cupim + peito + paleta + músculo_dianteiro + retalhos_dianteiro, GRB.MAXIMIZE)

# Otimização do modelo
m.optimize()

# Impressão da solução
if m.status == GRB.OPTIMAL:
    print('Dianteiro:',peso_dianteiro)
    print('Acém:', acém.x)
    print('Pescoço:', pescoço.x)
    print('Cupim:', cupim.x)
    print('Peito:', peito.x)
    print('Paleta:', paleta.x)
    print('Músculo Dianteiro:', músculo_dianteiro.x)
    print('Retalhos Dianteiro:', retalhos_dianteiro.x)
    print('Gordura Dianteiro:', gordura_dianteiro.x)
    print('Ossos Dianteiro:', ossos_dianteiro.x)
