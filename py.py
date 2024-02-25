import pandas as pd
import numpy as np
from scipy import stats



df = pd.read_excel('py.xlsx', engine='openpyxl')


costs = df['Cost'].values

z_scores = stats.zscore(costs)

threshold = 2  


abnormal_skus = df[np.abs(z_scores) > threshold]['SKU'].tolist()


print("Abnormal SKUs:", abnormal_skus)
