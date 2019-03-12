import matplotlib.pyplot as plt
x = list(range(-49, 50))
y = [n ** 2 - n + 2 for n in x]
plt.scatter(x, y)
plt.title('An Exponential Distribution, $y = x^2$')
plt.xlabel('$x$')
plt.ylabel('$x^2$')
plt.show()
