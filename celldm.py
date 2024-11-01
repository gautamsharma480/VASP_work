import numpy as np 


f=open('POSCAR1', 'r')


data=f.readlines()

a=[]
b=[]
c=[]
for num, i in enumerate(data):
	a.append(float(i.split()[0]))
	b.append(float(i.split()[1]))
	c.append(float(i.split()[2]))

a = np.array(a)
b = np.array(b)
c = np.array(c)

print(np.linalg.norm(a), '%2.10f' %0, '%2.10f' %0)
print('%2.10f' %0 ,np.linalg.norm(b), '%2.10f' %0)
print('%2.10f' %0, '%2.10f' %0 ,np.linalg.norm(c))

