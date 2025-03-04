import numpy as np
import matplotlib.pyplot as plt

# Generate values from -2π to 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Compute sine and cosine values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the sine wave
plt.plot(x, y_sin, label="Sine", color="blue")

# Plot the cosine wave
plt.plot(x, y_cos, label="Cosine", color="red")

# Labels and Title
plt.xlabel("X Values (radians)")
plt.ylabel("Y Values")
plt.title("Sine and Cosine Graph")

# Grid and Legend
plt.grid(True)
plt.legend()

# Show the graph
plt.show()
