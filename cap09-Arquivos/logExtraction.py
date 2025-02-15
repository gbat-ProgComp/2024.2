import matplotlib.pyplot as plt


def leArquivo (nomeArquivo):
    dadosLog = tuple()
    
    fd = open(nomeArquivo, "r")
    for linha in fd:
        ip = linha[0:linha.find(' ')]
        posPrimColchete = linha.find('[')
        dataHora = linha[posPrimColchete+1: 
                         linha.find(' ', posPrimColchete)]
        posSegundaAspas = linha.find('" ')
        codigo = linha[posSegundaAspas+2:posSegundaAspas+5]

        dadosLog += ((ip, dataHora, codigo), )
    fd.close()
    return dadosLog 

def questao1(logs):
    grupoHoraMin = {}
    for log in logs:
        horaMin = log[1][12:17]
        grupoHoraMin[horaMin] = grupoHoraMin.get(horaMin, 0)+1
    print (grupoHoraMin)

def questao2(logs):
    grupoDiaHora = {}
    for log in logs:
        horaMin = log[1][0:17]
        grupoDiaHora[horaMin] = grupoDiaHora.get(horaMin, 0)+1
    maxDiaHora = sorted(grupoDiaHora.items(), key=lambda x: -x[1])[0]
    print (maxDiaHora)

def questao3(logs):
    grupoCodigos = {}
    for log in logs:
        codigo = log[2]
        grupoCodigos[codigo] = grupoCodigos.get(codigo, 0)+1

    fig, ax = plt.subplots()
    codigos = grupoCodigos.keys()
    contadores = grupoCodigos.values()
    ax.bar(codigos, contadores)
    plt.show()
    
dadosLog = leArquivo('cap09-Arquivos/apache_logs.txt')

questao1(dadosLog)
questao2(dadosLog)
questao3(dadosLog)