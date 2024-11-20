from pulp import *
from escritor import *
from pacientes import *
from profissionais import *

def problema():

    pacientes = listaDePacientes()
    profissionais = listaDeProfissionais()
    intersecoes = []

    # 1. Criação do modelo
    modelo = LpProblem("Agendamento", sense=LpMaximize)

    # 2. Variáveis de decisão
    x = LpVariable.dicts("x", ((paciente['nome'], profissional['nome']) for paciente in pacientes for profissional in profissionais), cat = LpBinary)

    # 3. Função objetivo: maximizar o número de atendimentos
    modelo += lpSum(x[paciente['nome'], profissional['nome']]
        for paciente in pacientes
            for profissional in profissionais), "TotalAtendimentos"

    # 4. Restrições

    # 4.1.  Cada paciente só pode ser atendido uma vez
    for paciente in pacientes:
        modelo += lpSum(x[paciente['nome'], profissional['nome']]
                        for profissional in profissionais) <= 1, f"UmaVez_{paciente['nome']}"


    # 4.2.  Cada profissional deve ter um tempo menor ou igual ao disponível
    for profissional in profissionais:
        modelo += lpSum(x[paciente['nome'], profissional['nome']]
                        for paciente in pacientes) <= profissional['qtdHorasDisponiveis'], f"qtdHorasDisponiveis{profissional['nome']}"

    locaisComuns = []
    disponibilidadesComuns = []

    # 4.3.  Profissional deve estar disponível e ter a especialidade certa
    for paciente in pacientes:
        for profissional in profissionais:
            if paciente['idade'] in profissional['especialidade']:
                # Checar se há pelo menos um local e uma disponibilidade em comum
                local_comum = paciente['locais'] & profissional['locais']
                disponibilidade_comum = paciente['disponibilidade'] & profissional['disponibilidade']
                if local_comum.any() and disponibilidade_comum.any():
                    modelo += x[paciente['nome'], profissional['nome']] <= 1  # Podem ser atendidos
                    locaisComuns.append(local_comum)
                else:
                    modelo += x[paciente['nome'], profissional['nome']] == 0  # Não podem ser atendidos
            else:
                modelo += x[paciente['nome'], profissional['nome']] == 0  # Não podem ser atendidos
            
    # 5.    Resolver o modelo
    modelo.solve()

    # 6.    Resultados
    print(f"Status: {LpStatus[modelo.status]}")

    print("\n\n")
    for v in modelo.variables():
        if v.value() > 0:
            print(f"{v.name} = {v.value()}")

    escrever(modelo)   

problema()