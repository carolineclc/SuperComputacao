import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([200, 300, 900, 1300])
pythontime = np.array([0.64, 2.44, 100.02, 287.48])
ctime = np.array([0.0498435, 0.166017, 5.74352, 18.8561])
cmodifiedtime = np.array([0.0445861, 0.134049, 3.71698, 11.4424])

plt.plot(xpoints, pythontime, label='Linha python ')
plt.plot(xpoints, ctime, label='Linha C')
plt.plot(xpoints, cmodifiedtime,alpha=0.7, label='Linha C modificado')
plt.legend()
plt.show()