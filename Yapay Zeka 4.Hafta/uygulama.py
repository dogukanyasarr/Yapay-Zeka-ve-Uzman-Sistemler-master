import numpy as np 
import skfuzzy as fuzz 
from skfuzzy import control as ctrl 
import matplotlib.pyplot as plt

kalite=ctrl.Antecedent(np.arange(0,11,1),"kalite")
servis=ctrl.Antecedent(np.arange(0,11,1),"servis")
bahşiş=ctrl.Consequent(np.arange(0,26,1),"bahşiş")

kalite.automf(3)
servis.automf(3)

bahşiş["düşük"]=fuzz.trimf(bahşiş.universe,[0,0,13])
bahşiş["orta"]=fuzz.trimf(bahşiş.universe,[0,13,25])
bahşiş["yüksek"]=fuzz.trimf(bahşiş.universe,[13,25,25])

kalite.view()

servis.view()

bahşiş.view()

kural1=ctrl.Rule(kalite["good"] | servis["good"],bahşiş["yüksek"])
kural2=ctrl.Rule(servis["average"] , bahşiş["yüksek"])
kural3=ctrl.Rule(kalite["poor"] | kalite["poor"],bahşiş["düşük"])

bahşişKontrol=ctrl.ControlSystem([kural1,kural2,kural3])
bahşişBelirleme=ctrl.ControlSystemSimulation(bahşişKontrol)

bahşişBelirleme.input["kalite"]=3.2
bahşişBelirleme.input["servis"]=2.4
bahşişBelirleme.compute()
print(bahşişBelirleme.output["bahşiş"])

bahşiş.view(sim=bahşişBelirleme)

plt.show()