import sys
data = []
n = 5
for k in range(n):
    a = len(data) #number of elements
    b = sys.getsizeof(data) #actual size in bytes
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
    data.append(None)
