import pandas as pd
import numpy as np
import seaborn as sns

df_class = pd.read_csv('/Users/Caroline/Desktop/school/understanding_uncertainty/data/metabric.csv')

x = df_class['Tumor Size']
y = df_class['Overall Survival (Months)']
N = len(x)

y_hat = []
grid = np.sort(np.unique(x))
#grid

# LCLS formula

# Pick usual bandwidth
h = 1.06 * np.std(x) * N**(-0.2)
h

for z_j in grid:

    den = 0
    num = 0

    for index in range(N):   
        kernel = int(np.abs(x[index] - z_j) <= h)
        num += y[index] * kernel/(2*N*h) # Accumulating in proportion to probability that they occur; weighting values of y_i
        den += kernel/(2*N*h)# Can do N now or leave N for later - good to keep it normalized here bc keeps values small
    y_hat.append(num/den)
    # Or y_hat_z = num/den

print(y_hat)