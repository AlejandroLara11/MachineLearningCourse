import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def load_dataset():
    iris = load_iris()
    x = iris.data
    y = iris.target
    return x, y
    
X, y = load_dataset()
# print(x)
# print(y)
y_pred = predict_randomly(x_size = X.shape[0])
print(y, y_pred)


def predict_randomly(x_size, num_clases = 3, seed = 42):
    np.random.seed(seed = seed)
    return np.random.randint(num_clases, size = x_size)

def compute_confusion_matrix(y_true, y_pred):
    num_classes = len(np.unique(y_true)) 
    confusion_matriz = np.zeros(num_classes, num_classes)
    for true_label, pred_label in zip(y_true, y_pred):
        confusion_matriz[true_label][pred_label] += 1
        