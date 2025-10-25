
import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "latency_comparison.png"

fname = "performance_data.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)
print("var names =", var_names)

problem_sizes = df[var_names[0]].values.tolist()
direct_times = df[var_names[1]].values.tolist()
vector_times = df[var_names[2]].values.tolist()
indirect_times = df[var_names[3]].values.tolist()

#calculate memory latency
direct_latency = []
vector_latency = []
indirect_latency = []

for i in range(len(problem_sizes)):
    size = problem_sizes[i]
    
    direct_lat = (direct_times[i] / size) * 1e9
    direct_latency.append(direct_lat)
    
    vector_lat = (vector_times[i] / size) * 1e9
    vector_latency.append(vector_lat)

    indirect_lat = (indirect_times[i] / size) * 1e9
    indirect_latency.append(indirect_lat)

plt.figure(figsize=(12, 8))

plt.title("Memory Latency Comparison")

xlocs = [i for i in range(len(problem_sizes))]
plt.xticks(xlocs, problem_sizes)

plt.plot(direct_latency, "r-o", label="Direct Sum")
plt.plot(vector_latency, "b-x", label="Vector Sum")
plt.plot(indirect_latency, "g-^", label="Indirect Sum")

plt.xlabel("Problem Size")
plt.ylabel("Memory Latency (nanoseconds)")

plt.legend(["Direct Sum", "Vector Sum", "Indirect Sum"], loc="best")

plt.grid(axis='both')

plt.savefig(plot_fname, dpi=300)
plt.show()

# EOF