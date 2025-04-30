import seaborn as sns
import numpy as np


visitors = np.random.normal(500, 50, 100)

plt.figure(figsize=(7,5))
sns.histplot(visitors, bins=10, kde=True)
plt.title('Distribution of Daily Website Visitors')
plt.xlabel('Number of Visitors')
plt.ylabel('Frequency')
plt.show()
