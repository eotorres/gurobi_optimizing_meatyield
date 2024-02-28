import gurobipy as gp
from gurobipy import GRB

# Criação do modelo de otimização com Gurobi
m = gp.Model("Maximizar_Rendimento")

# Variáveis de decisão para cada corte de carne, gordura e ossos
filé = m.addVar(vtype=GRB.CONTINUOUS, name="Filé")
contrafilé = m.addVar(vtype=GRB.CONTINUOUS, name="Contrafilé")
alcatra = m.addVar(vtype=GRB.CONTINUOUS, name="Alcatra")
coxão_mole = m.addVar(vtype=GRB.CONTINUOUS, name="Coxão Mole")
coxão_duro = m.addVar(vtype=GRB.CONTINUOUS, name="Coxão Duro")
patinho = m.addVar(vtype=GRB.CONTINUOUS, name="Patinho")
lagarto = m.addVar(vtype=GRB.CONTINUOUS, name="Lagarto")
capa_e_aba = m.addVar(vtype=GRB.CONTINUOUS, name="Capa e Aba")
músculo = m.addVar(vtype=GRB.CONTINUOUS, name="Músculo")
retalhos = m.addVar(vtype=GRB.CONTINUOUS, name="Retalhos")
gordura = m.addVar(vtype=GRB.CONTINUOUS, name="Gordura")
ossos = m.addVar(vtype=GRB.CONTINUOUS, name="Ossos")

# Peso total do traseiro
peso_traseiro_especial = 120  # Em quilogramas

# Porcentagens de cada corte de carne, gordura e ossos em relação ao traseiro
porcentagem_filé = 0.044
porcentagem_contrafilé = 0.144
porcentagem_alcatra = 0.115
porcentagem_coxão_mole = 0.164
porcentagem_coxão_duro = 0.11
porcentagem_patinho = 0.1
porcentagem_lagarto = 0.046
porcentagem_capa_e_aba = 0.036
porcentagem_músculo = 0.076
porcentagem_retalhos = 0.06
porcentagem_gordura = 0.094
porcentagem_ossos = 0.21

# Restrições para cada corte de carne, gordura e ossos
m.addConstr(filé == peso_traseiro_especial * porcentagem_filé, "Restrição Filé")
m.addConstr(contrafilé == peso_traseiro_especial * porcentagem_contrafilé, "Restrição Contrafilé")
m.addConstr(alcatra == peso_traseiro_especial * porcentagem_alcatra, "Restrição Alcatra")
m.addConstr(coxão_mole == peso_traseiro_especial * porcentagem_coxão_mole, "Restrição Coxão Mole")
m.addConstr(coxão_duro == peso_traseiro_especial * porcentagem_coxão_duro, "Restrição Coxão Duro")
m.addConstr(patinho == peso_traseiro_especial * porcentagem_patinho, "Restrição Patinho")
m.addConstr(lagarto == peso_traseiro_especial * porcentagem_lagarto, "Restrição Lagarto")
m.addConstr(capa_e_aba == peso_traseiro_especial * porcentagem_capa_e_aba, "Restrição Capa e Aba")
m.addConstr(músculo == peso_traseiro_especial * porcentagem_músculo, "Restrição Músculo")
m.addConstr(retalhos == peso_traseiro_especial * porcentagem_retalhos, "Restrição Retalhos")
m.addConstr(gordura == peso_traseiro_especial * porcentagem_gordura, "Restrição Gordura")
m.addConstr(ossos == peso_traseiro_especial * porcentagem_ossos, "Restrição Ossos")

# Objetivo do modelo (maximizar a quantidade total de carne)
m.setObjective(filé + contrafilé + alcatra + coxão_mole + coxão_duro + patinho + lagarto + capa_e_aba + músculo + retalhos, GRB.MAXIMIZE)

# Otimização do modelo
m.optimize()

# Impressão da solução
if m.status == GRB.OPTIMAL:
    print('Traseiro:',peso_traseiro_especial)
    print('Filé:', filé.x)
    print('Contrafilé:', contrafilé.x)
    print('Alcatra:', alcatra.x)
    print('Coxão Mole:', coxão_mole.x)
    print('Coxão Duro:', coxão_duro.x)
    print('Patinho:', patinho.x)
    print('Lagarto:', lagarto.x)
    print('Capa e Aba:', capa_e_aba.x)
    print('Músculo:', músculo.x)
    print('Retalhos:', retalhos.x)
    print('Gordura:', gordura.x)
    print('Ossos:', ossos.x)
