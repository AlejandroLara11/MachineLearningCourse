import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(500) *100-50
# plt.plot(data)
# plt.show()

def min_max_scaler(data):
    dmin = np.min(data)
    dmax = np.max(data)
    return (data - dmin) / (dmax-dmin)

norm_data = min_max_scaler(data)
# plt.plot(norm_data)
# plt.show()

def standar_scaler(data):
    mean = np.mean(data)
    std = np.std(data)
    return (data-mean)/std

stand = standar_scaler(data)
plt.plot(stand)
plt.show()