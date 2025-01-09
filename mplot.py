import matplotlib.pyplot as plt

def square(x):
    return x * x


# Call this to generate the plot on screen.
def plot_function(f):
    x = [i - 100 for i in range(201)]
    y = [f(n) for n in x]
    plt.plot(x,y)
    plt.show()
    plt.clf()

# Can pass a function, or a lambda
plot_function(square)
plot_function(lambda x: x + x)


# Call this to save the plot to a file.
def save_plot_function(f, filename):
    x = [i - 100 for i in range(201)]
    y = [f(n) for n in x]
    plt.plot(x,y)
    plt.savefig(filename)
    plt.clf()

# File format is dictated by the extension in the filename
# save_plot_function(square, "square.png")
# save_plot_function(lambda x: x + x, "double.pdf")
