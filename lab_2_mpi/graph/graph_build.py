import matplotlib.pyplot as plt

N = []
T = []

with open(r"E:\Parallel_Programming\lab_1\multiple\timing\time_log.txt") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        parts = line.split()

        if len(parts) != 2:
            continue

        n, t = parts
        N.append(int(n))
        T.append(float(t))

plt.plot(N, T, marker="o")
plt.xlabel("Matrix size")
plt.ylabel("Time (s)")
plt.grid()
plt.show()