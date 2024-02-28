import streamlit as st
import gurobipy as gp
from gurobipy import GRB

def optimize_meat_yield():
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

    # Resultados
    rendimento_total_carne = m.objVal
    rendimento_traseiro = carne_traseiro.x
    rendimento_dianteiro = carne_dianteiro.x
    rendimento_ponta_agulha = carne_ponta_agulha.x

    return rendimento_total_carne, rendimento_traseiro, rendimento_dianteiro, rendimento_ponta_agulha

def optimize_pa_cut():
    # Criação do modelo de otimização com Gurobi
    m = gp.Model("Maximizar_Rendimento_PA")

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

    # Objetivo do modelo (maximizar a quantidade de carne)
    m.setObjective(carne_pa, GRB.MAXIMIZE)

    # Otimização do modelo
    m.optimize()

    # Resultados
    rendimento_carne_pa = carne_pa.x
    rendimento_gordura_pa = gordura_pa.x
    rendimento_ossos_pa = ossos_pa.x

    return rendimento_carne_pa, rendimento_gordura_pa, rendimento_ossos_pa,peso_pa

def optimize_cuts():
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

    # Resultados
    resultados = {
        'Traseiro': peso_traseiro_especial,
        'Filé': filé.x,
        'Contrafilé': contrafilé.x,
        'Alcatra': alcatra.x,
        'Coxão Mole': coxão_mole.x,
        'Coxão Duro': coxão_duro.x,
        'Patinho': patinho.x,
        'Lagarto': lagarto.x,
        'Capa e Aba': capa_e_aba.x,
        'Músculo': músculo.x,
        'Retalhos': retalhos.x,
        'Gordura': gordura.x,
        'Ossos': ossos.x
    }

    return resultados

def optimize_front_cuts():
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

    # Resultados
    resultados = {
        'Dianteiro': peso_dianteiro,
        'Acém': acém.x,
        'Pescoço': pescoço.x,
        'Cupim': cupim.x,
        'Peito': peito.x,
        'Paleta': paleta.x,
        'Músculo Dianteiro': músculo_dianteiro.x,
        'Retalhos Dianteiro': retalhos_dianteiro.x,
        'Gordura Dianteiro': gordura_dianteiro.x,
        'Ossos Dianteiro': ossos_dianteiro.x
    }

    return resultados

def optimize_boi_desdobramento():
    # Criação do modelo de otimização com Gurobi
    m = gp.Model("Desdobramento de Peso de um Boi")

    # Variáveis de decisão para cada componente
    peso_boi_gordo = 468  # Em quilogramas
    peso_boi_entrada_frigorifico = 440 #94%
    porcentagem_carcaça_quente = 0.545
    porcentagem_carne_industrial = 0.016
    porcentagem_miúdos_glandulas = 0.028
    porcentagem_sangue = 0.026
    porcentagem_ossos = 0.102
    porcentagem_gorduras = 0.048
    porcentagem_couros_mocotós = 0.139
    porcentagem_conteudo_bucho_estrias = 0.079
    porcentagem_quebras_currais_matanca = 0.032

    # Variáveis de decisão para cada componente
    carcaça_quente = m.addVar(vtype=GRB.CONTINUOUS, name="Carcaça Quente")
    carne_industrial = m.addVar(vtype=GRB.CONTINUOUS, name="Carne Industrial")
    miúdos_glandulas = m.addVar(vtype=GRB.CONTINUOUS, name="Miúdos e Glândulas")
    sangue = m.addVar(vtype=GRB.CONTINUOUS, name="Sangue")
    ossos = m.addVar(vtype=GRB.CONTINUOUS, name="Ossos")
    gorduras = m.addVar(vtype=GRB.CONTINUOUS, name="Gorduras")
    couros_mocotós = m.addVar(vtype=GRB.CONTINUOUS, name="Couro, Mocotós, etc.")
    conteudo_bucho_estrias = m.addVar(vtype=GRB.CONTINUOUS, name="Conteúdo do Bucho e Estrias")
    quebras_currais_matanca = m.addVar(vtype=GRB.CONTINUOUS, name="Quebras nos Currais e na Matança")

    # Restrições para cada componente
    m.addConstr(carcaça_quente == peso_boi_entrada_frigorifico * porcentagem_carcaça_quente, "Restrição Carcaça Quente")
    m.addConstr(carne_industrial == peso_boi_entrada_frigorifico * porcentagem_carne_industrial, "Restrição Carne Industrial")
    m.addConstr(miúdos_glandulas == peso_boi_entrada_frigorifico * porcentagem_miúdos_glandulas, "Restrição Miúdos e Glândulas")
    m.addConstr(sangue == peso_boi_entrada_frigorifico * porcentagem_sangue, "Restrição Sangue")
    m.addConstr(ossos == peso_boi_entrada_frigorifico * porcentagem_ossos, "Restrição Ossos")
    m.addConstr(gorduras == peso_boi_entrada_frigorifico * porcentagem_gorduras, "Restrição Gorduras")
    m.addConstr(couros_mocotós == peso_boi_entrada_frigorifico * porcentagem_couros_mocotós, "Restrição Couro, Mocotós, etc.")
    m.addConstr(conteudo_bucho_estrias == peso_boi_entrada_frigorifico * porcentagem_conteudo_bucho_estrias, "Restrição Conteúdo do Bucho e Estrias")
    m.addConstr(quebras_currais_matanca == peso_boi_entrada_frigorifico * porcentagem_quebras_currais_matanca, "Restrição Quebras nos Currais e na Matança")

    # Objetivo do modelo (maximizar o peso total)
    m.setObjective(carcaça_quente + carne_industrial + miúdos_glandulas + sangue + ossos + gorduras + couros_mocotós + conteudo_bucho_estrias + quebras_currais_matanca, GRB.MAXIMIZE)

    # Otimização do modelo
    m.optimize()

    # Resultados
    resultados = {
        'Peso Boi Gordo': peso_boi_gordo,
        'Peso Boi Frigorifico': peso_boi_entrada_frigorifico,
        'Carcaça Quente': carcaça_quente.x,
        'Carne Industrial': carne_industrial.x,
        'Miúdos e Glândulas': miúdos_glandulas.x,
        'Sangue': sangue.x,
        'Ossos': ossos.x,
        'Gorduras': gorduras.x,
        'Couro, Mocotós, etc.': couros_mocotós.x,
        'Conteúdo do Bucho e Estrias': conteudo_bucho_estrias.x,
        'Quebras nos Currais e na Matança': quebras_currais_matanca.x
    }

    return resultados

def main():
    st.title("Optimizing Meat Yield")    
    st.write("This app maximizes meat yield based on specified carcass weights and meat yields.")    
    if st.button("Optimize Boi Gordo"):
        resultados = optimize_boi_desdobramento()
        
        for componente, quantidade in resultados.items():
            st.write(f"{componente}: {quantidade:.2f}")

    if st.button("Optimize Carcass Yield"):
        rendimento_total_carne, rendimento_traseiro, rendimento_dianteiro, rendimento_ponta_agulha = optimize_meat_yield()

        st.write(f"Rendimento total em carne resfriada: {rendimento_total_carne:.2f}")
        st.write(f"Rendimento em carne Traseiro: {rendimento_traseiro:.2f}")
        st.write(f"Rendimento em carne Dianteiro: {rendimento_dianteiro:.2f}")
        st.write(f"Rendimento em carne Ponta de Agulha: {rendimento_ponta_agulha:.2f}")

    if st.button("Optimize PA Cut"):
        rendimento_carne_pa, rendimento_gordura_pa, rendimento_ossos_pa,peso_pa = optimize_pa_cut()
        
        st.write(f"Peso da Ponta de Agulha: {peso_pa:.2f}")
        st.write(f"Rendimento em carne da Ponta de Agulha: {rendimento_carne_pa:.2f}")
        st.write(f"Rendimento em gordura da Ponta de Agulha: {rendimento_gordura_pa:.2f}")
        st.write(f"Rendimento em ossos da Ponta de Agulha: {rendimento_ossos_pa:.2f}")

    if st.button("Optimize Traseiro Cut"):
        resultados = optimize_cuts()

        for corte, quantidade in resultados.items():
            st.write(f"{corte}: {quantidade:.2f}")
            
    if st.button("Optimize Dianteiro Cut"):
        resultados = optimize_front_cuts()

        for corte, quantidade in resultados.items():
            st.write(f"{corte}: {quantidade:.2f}")
            
if __name__ == "__main__":
    main()
