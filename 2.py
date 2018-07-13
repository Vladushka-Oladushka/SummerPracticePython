import numpy as np
import random 

n = int((input()))
a = np.zeros(n)

for i in range(n):
  rand_num = random.uniform(-1, 1)
  print("%.4f"% (rand_num))
  a[i] = rand_num

ar_mean = np.mean(a)
print("Arithmetic mean: ")
print(arr_mean)
