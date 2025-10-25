
import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "bandwidth_comparison.png"

peak_bandwidth = 204800000000  

fname = "performance_data.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)
print("var names =", var_names)

problem_sizes = df[var_names[0]].values.tolist()
direct_times = df[var_names[1]].values.tolist()
vector_times = df[var_names[2]].values.tolist()
indirect_times = df[var_names[3]].values.tolist()

#calculate memory bandwidth utilization
direct_bandwidth = []
vector_bandwidth = []
indirect_bandwidth = []

for i in range(len(problem_sizes)):
    size = problem_sizes[i]
    bytes_accessed = size * 8 
    
    direct_bw = (bytes_accessed / direct_times[i]) / peak_bandwidth * 100
    direct_bandwidth.append(direct_bw)
    
    vector_bw = (bytes_accessed / vector_times[i]) / peak_bandwidth * 100
    vector_bandwidth.append(vector_bw)
    
    indirect_bw = (bytes_accessed / indirect_times[i]) / peak_bandwidth * 100
    indirect_bandwidth.append(indirect_bw)

plt.figure(figsize=(12, 8))

plt.title("Memory Bandwidth Utilization")

xlocs = [i for i in range(len(problem_sizes))]
plt.xticks(xlocs, problem_sizes)

plt.plot(direct_bandwidth, "r-o", label="Direct Sum")
plt.plot(vector_bandwidth, "b-x", label="Vector Sum")
plt.plot(indirect_bandwidth, "g-^", label="Indirect Sum")

plt.xlabel("Problem Size")
plt.ylabel("Memory Bandwidth Utilization (%)")


plt.legend(["Direct Sum", "Vector Sum", "Indirect Sum"], loc="best")

plt.grid(axis='both')

plt.savefig(plot_fname, dpi=300)
plt.show()

# EOF
