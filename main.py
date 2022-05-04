import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import sys
import matplotlib.pyplot as plt


def main():
    ##variaveis de entrada
    temperatura = ctrl.Antecedent(np.arange(-10, 51, 1), 'temperatura')
    umidade = ctrl.Antecedent(np.arange(0, 71, 1), 'umidade')
    vazao = ctrl.Antecedent(np.arange(2, 201, 1), 'vazao')

    ##resultado
    duracao = ctrl.Consequent(np.arange(0, 51, 1), 'duracao')

    ##membership functions - temperatura
    temperatura['muitoFrio'] = fuzz.trimf(temperatura.universe, [-10, -10, 3])
    temperatura['frio'] = fuzz.trimf(temperatura.universe, [0, 7.5, 15])
    temperatura['ameno'] = fuzz.trimf(temperatura.universe, [12, 19.5, 27])
    temperatura['quente'] = fuzz.trimf(temperatura.universe, [24, 31.5, 39])
    temperatura['muitoQuente'] = fuzz.trimf(temperatura.universe, [36, 50, 50])

    ##membership functions - temperatura
    umidade['seco'] = fuzz.trimf(umidade.universe, [0, 0, 15])
    umidade['poucoUmido'] = fuzz.trimf(umidade.universe, [10, 22.5, 35])
    umidade['umido'] = fuzz.trimf(umidade.universe, [30, 42.5, 60])
    umidade['muitoUmido'] = fuzz.trimf(umidade.universe, [55, 100, 100])

    ##membership functions - vazao
    vazao['gotejador'] = fuzz.trimf(vazao.universe, [2, 18, 18])
    vazao['microAspersor'] = fuzz.trimf(vazao.universe, [15, 70, 120])
    vazao['aspersor'] = fuzz.trimf(vazao.universe, [110, 150, 200])

    ##membership functions - Duração
    duracao['minima'] = fuzz.trimf(duracao.universe, [0, 1, 2])
    duracao['curta'] = fuzz.trimf(duracao.universe, [1, 3, 5])
    duracao['media'] = fuzz.trimf(duracao.universe, [4, 7, 10])
    duracao['longa'] = fuzz.trimf(duracao.universe, [8, 20, 30])
    duracao['bemLonga'] = fuzz.trimf(duracao.universe, [25, 40, 50])

    ##Fuzzy Rules
    ##Gotejador

    rule1 = ctrl.Rule(vazao['gotejador'] & umidade['seco'] & temperatura['muitoFrio'], duracao['bemLonga'])
    rule2 = ctrl.Rule(vazao['gotejador'] & umidade['seco'] & temperatura['frio'], duracao['bemLonga'])
    rule3 = ctrl.Rule(vazao['gotejador'] & umidade['seco'] & temperatura['ameno'], duracao['bemLonga'])
    rule4 = ctrl.Rule(vazao['gotejador'] & umidade['seco'] & temperatura['quente'], duracao['bemLonga'])
    rule5 = ctrl.Rule(vazao['gotejador'] & umidade['seco'] & temperatura['muitoQuente'], duracao['bemLonga'])

    rule6 = ctrl.Rule(vazao['gotejador'] & umidade['poucoUmido'] & temperatura['muitoFrio'], duracao['bemLonga'])
    rule7 = ctrl.Rule(vazao['gotejador'] & umidade['poucoUmido'] & temperatura['frio'], duracao['bemLonga'])
    rule8 = ctrl.Rule(vazao['gotejador'] & umidade['poucoUmido'] & temperatura['ameno'], duracao['bemLonga'])
    rule9 = ctrl.Rule(vazao['gotejador'] & umidade['poucoUmido'] & temperatura['quente'], duracao['bemLonga'])
    rule10 = ctrl.Rule(vazao['gotejador'] & umidade['poucoUmido'] & temperatura['muitoQuente'], duracao['bemLonga'])

    rule11 = ctrl.Rule(vazao['gotejador'] & umidade['umido'] & temperatura['muitoFrio'], duracao['longa'])
    rule12 = ctrl.Rule(vazao['gotejador'] & umidade['umido'] & temperatura['frio'], duracao['longa'])
    rule13 = ctrl.Rule(vazao['gotejador'] & umidade['umido'] & temperatura['ameno'], duracao['longa'])
    rule14 = ctrl.Rule(vazao['gotejador'] & umidade['umido'] & temperatura['quente'], duracao['longa'])
    rule15 = ctrl.Rule(vazao['gotejador'] & umidade['umido'] & temperatura['muitoQuente'], duracao['bemLonga'])

    rule16 = ctrl.Rule(vazao['gotejador'] & umidade['muitoUmido'] & temperatura['muitoFrio'], duracao['longa'])
    rule17 = ctrl.Rule(vazao['gotejador'] & umidade['muitoUmido'] & temperatura['frio'], duracao['longa'])
    rule18 = ctrl.Rule(vazao['gotejador'] & umidade['muitoUmido'] & temperatura['ameno'], duracao['longa'])
    rule19 = ctrl.Rule(vazao['gotejador'] & umidade['muitoUmido'] & temperatura['quente'], duracao['longa'])
    rule20 = ctrl.Rule(vazao['gotejador'] & umidade['muitoUmido'] & temperatura['muitoQuente'], duracao['longa'])

    ##microAspersor
    rule21 = ctrl.Rule(vazao['microAspersor'] & umidade['seco'] & temperatura['muitoFrio'], duracao['media'])
    rule22 = ctrl.Rule(vazao['microAspersor'] & umidade['seco'] & temperatura['frio'], duracao['media'])
    rule23 = ctrl.Rule(vazao['microAspersor'] & umidade['seco'] & temperatura['ameno'], duracao['media'])
    rule24 = ctrl.Rule(vazao['microAspersor'] & umidade['seco'] & temperatura['quente'], duracao['media'])
    rule25 = ctrl.Rule(vazao['microAspersor'] & umidade['seco'] & temperatura['muitoQuente'], duracao['media'])

    rule26 = ctrl.Rule(vazao['microAspersor'] & umidade['poucoUmido'] & temperatura['muitoFrio'], duracao['media'])
    rule27 = ctrl.Rule(vazao['microAspersor'] & umidade['poucoUmido'] & temperatura['frio'], duracao['media'])
    rule28 = ctrl.Rule(vazao['microAspersor'] & umidade['poucoUmido'] & temperatura['ameno'], duracao['media'])
    rule29 = ctrl.Rule(vazao['microAspersor'] & umidade['poucoUmido'] & temperatura['quente'], duracao['media'])
    rule30 = ctrl.Rule(vazao['microAspersor'] & umidade['poucoUmido'] & temperatura['muitoQuente'],
                       duracao['media'])

    rule31 = ctrl.Rule(vazao['microAspersor'] & umidade['umido'] & temperatura['muitoFrio'], duracao['curta'])
    rule32 = ctrl.Rule(vazao['microAspersor'] & umidade['umido'] & temperatura['frio'], duracao['curta'])
    rule33 = ctrl.Rule(vazao['microAspersor'] & umidade['umido'] & temperatura['ameno'], duracao['curta'])
    rule34 = ctrl.Rule(vazao['microAspersor'] & umidade['umido'] & temperatura['quente'], duracao['curta'])
    rule35 = ctrl.Rule(vazao['microAspersor'] & umidade['umido'] & temperatura['muitoQuente'], duracao['curta'])

    rule36 = ctrl.Rule(vazao['microAspersor'] & umidade['muitoUmido'] & temperatura['muitoFrio'], duracao['minima'])
    rule37 = ctrl.Rule(vazao['microAspersor'] & umidade['muitoUmido'] & temperatura['frio'], duracao['minima'])
    rule38 = ctrl.Rule(vazao['microAspersor'] & umidade['muitoUmido'] & temperatura['ameno'], duracao['minima'])
    rule39 = ctrl.Rule(vazao['microAspersor'] & umidade['muitoUmido'] & temperatura['quente'], duracao['minima'])
    rule40 = ctrl.Rule(vazao['microAspersor'] & umidade['muitoUmido'] & temperatura['muitoQuente'],
                       duracao['minima'])

    ##Aspersor

    rule41 = ctrl.Rule(vazao['aspersor'] & umidade['seco'] & temperatura['muitoFrio'], duracao['curta'])
    rule42 = ctrl.Rule(vazao['aspersor'] & umidade['seco'] & temperatura['frio'], duracao['curta'])
    rule43 = ctrl.Rule(vazao['aspersor'] & umidade['seco'] & temperatura['ameno'], duracao['curta'])
    rule44 = ctrl.Rule(vazao['aspersor'] & umidade['seco'] & temperatura['quente'], duracao['curta'])
    rule45 = ctrl.Rule(vazao['aspersor'] & umidade['seco'] & temperatura['muitoQuente'], duracao['curta'])

    rule46 = ctrl.Rule(vazao['aspersor'] & umidade['poucoUmido'] & temperatura['muitoFrio'], duracao['curta'])
    rule47 = ctrl.Rule(vazao['aspersor'] & umidade['poucoUmido'] & temperatura['frio'], duracao['curta'])
    rule48 = ctrl.Rule(vazao['aspersor'] & umidade['poucoUmido'] & temperatura['ameno'], duracao['curta'])
    rule49 = ctrl.Rule(vazao['aspersor'] & umidade['poucoUmido'] & temperatura['quente'], duracao['curta'])
    rule50 = ctrl.Rule(vazao['aspersor'] & umidade['poucoUmido'] & temperatura['muitoQuente'], duracao['curta'])

    rule51 = ctrl.Rule(vazao['aspersor'] & umidade['umido'] & temperatura['muitoFrio'], duracao['minima'])
    rule52 = ctrl.Rule(vazao['aspersor'] & umidade['umido'] & temperatura['frio'], duracao['minima'])
    rule53 = ctrl.Rule(vazao['aspersor'] & umidade['umido'] & temperatura['ameno'], duracao['minima'])
    rule54 = ctrl.Rule(vazao['aspersor'] & umidade['umido'] & temperatura['quente'], duracao['minima'])
    rule55 = ctrl.Rule(vazao['aspersor'] & umidade['umido'] & temperatura['muitoQuente'], duracao['minima'])

    rule56 = ctrl.Rule(vazao['aspersor'] & umidade['muitoUmido'] & temperatura['muitoFrio'], duracao['minima'])
    rule57 = ctrl.Rule(vazao['aspersor'] & umidade['muitoUmido'] & temperatura['frio'], duracao['minima'])
    rule58 = ctrl.Rule(vazao['aspersor'] & umidade['muitoUmido'] & temperatura['ameno'], duracao['minima'])
    rule59 = ctrl.Rule(vazao['aspersor'] & umidade['muitoUmido'] & temperatura['quente'], duracao['minima'])
    rule60 = ctrl.Rule(vazao['aspersor'] & umidade['muitoUmido'] & temperatura['muitoQuente'], duracao['minima'])

    ##Regras
    tempoTotal_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
                                          rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
                                          rule20,
                                          rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29,
                                          rule30,
                                          rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39,
                                          rule40,
                                          rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49,
                                          rule50,
                                          rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59,
                                          rule60])
    tempoTotal = ctrl.ControlSystemSimulation(tempoTotal_ctrl)

    print('Please input temperature value (celcius) : ', flush=True)
    tempoTotal.input['temperatura'] = int(sys.stdin.readline())

    print('Please input percentage humidity (%) : ', flush=True)
    tempoTotal.input['umidade'] = int(sys.stdin.readline())

    print('Informa a vazão do sistem (em L/H) ', flush=True)
    tempoTotal.input['vazao'] = int(sys.stdin.readline())

    #tempoTotal.input['temp'] = 30
    #tempoTotal.input['umi'] = 15
    #tempoTotal.input['v'] = 25

    tempoTotal.compute()
    print(tempoTotal.output['duracao'])

    duracao.view(sim=tempoTotal)
    plt.show()

if __name__ == '__main__':
    main()
