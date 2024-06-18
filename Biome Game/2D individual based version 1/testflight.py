from spicy import signal
import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
nurcle = np.array([[1, 1, 1], [1, 1, 1],[1, 1, 1]])
A1 = signal.convolve2d(data,nurcle)
A2 = signal.convolve2d(data, nurcle, "same")
print(A1, A2)

from WorldMapper import WorldMapper
A = np.zeros([240, 140])
B = np.zeros([240, 140])
A[30, 40] = 30
A1 = signal.convolve2d(A, nurcle)
WorldMapper.drawWorld(A1, B)



