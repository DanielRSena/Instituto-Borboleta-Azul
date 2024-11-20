import numpy as np
from util import *
from excecoes import *

def especialidades(profissional: int):
    dados = lerGuia('RegraProfissional')
    especialidades = dados.iloc[profissional + 1, 3:6]  # Pega as colunas de especialidade
    tabelaProf = []

    for i, especialidade in enumerate(especialidades):
        if isinstance(especialidade, str) and especialidade.lower() == 'x':
            if i == 0:
                tabelaProf.append('infantil')
            elif i == 1:
                tabelaProf.append('adolescente')
            elif i == 2:
                tabelaProf.append('adulto')
    return tabelaProf

def locaisProf(profissional: int):
    dados = lerGuia('LocalProfissional')
    tabelaProf = dados.iloc[profissional + 1, 1:].replace({'X': True, np.nan: False, 'x': True})
    return tabelaProf.values

def listaDeProfissionais():
    dados = leituraDados()
    profissionais = []
    for prof in range(len(dados['RegraProfissional']['profissional'])):
        profissional = {
            'nome': dados['RegraProfissional']['profissional'][prof],
            'tipo': dados['RegraProfissional']['tipo'][prof],
            'qtdHorasDisponiveis': dados['RegraProfissional']['horas_semana'][prof],
            'especialidade': especialidades(prof),
            'disponibilidade': obterDisponibilidade('DisponProfissional', prof),
            'locais': locaisProf(prof)
        }
        profissionais.append(profissional)
        if not any(profissional['disponibilidade'][prof]):
            escreverErro('Disponibilidade', 'ERRO', 'Sem local cadastrado para ' + profissional['nome'])
    return profissionais