import matplotlib.pyplot as plt

T = [100, 0, 0, 0, 0]
x = [0, 0.25, 0.5, 0.75, 1]

r = 0.08

for step in range(20):
    new_T = T.copy()

    for i in range(1, 4):
        new_T[i] = T[i] + r * (T[i+1] - 2*T[i] + T[i-1])

    T = new_T

print("Final Temperature:", T)

plt.plot(x, T, marker="o")
plt.xlabel("Position (m)")
plt.ylabel("Temperature (C)")
plt.title("Heat Transfer in a Rod")
plt.grid()
plt.show()
