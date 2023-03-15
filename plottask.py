# program to plot a histogram of a normal distribution and the plot of a function
# Author: Daniel Mc Donagh

import matplotlib.pyplot as plt
import numpy as np
# import modules numpy for ability to use random generated number
# import mathplotlib to generate plots

# generates 1000 random numbers with a mean of 5 and std deviation of 1
x = np.random.normal(5, 1, 1000)

#plots the generated numbers as a hostogram with 100 bars
plt.hist(x, 100, label='Histogram Mean=5 Std Dev=1')

# sets font color and size to a dictionary object to be used for labels
font1 = {"family":"serif","color":"green","size":20}
font2 = {"family":"serif",'color':'darkred','size':15}


# adding labels to the plot
plt.title("Normal Histogram Distribution overlayed on Exponential Curve", fontdict=font1)
plt.xlabel("X Axis", fontdict=font2)
plt.ylabel("Y Axis Logarithmic Scale", fontdict=font2)

# overlays a grid on the plot
plt.grid()


# data poiints for function h(x)=x^3 added in manually
ypoints = np.array([0, 1, 8, 27, 54, 125, 216, 343, 512, 729, 1000])
xpoints = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# set yaxis to log scale to show both plots on same axis
plt.yscale("log")


plt.plot(xpoints, ypoints, label='Exponential Curve of function h(X)=X^3')

# plotss legend locked to upper left corner
plt.legend(loc='upper left')

# shows the plot 
plt.show()

