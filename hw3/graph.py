import matplotlib.pyplot as plt
import json
import numpy as np


with open("results.json", "r") as f:
    results = json.load(f)

ein_gradient = results["ein_gradient"]
ein_stochastic = results["ein_stochastic"]


# Ein
fig1, ax1 = plt.subplots()
index = np.arange(len(ein_gradient))
ax1.plot(index, ein_gradient, label="Gradient Ein", color="b") 
ax1.plot(index, ein_stochastic, label="Stochastic Ein", color="g") 
ax1.set_title('B05902100 - Ein - T = 2000') # set title
ax1.legend()
ax1.set_xlabel('t') # set labels
ax1.set_ylabel('Ein') 

eout_gradient = results["eout_gradient"]
eout_stochastic = results["eout_stochastic"]
fig2, ax2 = plt.subplots()
ax2.plot(index, eout_gradient, label="Gradient Eout", color='b') 
ax2.plot(index, eout_stochastic, label="Stochastic Eout", color="g") 
ax2.set_title('B05902100 - Eout - T = 2000') # set title
ax2.legend()
ax2.set_xlabel('t') # set labels
ax2.set_ylabel('Eout') 



plt.show()