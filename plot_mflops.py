
import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "mflops_comparison.png"

fname = "performance_data.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)
print("var names =", var_names)

problem_sizes = df[var_names[0]].values.tolist()
direct_times = df[var_names[1]].values.tolist()
vector_times = df[var_names[2]].values.tolist()
indirect_times = df[var_names[3]].values.tolist()

#calculate MFLOP/s
direct_mflops = [(size / 1e6) / time for size, time in zip(problem_sizes, direct_times)]
vector_mflops = [(size / 1e6) / time for size, time in zip(problem_sizes, vector_times)]
indirect_mflops = [(size / 1e6) / time for size, time in zip(problem_sizes, indirect_times)]

plt.figure(figsize=(12, 8))

plt.title("MFLOP/s Performance Comparison")

xlocs = [i for i in range(len(problem_sizes))]
plt.xticks(xlocs, problem_sizes)

plt.plot(direct_mflops, "r-o", label="Direct Sum")
plt.plot(vector_mflops, "b-x", label="Vector Sum")
plt.plot(indirect_mflops, "g-^", label="Indirect Sum")

plt.xlabel("Problem Size")
plt.ylabel("MFLOP/s")

plt.legend(["Direct Sum", "Vector Sum", "Indirect Sum"], loc="best")

plt.grid(axis='both')

plt.savefig(plot_fname, dpi=300)
plt.show()

# EOF
