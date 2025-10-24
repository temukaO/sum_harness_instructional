
import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "latency_comparison.png"

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

# Calculate memory latency (nanoseconds)
vector_latency = []
indirect_latency = []

for i in range(len(problem_sizes)):
    size = problem_sizes[i]
    
    # Vector sum latency
    vector_lat = (vector_times[i] / size) * 1e9  # Convert to nanoseconds
    vector_latency.append(vector_lat)
    
    # Indirect sum latency
    indirect_lat = (indirect_times[i] / size) * 1e9  # Convert to nanoseconds
    indirect_latency.append(indirect_lat)

plt.figure(figsize=(12, 8))

# Updated title and labels
plt.title("Memory Latency Comparison", fontsize=16, fontweight='bold')

xlocs = [i for i in range(len(problem_sizes))]
plt.xticks(xlocs, [f"{size/1e6:.0f}M" for size in problem_sizes])

# Plot latency
plt.plot(vector_latency, "b-x", linewidth=2, markersize=8, label="Vector Sum")
plt.plot(indirect_latency, "g-^", linewidth=2, markersize=8, label="Indirect Sum")

plt.xlabel("Problem Size", fontsize=14)
plt.ylabel("Memory Latency (nanoseconds)", fontsize=14)

# Updated legend
plt.legend(["Vector Sum", "Indirect Sum"], loc="best", fontsize=12)

plt.grid(axis='both', alpha=0.3)

plt.tight_layout()
plt.savefig(plot_fname, dpi=300, bbox_inches='tight')
plt.show()

print("Memory Latency Results:")
for i, size in enumerate(problem_sizes):
    print(f"Size {size/1e6:.0f}M: Vector={vector_latency[i]:.2f}ns, Indirect={indirect_latency[i]:.2f}ns")

# EOF