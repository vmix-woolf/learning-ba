import matplotlib.pyplot as plt
import numpy as np

# Визначаємо діапазон n
n = np.arange(1, 100)

# Обчислюємо значення для різних часових складностей
O_1 = np.ones_like(n)
O_n = n
O_n_squared = n**2
O_n_cubed = n**3

# Побудова графіка
plt.figure(figsize=(12, 8))
plt.plot(n, O_1, label="O(1)")
plt.plot(n, O_n, label="O(n)")
plt.plot(n, O_n_squared, label="O(n^2)")
plt.plot(n, O_n_cubed, label="O(n^3)")
plt.xlabel("n")
plt.ylabel("Operations")
plt.title("Основні часові складності алгоритмів")
plt.legend()
plt.grid(True, which="both", ls="--", c='0.65')
plt.show()
