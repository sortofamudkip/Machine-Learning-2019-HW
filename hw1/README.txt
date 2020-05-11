There are 4 files in this folder (excluding the README.txt):
* q6.py
* q7.py
* plot_q7.py
* q8.py

All of these files require the following environments:
* Python 3 with numpy, matplotlib, and multiprocessing modules (the latter being built-in).
* To run these files, simply type "python XXX.py" in a terminal.

Note that the resulting graphs themselves are on the pdf file submitted on gradescope, though you can get the same graphs by running the files in this folder.

q6.py
======
The code uses numpy to implement the PLA algorithm, matplotlib's hist function for plotting the updates, and multiprocessing's Pool and map functions to paralellize the work.
The code reads the file directly from "./hw1_6_train.dat".
It takes around <2 minutes on workstation to finish running.
Note that np.random.RandomState is used to shuffle the dataset because randomSeed is not thread-safe.
The most important parts of the code are the PLA function (line 8) and the plotting (line 63).

q7.py
======
The code reads the file directly from "./hw1_7_train.dat" and "./hw1_7_test.dat".
The code uses multiprocessing's Pool and map functions paralellize the work.
It takes an absurdly long time (<50 minutes on workstation) to finish running. It took even longer when numpy was used for some reason. 
This file saves the results into "q7.txt", the contents being each error rate seperated by a newline. 
Note that np.random.RandomState is used to shuffle the dataset because randomSeed is not thread-safe.
The most important parts of the code are the Pocket function (line 8) and writing the results to an output file (line 79).

plot_q7.py
=======
This code takes the result of q7.py's processing (which is saved into "./q7.txt") and draws a histogram.
The reason why this program exists is because q7 took forever to run so it was more efficient to save the results and plot later.
The plotting uses matplotlib's hist function.

q8.py
======
The code uses numpy to implement the PLA algorithm, matplotlib's hist function for plotting the updates, and multiprocessing's Pool and map functions to paralellize the work.
The code reads the file directly from "./hw1_7_train.dat" and "./hw1_7_test.dat".
It takes around <1 minute on workstation to finish running.
Note that np.random.RandomState is used to shuffle the dataset because randomSeed is not thread-safe.
The most important parts of the code are the Pocket function (line 8, though the function name is misleading) and the plotting (line 71).