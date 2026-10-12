import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y1 = [1, 4, 9, 16, 25]
y2 = [5, 10, 15, 20, 25]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Square")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Multiplication")

plt.show()