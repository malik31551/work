import math
import matplotlib.pyplot as plt

angles=[]
sinevals=[]
cosvals=[]
#print(a,round(math.sin(math.radians(a)),2)*100)
for a in range(0,361,10):
    angles.append(a)
    sinevals.append(round(math.sin(math.radians(a)),2)*100)
    cosvals.append(round(math.cos(math.radians(a)),2)*100)

print(angles)
print(sinevals)

plt.plot(angles,sinevals)
plt.plot(angles,cosvals)
plt.show()