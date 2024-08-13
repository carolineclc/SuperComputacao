import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([200, 300, 900, 1300])
pythontime_cluster = np.array([0.82, 2.88, 81.06, 219.68])
ctime_cluster = np.array([0.0434071,0.145886, 4.03961, 12.4857])
cmodifiedtime_cluster = np.array([0.0132598, 0.0442508,1.16421, 3.49562])


pythontime = np.array([0.64,2.56 ,97.05 ,280.73 ])
ctime = np.array([0.0493944,0.170215, 5.64171, 18.7634])
cmodifiedtime = np.array([0.0497706, 0.171956,5.59915, 18.9563 ])

#plt.plot(xpoints, pythontime_cluster, label='Linha python Cluster ')
#plt.plot(xpoints, pythontime, label='Linha python ')
#plt.plot(xpoints, ctime_cluster, label='Linha C Cluster', color = "green")
#plt.plot(xpoints, ctime, label='Linha C', color = "red")
plt.plot(xpoints, cmodifiedtime_cluster,alpha=0.7, label='Linha C modificado Cluster', color = "purple")
#plt.plot(xpoints, cmodifiedtime,alpha=0.7, label='Linha C modificado ', color = "black")

plt.xlabel("Matrizes")
plt.ylabel("Tempo")


plt.legend()
plt.show()