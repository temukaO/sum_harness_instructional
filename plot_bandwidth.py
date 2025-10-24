
import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "bandwidth_comparison.png"

# Perlmutter CPU peak memory bandwidth
peak_bandwidth = 1.6e12  # 1.6 TB/s

# Load your actual performance data
fname = "performance_data.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)
print("var names =", var_names)

# Extract data
problem_sizes = df[var_names[0]].values.tolist()
direct_times = df[var_names[1]].values.tolist()
vector_times = df[var_names[2]].values.tolist()
indirect_times = df[var_names[3]].values.tolist()

# Calculate memory bandwidth utilization (%)
vector_bandwidth = []
indirect_bandwidth = []

for i in range(len(problem_sizes)):
    size = problem_sizes[i]
    bytes_accessed = size * 8  # 8 bytes per int64_t
    
    # Vector sum bandwidth
    vector_bw = (bytes_accessed / vector_times[i]) / peak_bandwidth * 100
    vector_bandwidth.append(vector_bw)
    
    # Indirect sum bandwidth
    indirect_bw = (bytes_accessed / indirect_times[i]) / peak_bandwidth * 100
    indirect_bandwidth.append(indirect_bw)

plt.figure(figsize=(12, 8))

# Updated title and labels
plt.title("Memory Bandwidth Utilization", fontsize=16, fontweight='bold')

xlocs = [i for i in range(len(problem_sizes))]
plt.xticks(xlocs, [f"{size/1e6:.0f}M" for size in problem_sizes])

# Plot bandwidth utilization
plt.plot(vector_bandwidth, "b-x", linewidth=2, markersize=8, label="Vector Sum")
plt.plot(indirect_bandwidth, "g-^", linewidth=2, markersize=8, label="Indirect Sum")

plt.xlabel("Problem Size", fontsize=14)
plt.ylabel("Memory Bandwidth Utilization (%)", fontsize=14)

# Updated legend
plt.legend(["Vector Sum", "Indirect Sum"], loc="best", fontsize=12)

plt.grid(axis='both', alpha=0.3)

plt.tight_layout()
plt.savefig(plot_fname, dpi=300, bbox_inches='tight')
plt.show()

print("Bandwidth Utilization Results:")
for i, size in enumerate(problem_sizes):
    print(f"Size {size/1e6:.0f}M: Vector={vector_bandwidth[i]:.2f}%, Indirect={indirect_bandwidth[i]:.2f}%")

# EOF
