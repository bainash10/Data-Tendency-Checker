import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
data = np.random.normal(loc=50, scale=10, size=1000)

# Calculate mean, median, and mode
mean = np.mean(data)
median = np.median(data)
mode = max(set(data), key=data.tolist().count)

# Plot histogram
plt.hist(data, bins=30, alpha=0.5, color='b', edgecolor='black')

# Add lines for mean, median, and mode
plt.axvline(mean, color='r', linestyle='dashed', linewidth=1, label='Mean')
plt.axvline(median, color='g', linestyle='dashed', linewidth=1, label='Median')
plt.axvline(mode, color='y', linestyle='dashed', linewidth=1, label='Mode')

# Add legend
plt.legend()

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Data with Mean, Median, and Mode')

# Show plot
plt.show()

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
