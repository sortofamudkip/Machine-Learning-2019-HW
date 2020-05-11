
There are 2 files in this folder (excluding the README.txt):
* q7.py (which answers question 7 of the homework)
* q8.py (which answers question 8 of the homework)

All of these files require the following environments:
* Python 3 with numpy, matplotlib, time and multiprocessing modules (the latter two being built-in).
* To run these files, simply type "python XXX.py" in a terminal.

Note that the resulting graphs themselves are on the pdf file submitted on gradescope, though you can get the same graphs by running the files in this folder.

q7.py
======
The code uses numpy to implement the task, matplotlib's hist function for plotting the updates, and multiprocessing's Pool and map functions to paralellize the work. It saves the graph to a file named "20.png".
The code doesn't read data from anywhere as it is generated randomly in the code.
Note that np.random.RandomState is used to shuffle the dataset because randomSeed is not thread-safe.
The most important parts of the code are: making the dataset (line 10), Ein and Eout (line 21), choosing the best theta (line 32) and plotting (line 52). So basically most of the file.
The random seeds are fixed so you should get the same results each time you run.
The program prints the execution time, though you can ignore this as it isn't related to the homework.

q8.py
======
This is almost exactly the same as q7.py except the DATASIZE is set to 2000 instead of 20 and saves the graph to "2000.png". There are no significant differences outside of that.

TL;DR: q7.py is for question 7 and q8.py is for question 8.