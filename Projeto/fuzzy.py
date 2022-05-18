import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#variaveis de entrada
temperatura = ctrl.Antecedent(np.arange(-10, 51, 1), 'temperatura')
necessidade_hidrica = ctrl.Antecedent(np.arange(0, 7, 1), 'necessidade')
umidade = ctrl.Antecedent(np.arange(0, 81, 1), 'umidade')
vazao = ctrl.Antecedent(np.arange(2, 201, 1), 'vazao')

##resultado
duracao = ctrl.Consequent(np.arange(0, 51, 1), 'duracao')

##membership functions - temperatura
temperatura['muitoFrio'] = fuzz.trimf(temperatura.universe, [-10, -10, 4])
temperatura['frio'] = fuzz.trimf(temperatura.universe, [0, 7.5, 15])
temperatura['ameno'] = fuzz.trimf(temperatura.universe, [12, 19.5, 27])
temperatura['quente'] = fuzz.trimf(temperatura.universe, [24, 31.5, 39])
temperatura['muitoQuente'] = fuzz.trimf(temperatura.universe, [36, 50, 50])

##membership functions - Necessidade Hidrica
necessidade_hidrica['baixa'] = fuzz.trimf(necessidade_hidrica.universe, [0, 2, 4])
necessidade_hidrica['alta'] = fuzz.trimf(necessidade_hidrica.universe, [3, 5, 6])

##membership functions - umidade
umidade['seco'] = fuzz.trimf(umidade.universe, [0, 0, 15])
umidade['poucoUmido'] = fuzz.trimf(umidade.universe, [10, 22.5, 35])
umidade['umido'] = fuzz.trimf(umidade.universe, [30, 42.5, 60])
umidade['muitoUmido'] = fuzz.trimf(umidade.universe, [55, 80, 80])

##membership functions - vazao
vazao['gotejador'] = fuzz.trimf(vazao.universe, [1, 1, 18])
vazao['microAspersor'] = fuzz.trimf(vazao.universe, [15, 70, 120])
vazao['aspersor'] = fuzz.trimf(vazao.universe, [110, 200, 200])

##membership functions - Duração
duracao['minima'] = fuzz.trimf(duracao.universe, [0, 0, 2])
duracao['curta'] = fuzz.trimf(duracao.universe, [1, 3, 5])
duracao['media'] = fuzz.trimf(duracao.universe, [4, 7, 10])
duracao['longa'] = fuzz.trimf(duracao.universe, [8, 20, 30])
duracao['bemLonga'] = fuzz.trimf(duracao.universe, [25, 35, 45])
duracao['maxima'] = fuzz.trimf(duracao.universe, [40, 50, 50])

##Fuzzy Rules
#Planta de Baixa Necessidade Hidrica
##Gotejador

rule1 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['muitoFrio'], duracao['bemLonga'])
rule2 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['frio'], duracao['bemLonga'])
rule3 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['ameno'], duracao['bemLonga'])
rule4 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['quente'], duracao['bemLonga'])
rule5 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['muitoQuente'], duracao['bemLonga'])

rule6 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['muitoFrio'], duracao['longa'])
rule7 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['frio'], duracao['longa'])
rule8 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['ameno'], duracao['longa'])
rule9 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['quente'], duracao['longa'])
rule10 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['muitoQuente'], duracao['longa'])

rule11 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['muitoFrio'], duracao['longa'])
rule12 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['frio'], duracao['longa'])
rule13 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['ameno'], duracao['longa'])
rule14 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['quente'], duracao['longa'])
rule15 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['muitoQuente'], duracao['bemLonga'])

rule16 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['muitoFrio'], duracao['longa'])
rule17 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['frio'], duracao['longa'])
rule18 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['ameno'], duracao['longa'])
rule19 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['quente'], duracao['longa'])
rule20 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['muitoQuente'], duracao['longa'])

##microAspersor
rule21 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['muitoFrio'], duracao['media'])
rule22 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['frio'], duracao['media'])
rule23 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['ameno'], duracao['media'])
rule24 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['quente'], duracao['media'])
rule25 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['muitoQuente'], duracao['media'])

rule26 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['muitoFrio'], duracao['curta'])
rule27 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['frio'], duracao['curta'])
rule28 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['ameno'], duracao['curta'])
rule29 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['quente'], duracao['curta'])
rule30 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['muitoQuente'], duracao['curta'])

rule31 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['muitoFrio'], duracao['minima'])
rule32 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['frio'], duracao['minima'])
rule33 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['ameno'], duracao['minima'])
rule34 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['quente'], duracao['minima'])
rule35 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['muitoQuente'], duracao['minima'])

rule36 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['muitoFrio'], duracao['minima'])
rule37 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['frio'], duracao['minima'])
rule38 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['ameno'], duracao['minima'])
rule39 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['quente'], duracao['minima'])
rule40 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['muitoQuente'], duracao['minima'])

##Aspersor

rule41 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['muitoFrio'], duracao['curta'])
rule42 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['frio'], duracao['curta'])
rule43 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['ameno'], duracao['curta'])
rule44 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['quente'], duracao['curta'])
rule45 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['seco'] & temperatura['muitoQuente'], duracao['curta'])

rule46 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['muitoFrio'], duracao['minima'])
rule47 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['frio'], duracao['minima'])
rule48 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['ameno'], duracao['minima'])
rule49 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['quente'], duracao['minima'])
rule50 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['poucoUmido'] & temperatura['muitoQuente'], duracao['minima'])

rule51 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['muitoFrio'], duracao['minima'])
rule52 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['frio'], duracao['minima'])
rule53 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['ameno'], duracao['minima'])
rule54 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['quente'], duracao['minima'])
rule55 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['umido'] & temperatura['muitoQuente'], duracao['minima'])

rule56 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['muitoFrio'], duracao['minima'])
rule57 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['frio'], duracao['minima'])
rule58 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['ameno'], duracao['minima'])
rule59 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['quente'], duracao['minima'])
rule60 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['baixa'] & umidade['muitoUmido'] & temperatura['muitoQuente'], duracao['minima'])

###################################################################################################################
###################################################################################################################
###################################################################################################################
###################################################################################################################
###################################################################################################################

##Alta necessidade hidrica
##Gotejador

rule61 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['muitoFrio'], duracao['maxima'])
rule62 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['frio'], duracao['maxima'])
rule63 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['ameno'], duracao['maxima'])
rule64 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['quente'], duracao['maxima'])
rule65 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['muitoQuente'], duracao['maxima'])

rule66 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['muitoFrio'], duracao['maxima'])
rule67 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['frio'], duracao['maxima'])
rule68 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['ameno'], duracao['maxima'])
rule69 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['quente'], duracao['maxima'])
rule70 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['muitoQuente'], duracao['maxima'])

rule71 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['muitoFrio'], duracao['bemLonga'])
rule72 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['frio'], duracao['bemLonga'])
rule73 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['ameno'], duracao['bemLonga'])
rule74 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['quente'], duracao['bemLonga'])
rule75 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['muitoQuente'], duracao['bemLonga'])

rule76 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['muitoFrio'], duracao['longa'])
rule77 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['frio'], duracao['longa'])
rule78 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['ameno'], duracao['longa'])
rule79 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['quente'], duracao['longa'])
rule80 = ctrl.Rule(vazao['gotejador'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['muitoQuente'], duracao['longa'])

##microAspersor
rule81 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['muitoFrio'], duracao['media'])
rule82 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['frio'], duracao['media'])
rule83 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['ameno'], duracao['media'])
rule84 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['quente'], duracao['media'])
rule85 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['muitoQuente'], duracao['media'])

rule86 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['muitoFrio'], duracao['media'])
rule87 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['frio'], duracao['media'])
rule88 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['ameno'], duracao['media'])
rule89 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['quente'], duracao['media'])
rule90 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['muitoQuente'], duracao['media'])

rule91 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['muitoFrio'], duracao['curta'])
rule92 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['frio'], duracao['curta'])
rule93 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['ameno'], duracao['curta'])
rule94 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['quente'], duracao['curta'])
rule95 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['muitoQuente'], duracao['curta'])

rule96 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['muitoFrio'], duracao['minima'])
rule97 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['frio'], duracao['minima'])
rule98 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['ameno'], duracao['minima'])
rule99 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['quente'], duracao['minima'])
rule100 = ctrl.Rule(vazao['microAspersor'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['muitoQuente'], duracao['minima'])


##Aspersor

rule101 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['muitoFrio'], duracao['curta'])
rule102 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['frio'], duracao['curta'])
rule103 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['ameno'], duracao['curta'])
rule104 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['quente'], duracao['curta'])
rule105 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['seco'] & temperatura['muitoQuente'], duracao['curta'])

rule106 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['muitoFrio'], duracao['curta'])
rule107 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['frio'], duracao['curta'])
rule108 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['ameno'], duracao['curta'])
rule109 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['quente'], duracao['curta'])
rule110 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['poucoUmido'] & temperatura['muitoQuente'], duracao['curta'])

rule111 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['muitoFrio'], duracao['curta'])
rule112 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['frio'], duracao['curta'])
rule113 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['ameno'], duracao['curta'])
rule114 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['quente'], duracao['curta'])
rule115 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['umido'] & temperatura['muitoQuente'], duracao['curta'])

rule116 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['muitoFrio'], duracao['minima'])
rule117 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['frio'], duracao['minima'])
rule118 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['ameno'], duracao['minima'])
rule119 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['quente'], duracao['minima'])
rule120 = ctrl.Rule(vazao['aspersor'] & necessidade_hidrica['alta'] & umidade['muitoUmido'] & temperatura['muitoQuente'], duracao['minima'])


###################################################################################################################
###################################################################################################################
###################################################################################################################
###################################################################################################################
###################################################################################################################


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
                                      rule60,
                                      rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69,
                                      rule70,
                                      rule71, rule72, rule73, rule74, rule75, rule76, rule77, rule78, rule79,
                                      rule80,
                                      rule81, rule82, rule83, rule84, rule85, rule86, rule87, rule88, rule89,
                                      rule90,
                                      rule91, rule92, rule93, rule94, rule95, rule96, rule97, rule98, rule99,
                                      rule100,
                                      rule101, rule102, rule103, rule104, rule105, rule106, rule107, rule108, rule109,
                                      rule110,
                                      rule111, rule112, rule113, rule114, rule115, rule116, rule117, rule118, rule119,
                                      rule120
                                      ])
tempoTotal = ctrl.ControlSystemSimulation(tempoTotal_ctrl)