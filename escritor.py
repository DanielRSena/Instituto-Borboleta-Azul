import openpyxl
import pandas as pd
from util import obterCaminho, leituraDados
from datetime import datetime, timezone, timedelta
from pacientes import listaDePacientes
from profissionais import listaDeProfissionais

def dataEHora():
    utc_now = datetime.now(timezone.utc)
    brt_now = utc_now - timedelta(hours = 3)  # Define o fuso horário de Brasília (UTC-3, sem horário de verão)
    return brt_now.strftime('%d/%m/%Y, %H:%M:%S')

def escrever(modelo):

    pacientes = listaDePacientes()  # Função presumida que retorna uma lista
    profissionais = listaDeProfissionais()  # Função presumida que retorna uma lista

    dadosParaEscrever = []
    dados = pd.read_excel(obterCaminho(), sheet_name='LocalProfissional')

    # Variáveis para armazenar os dados
    paciente = ''
    profissional = ''
    diaSemana = ''
    hora = ''
    local = ''

    # Percorrer as variáveis do modelo
    for v in modelo.variables():
        if v.value() > 0:
            paciente  = str(v.name.split('_')[1])[2:-2]
            profissional = str(v.name.split('_')[2])[1:-2]
            dadosParaEscrever.append([paciente, profissional, diaSemana, hora, local,  dataEHora()])
            print(f'\n\t{paciente} atendido pelo {profissional} na {local}, Dia: {diaSemana}, Hora: {hora}')

    # Ler o arquivo existente
    caminho = obterCaminho()
    workbook = openpyxl.load_workbook(caminho)

    # Selecionar a planilha correta
    planilha = workbook['Solução']

    # Escrever os dados na planilha
    for linha_index, linha_dados in enumerate(dadosParaEscrever, start=2):  # Começa na linha 2
        for coluna_index, valor in enumerate(linha_dados):  # Percorre cada valor na linha
            letra_coluna = chr(ord('A') + coluna_index)  # Define a letra da coluna
            planilha[f'{letra_coluna}{linha_index}'] = valor  # Escreve o valor na célula

    # Salvar o arquivo
    workbook.save(caminho)

    input('Pressione ENTER para sair...')