"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot, and saves it to a file named "myplot.png"

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""


import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "mflops_comparison.png"

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

# Calculate MFLOP/s
direct_mflops = [(size / 1e6) / time for size, time in zip(problem_sizes, direct_times)]
vector_mflops = [(size / 1e6) / time for size, time in zip(problem_sizes, vector_times)]
indirect_mflops = [(size / 1e6) / time for size, time in zip(problem_sizes, indirect_times)]

plt.figure(figsize=(12, 8))

# Updated title and labels
plt.title("MFLOP/s Performance Comparison", fontsize=16, fontweight='bold')

xlocs = [i for i in range(len(problem_sizes))]
plt.xticks(xlocs, [f"{size/1e6:.0f}M" for size in problem_sizes])

# Plot MFLOP/s instead of time
plt.plot(direct_mflops, "r-o", linewidth=2, markersize=8, label="Direct Sum")
plt.plot(vector_mflops, "b-x", linewidth=2, markersize=8, label="Vector Sum")
plt.plot(indirect_mflops, "g-^", linewidth=2, markersize=8, label="Indirect Sum")

plt.xlabel("Problem Size", fontsize=14)
plt.ylabel("MFLOP/s", fontsize=14)

# Updated legend
plt.legend(["Direct Sum", "Vector Sum", "Indirect Sum"], loc="best", fontsize=12)

plt.grid(axis='both', alpha=0.3)
plt.yscale("log")  # Log scale for better visualization

plt.tight_layout()
plt.savefig(plot_fname, dpi=300, bbox_inches='tight')
plt.show()

print("MFLOP/s Results:")
for i, size in enumerate(problem_sizes):
    print(f"Size {size/1e6:.0f}M: Direct={direct_mflops[i]:.1f}, Vector={vector_mflops[i]:.1f}, Indirect={indirect_mflops[i]:.1f}")


# EOF
