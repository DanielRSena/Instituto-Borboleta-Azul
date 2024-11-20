from util import *

def faixaEspecialidade(idade):
    if idade < 12: return 'infantil'
    elif idade < 18: return 'adolescente'
    else: return 'adulto'

def localPaciente(paciente: int):
    dados = lerGuia('LocalPaciente')
    comeco = paciente * 6 + 1
    final = comeco + 6
    tabelaPaciente = dados.iloc[comeco:final, 2:].replace({'X': True, np.nan: False, 'x': True})
    return tabelaPaciente.values

def listaDePacientes():
    dados = leituraDados()
    pacientes = []
    for pac in range(len(dados['IdadePaciente']['paciente'])):
        paciente = {
            'nome': dados['IdadePaciente']['paciente'][pac],
            'idade': faixaEspecialidade(dados['IdadePaciente']['idade'][pac]),
            'qtdHorasDisponivel': 1,
            'disponibilidade': obterDisponibilidade('DisponPaciente', pac),
            'locais': localPaciente(pac)
        }
        pacientes.append(paciente)
    return pacientes