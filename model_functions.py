import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib as plt

def center_scale(data):
    '''Centers and scales data'''
    new_data = data - data.mean()
    scaler = StandardScaler()
    return scaler.fit_transform(new_data)

def choose_PCA_elements(data):
    pca_test = PCA(n_components=data.shape[1])
    pca_test.fit(data)
    pcafeat_test = pca_test.transform(data)

    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.plot(pca_test.explained_variance_ratio_)

    ax2.plot(np.cumsum(pca_test.explained_variance_ratio_))
