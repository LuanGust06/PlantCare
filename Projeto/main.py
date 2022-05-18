import sys
import matplotlib.pyplot as plt
from fuzzy import tempoTotal, duracao
import requests
import json
from reconhecimento import identify_plant

def main():
    requisicao = requests.get('http://127.0.0.1:8000/planta')

    plantinha =(identify_plant(["./img/alface.jpg"]))
    print(plantinha)
    if (plantinha == "lettuce" or plantinha == "Spinach"):
        necessidade = 5
    else:
        necessidade = 2

    dados = requisicao.json()
    for planta in dados['planta']:
        tempoTotal.input['temperatura'] = planta['temperatura']
        print(planta['temperatura'])
        tempoTotal.input['umidade'] = planta['umidade']
        print(planta['umidade'])
        tempoTotal.input['vazao'] = planta['vazao']
        print(planta['vazao'])

    tempoTotal.input['necessidade'] = necessidade
    print(necessidade)

    tempoTotal.compute()
    print(tempoTotal.output['duracao'])
    resultado = {'duracao': tempoTotal.output['duracao']}
    print(resultado)
    requests.put('http://127.0.0.1:8000/resultadonovo', data=json.dumps(resultado))

    duracao.view(sim=tempoTotal)
    plt.show()

if __name__ == '__main__':
    main()
