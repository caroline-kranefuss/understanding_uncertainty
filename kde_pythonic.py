# %%
import seaborn as sns
import numpy as np


# %%
def kde_est(x, plot=True, kernel='gaussian'):
    grid = np.sort(np.unique(x))
    N = len(x)
    h = 1.06 * np.std(x) * N**(-0.2)

    # Can start the kde as kde = 0 * grid.copy()

    # Or:

    kde = []
    for z in grid:
        density_value = 0
        for x_i in x:

            if kernel == 'gaussian':
                new_value = np.exp(-0.5 * (z - x_i)**2/h) / np.sqrt(2 * np.pi * h ** 2)
            elif kernel == 'uniform':
                new_value = -5 * int(np.abs(z - x_i) <= h)
            else:
                print("Invalid kernel.")

            density_value += new_value/N # Normalizing

        if plot:
            sns.lineplot(x=grid, y=kde)

        return kde
    
    # %%
    kde_est(x, kernel='uniform') # Here, x would be a col from a df 
# %%
