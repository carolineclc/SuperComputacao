import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([15, 30, 50, 100])

convulcao_1 = np.array([0.8544,1.72497, 2.88067,5.75853])
convulcao_4 = np.array([0.228873,0.453441 ,0.77043,1.53333])




plt.plot(xpoints, convulcao_1, label='1 CPU')
plt.plot(xpoints, convulcao_4, label='4 CPUs')

plt.xlabel("Iteracoes")
plt.ylabel("Tempo")


plt.legend()
plt.show()