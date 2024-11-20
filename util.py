import pandas as pd
import numpy as np

def obterCaminho():
    return 'cenario_1.xlsx'

def leituraDados():

    caminho = obterCaminho()

    # Dicionário para armazenar os DataFrames
    dados = {
        'IdadePaciente': pd.read_excel(caminho, sheet_name='IdadePaciente'),
        'DisponPaciente': pd.read_excel(caminho, sheet_name='DisponPaciente'),
        'LocalPaciente': pd.read_excel(caminho, sheet_name='LocalPaciente'),
        'RegraProfissional': pd.read_excel(caminho, sheet_name='RegraProfissional'),
        'LocalProfissional': pd.read_excel(caminho, sheet_name='LocalProfissional'),
        'Solucao': pd.read_excel(caminho, sheet_name='Solução'),
        'Inconsistencia': pd.read_excel(caminho, sheet_name='Inconsistência'),
    }

    return dados

def lerGuia(guia: str):

    caminho = obterCaminho()
    dadosDaGuia = pd.read_excel(caminho, sheet_name=guia, header=None)

    return dadosDaGuia

def obterDisponibilidade(tipoPessoa: str, num: int):

    dados = lerGuia(tipoPessoa)
    comeco = num * 6 + 1
    final = comeco + 6
    tabelaDispon = dados.iloc[comeco:final, 2:15].replace({'X': True, np.nan: False, 'x': True})

    return tabelaDispon.values