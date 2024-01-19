import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

a = np.array([[1, 2],[4,5]])

print(a)

b = [1, 0, 0, 1]
d = [-1, 1,1,-1]
c =np.array(d)
a = np.array(b)
a = np.reshape(a, (2, 2))
c = np.reshape(c, (2, 2))
e = a + c
print("\n")
print(f"{a} + {c} = {e}")

l = 10
d = dict()

for i in range(10):
    d[i]= l
    l -= 1
print(d)

d = {}
d = {'Age': 20,
     'Height': 17,
     'Color': 'black'
     }
print(d)
d['Age'] = 21
d['Height'] = 1.8
d['Color'] = 'white'

print(d.keys())
print(d.values())
print(d.items())