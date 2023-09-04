import numpy as np
import matplotlib.pyplot as plt

# simple scatter:
X_data = np.random.random(50) * 100
Y_data = np.random.random(50) * 100
#plt.scatter(X_data, Y_data, c="red", marker="^")

# simple lines
years = [2006 + x for x in range(16)]
weights = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80, 82, 82, 83, 81, 80, 79]
#plt.plot(years, weights, "r--", lw=3)

# simple bar
x = ["C++", "C#", "Python", "Java", "Go"]
y = [20, 50, 140, 1, 45]
#plt.bar(x, y, color='red', align="center", width=0.6, edgecolor='black', lw=3)

#simple histograms
ages = np.random.normal(20, 1.5, 1000)
#plt.hist(ages, bins=20, cumulative="true")

langs = ["Python", "C++", "Java", "C#", "Go"]
explodes = [0.1, 0, 0, 0, 0]
votes = [50, 24, 14, 6, 17]
#plt.pie(votes, labels=langs, explode=explodes, autopct="%.2f%%", pctdistance=0.7, startangle=90)

# simple bar plot
heights = np.random.normal(172, 8, 300)
plt.boxplot(heights)

plt.show()