#
# Contagem com tubo Geiger-Mueller
#
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Data
count_1  = np.array([63, 44, 49, 53, 48, 46, 56, 38, 54, 49])
count_10 = np.array([516, 494, 529, 581, 561])
count_60 = np.array([3341, 3075, 3039])
count_100 = np.array([5190])

# Plotting function
def plot_histogram_with_poisson(counts, title):
    mu = np.mean(counts)
    bins = np.arange(np.min(counts) - 0.5, np.max(counts) + 1.5, 1)
    plt.hist(counts, bins=bins, density=True, alpha=0.6, color='g', edgecolor='black')

    x_values = np.arange(np.min(counts), np.max(counts) + 1)
    plt.plot(x_values, poisson.pmf(x_values, mu), '-', color='black')

    plt.grid(linestyle='--', linewidth=0.6)
    plt.title(title)
    plt.xlabel('Count')
    plt.ylabel('Probability')
    plt.show()

# Plot each histogram with Poisson distribution
plot_histogram_with_poisson(count_1, r'$\Delta t$ = 1s')
plot_histogram_with_poisson(count_10, r'$\Delta t$ = 10s')
plot_histogram_with_poisson(count_60, r'$\Delta t$ = 60s')

count_total = np.concatenate([count_1, count_10/10, count_60/60, count_100/100])
plot_histogram_with_poisson(count_total, 'total')
