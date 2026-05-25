import matplotlib.pyplot as plt

N = []
Threads = []
T = []

with open(r"E:\Parallel_Programming\lab_1\lab_2_mpi\multiple\timing_omp\time_log1.txt") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        parts = line.split()

        if len(parts) != 3:
            continue

        n, th, t = parts

        N.append(int(n))
        Threads.append(int(th))
        T.append(float(t))


plt.plot(N, T, marker="o")
plt.xlabel("Matrix size")
plt.ylabel("Time (s)")
plt.grid()
plt.show()
