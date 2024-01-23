import time
import numpy as np
# testing synctactic sugar
alphabets = ['A', 'B', 'C', 'D']
print(alphabets)
for i in alphabets:
    print(i)
# with syntactic sugar

print(*alphabets)
print("=="*1000, "\npart 2")
print("python"[::-1])
big_number = 1_000_000_000
print(big_number)
print(25 < 30)

# testing vectorization
print("=="*1000, "\nloop")
start = time.time()
# iterative sum
total = 0
# iterating through 1.5 Million numbers
for item in range(0, 100_001):
    total = total + item
print(f'sum is: {total}')
end = time.time()
print(f'Execution time using loop = {end-start}')
print("=="*100, "\nVectorization")
start = time.time()
# vectorized sum - using numpy for vectorization
# numpy.arange create a sequence of the numbers from 0 to 1499999
arrange = np.asarray(np.arange(100_001))
print(f'arange: {arrange}')
print(np.sum(arrange))
# c'est limité
end = time.time()
print(f'Execution time vectorization = {end-start}')