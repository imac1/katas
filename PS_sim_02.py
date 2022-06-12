import math
import random

x = ["phosfluorescently", "authoritatively",
     "enthusiastically", "monotonectally", "appropriately"]
y = ["strategize", "unleash", "right-shore", "expedite", "enhance", "initiate", "evisculate", "matrix", "communicate", "simplify", "predominate", "supply",
     "facilitate", "exploit", "re-engineer", "visualize", "syndicate", "repurpose", "transition", "architect", "grow", "e-enable", "develop", "evolve", "redefine"]
z = ["cross functional", "standardized", "state of the art", "sticky", "seamless", "team driven", "cutting-edge", "world-class", "resource-sucking", "cross-media",
     "holistic", "accurate", "compelling", "resource-maximizing", "high standards in", "top-line", "timely", "viral", "interdependent", "robust", "prospective"]
t = ["innovation", "action items", "data", "technology",
     "testing procedures", "e-services", "materials", "benefits", "vortals"]

a = random.randint(0, 10) # salveaza 10 int random de la 0 la 9
b = random.randint(0, 10)
c = random.randint(0, 10)
d = random.randint(0, 10)

print("The way to move forward is to ")

w = []
'''
 # creeaza o bucla care se repeta de 3 ori 
  #(fiindca scopul e sa aleaga un index pentru fiecare lista x, y, z, t )
'''
while len(w) < 4:
  
    while 1:
        try:
            w.append(x[a])
            break
        except IndexError:
            a = random.randint(0, 10)

    while 1:
        try:
            w.append(y[b])
            break
        except IndexError:
            b = random.randint(0, 10)

    while 1:
        try:
            w.append(z[c])
            break
        except IndexError:
            c = random.randint(0, 10)

    while 1:
        try:
            w.append(t[d])
            break
        except IndexError:
            d = random.randint(0, 10)

    break

for i in w:  # printeaza fiecare item din noua lista de cuvinte
    print(i) 

'''
trebuie sa construiasca o propozitie din cuvinte aleatoare aflate in 4 liste diferite
'''