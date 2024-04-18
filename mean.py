import numpy
n,m=map(int,input().strip().split())
array=numpy.array([list(map(int,input().strip().split()))for _ in range(n)])
print(numpy.mean(array,axis=1))
print(numpy.var(array,axis=0))
std_1=numpy.std(array,axis=None)
print(f"{std_1:.11f}")

