




import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np, tensorflow as tf
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import os


PRICED_BITCOIN_FILE_PATH = "data/pricedBitcoin2009-2018.csv"


def preprocessData():
    priced_bitcoin = pd.read_csv(PRICED_BITCOIN_FILE_PATH, sep=",")
    priced_bitcoin = priced_bitcoin[priced_bitcoin['year']==2016].reset_index(drop=True)
    priced_bitcoin_label = np.asarray(priced_bitcoin[['price']].values)
    row, column = np.asarray(priced_bitcoin_label).shape

    changing_prices = list()
    for i in range(row):
        changing_prices.append((priced_bitcoin_label[i] - priced_bitcoin_label[i-1])/priced_bitcoin_label[i-1])

    return changing_prices





changing_prices = preprocessData()
temp = np.asarray(changing_prices).flatten()
plt.hist(temp, bins='auto')
plt.show()
