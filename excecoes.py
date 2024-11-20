import pandas as pd
from util import *
import escritor
import openpyxl

def escreverErro(tabela: str, tipo: str, mensagem: str):
    # Ler o arquivo existente
    caminho = obterCaminho()
    workbook = openpyxl.load_workbook(caminho)

    ocorrencia = escritor.dataEHora()

    # Criar uma nova linha de dados
    dados = [tabela, tipo, mensagem, ocorrencia]

    # Selecionar a planilha correta
    planilha = workbook['Inconsistência']

    # Limpar a planilha antes de escrever novos dados
    planilha.delete_rows(2, planilha.max_row)  # Remove todas as linhas a partir da linha 2

    # Escrever os novos dados na primeira linha (linha 2)
    for coluna_index, valor in enumerate(dados):  # Percorre cada valor na lista de dados
        letra_coluna = chr(ord('A') + coluna_index)  # Define a letra da coluna
        planilha[f'{letra_coluna}2'] = valor  # Escreve o valor na célula (linha 2)

    # Salvar o arquivo
    workbook.save(caminho)