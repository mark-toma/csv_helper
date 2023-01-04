#!/usr/bin/env python3

# This is a scratchpad for development

import numpy as np # Work with arrays and delimited text files of type CSV, TXT, etc.
import matplotlib.pyplot as plt

# See numpy reference for loadtxt()
#   https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html
# header = np.loadtxt(path, delimiter = ",", dtype = "string")

# Array of filenames to load
filenames = ["sine1", "sine2", "sine3", "sine4", "sine5"]

# Loop through filenames loading the contents and concatenating onto data
for filename in filenames:
    
    path = "data/" + filename + ".csv"
    print("Loading data from '" + path + "'")

    # Skip the header row and assume column IDs for data
    tmp = np.loadtxt(path, delimiter = ",", dtype = "float", skiprows = 1)
    
    # Handle initializing data otherwise concatenate tmp onto data
    if "data" in locals():
        print("Concatenating " + filename + " data...")
        data = np.concatenate((data, tmp))
    else:
        print("Initializing data from " + filename + "...")
        data = tmp

# Print out the data
print(data)

# Plot the data
plt.plot(data[:,0], data[:,1], "-xr")
plt.show()
