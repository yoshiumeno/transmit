import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

def spline1(x,y,point):
    f = interpolate.interp1d(x,y,kind="cubic")
    X = np.linspace(x[0],x[-1],num=point,endpoint=True)
    Y = f(X)
    return X,Y


x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 287]
y = [800, 1000, 1200, 1600, 2000, 3000, 4000, 5000, 5500, 6000, 6000, 5500, 5000, 4000, 3000, 2000, 1700, 1600, 1500, 1400, 1200, 1100, 1000, 600, 200, 100, 100, 100, 100, 100]

a,b = spline1(x,y,287)

fout = open('hersys_data.csv','w')
for i in range(len(a)):
    print(i+1,',',int(b[i]/10),',',int(b[i]/10),',',int(b[i]/10),',',int(b[i]/10),',',int(b[i]/10),',',int(b[i]/10),',',int(b[i]/10),',',int(b[i]/10),',',int(b[i]/10),',',int(b[i]/10),file=fout)
fout.close()


plt.plot(a,b)
plt.show()

