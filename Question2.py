from google.colab import files
uploaded = files.upload()
import pandas as pd

df = pd.read_excel("project3.xlsx.xlsx")

df
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(len(df[" Run time for different data size"]))
width = 0.25

plt.figure(figsize=(8,5))

plt.bar(x - width, df["Alg.1"], width, label="Algorithm 1")
plt.bar(x,         df["Alg.2"], width, label="Algorithm 2")
plt.bar(x + width, df["Alg.3"], width, label="Algorithm 3")

plt.xticks(x, df[" Run time for different data size"])

plt.title("Bar Chart of Algorithm Execution Time")
plt.xlabel("Data Size")
plt.ylabel("Run Time")
plt.legend()
plt.grid(axis='y')

plt.show()
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

plt.plot(df[" Run time for different data size"], df["Alg.1"],
         marker='o', markersize=6, linewidth=2, label='Algorithm 1')

plt.plot(df[" Run time for different data size"], df["Alg.2"],
         marker='s', markersize=6, linewidth=2, label='Algorithm 2')

plt.plot(df[" Run time for different data size"], df["Alg.3"],
         marker='^', markersize=6, linewidth=2, label='Algorithm 3')

plt.title("Line Chart of Algorithm Execution Time")
plt.xlabel("Data Size")
plt.ylabel("Run Time")
plt.grid(True)
plt.legend()

plt.show()
import matplotlib.pyplot as plt

plt.figure(figsize=(7,5))

plt.boxplot(
    [df["Alg.1"], df["Alg.2"], df["Alg.3"]],
    tick_labels=["Algorithm 1", "Algorithm 2", "Algorithm 3"],
    patch_artist=True
)

plt.title("Box Plot of Algorithm Execution Time")
plt.ylabel("Run Time")

plt.grid(axis='y')

plt.show()
from google.colab import files

uploaded = files.upload()
import pandas as pd

df = pd.read_excel("project3.xlsx")

df
mean_alg2 = df["Alg.2"].iloc[:6].mean()

print("Average execution time of Algorithm 2:", mean_alg2)
