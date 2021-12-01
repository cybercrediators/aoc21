import numpy as np

print("1: ", np.sum(np.diff(np.loadtxt('input.txt', dtype=int))>0))
print("2: ", np.sum(np.diff(np.convolve(np.loadtxt('input.txt', dtype=int), np.ones(3,dtype=int), 'valid')) > 0))
