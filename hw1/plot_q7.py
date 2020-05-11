import numpy as np
import matplotlib.pyplot as plt

def process_input(fname):
    with open(fname, "r") as f:
        plots = [float(line) for line in f]
    return np.array(plots)

if __name__ == "__main__":
    error_rate = process_input("q7.txt")
    avg = np.average(error_rate)

    fig, ax = plt.subplots()

    n, bins, patches = ax.hist(error_rate, bins=27) # plot into a histogram
    # ax.set_xticks(bins)
    # ax.set_xticklabels(bins,rotation=45)
    ax.set_title('B05902100 - Q7 (avg error rate: {:.5})'.format(avg)) # set title
    ax.set_xlabel('Error rate') # set labels
    ax.set_ylabel('Frequency') 
    plt.show()
