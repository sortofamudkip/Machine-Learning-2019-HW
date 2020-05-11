import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool

def sgn(a): 
    return 1 if a > 0 else -1

def Pocket(D):
    w = np.zeros(5)
    TOTAL_UPDATES = 100
    count = 0

    while True:
        done = True
        for xy in D:
            x = xy[:5]; y = xy[5]
            sign = sgn(np.dot(w, x))
            if sign != y:
                done = False
                w += y * x
                count += 1
                if count == TOTAL_UPDATES: return w
        if done: break # to make sure the algorithm ends eventually; if w is all correct then count will not increase anyway
    return w

def evaluate(w, Test):
    errors = 0.0
    for xy in Test:
        x = xy[:5]; y = xy[5]
        sign = sgn(np.dot(w, x))
        if sign != y: errors += 1
    return float(errors / len(Test))

# threads
def run_thread(data):
    Train, Test, seed = data
    rs = np.random.RandomState(seed)
    Train_ = rs.permutation(Train) # shuffle data; this is thread safe supposedly
    w = Pocket(Train_) # get the pocket algorithm's w
    error_rate = evaluate(w, Test)
    return error_rate

# process inputs

def process_input(fname):
    train_7 = open(fname, "r")
    D = []
    for line in train_7:
        ls = line.split()
        D.append([1.] + [float(l) for l in ls])
    return np.array(D)

Train = process_input("hw1_7_train.dat")
Test = process_input("hw1_7_test.dat")

if __name__ == "__main__":
    seed = 5
    # run in thread pool
    with Pool(32) as p:
        result = p.map(run_thread, [(Train, Test, s) for s in range(seed, 1126+seed)])
    error_rate = np.array(result)

    avg = np.average(error_rate)

    print("Parameters:")
    print("\tSeeds: {} to {} (total {})".format(seed, seed+1126-1, 1126))
    print("Results:")
    print("\tAvg error rate:", avg)

    # plotting
    fig, ax = plt.subplots()

    n, bins, patches = ax.hist(error_rate, bins=100) # plot into a histogram
    # ax.set_xticks(bins)
    # ax.set_xticklabels(bins,rotation=45)
    ax.set_title('B05902100 - Q8 (avg error rate: {:.5})'.format(avg)) # set title
    ax.set_xlabel('Error rate') # set labels
    ax.set_ylabel('Frequency') 
    plt.show()

