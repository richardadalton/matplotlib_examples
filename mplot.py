import matplotlib.pyplot as plt

def square(x):
    return x * x

def double(x):
    return x + x

def plot_function(f):
    x = [i - 100 for i in range(201)]
    y = [f(n) for n in x]
    plt.plot(x,y)
    plt.show()
    plt.clf()


plot_function(square)
plot_function(double)