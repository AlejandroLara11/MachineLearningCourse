from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np
import matplotlib.pyplot as plt

data = np.array([[3], [8], [15], [6]])
scaler = MinMaxScaler()
scaler2 = StandardScaler()
scaled_data = scaler.fit_transform(data)
normalized_data = scaler2.fit_transform(data)

print(scaled_data)
print(normalized_data)
#plt.plot(scaled_data)
plt.plot(normalized_data)
plt.show()