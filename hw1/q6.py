import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool

def sgn(a): 
    return 1 if a > 0 else -1

def PLA(D):
    w = np.zeros(5)
    updates = 0
    while True:
        has_errors = False
        for xy in D:
            x = xy[:5]; y = xy[5]
            sign = sgn(np.dot(w, x))
            if sign != y: 
                w +=  y * x
                has_errors = True
                updates += 1
        if not has_errors: break
    return updates 

# threads
def run_PLA_thread(data):
    D, seed = data
    rs = np.random.RandomState(seed)
    D_ = rs.permutation(D)
    # D_ = np.random.permutation(D)
    # print("=== seed: {} ===".format(seed))
    # print(D_)
    # print("=== end: {} ===".format(seed))
    return PLA(D_)
    # return [1], {"updates": 0}

# process inputs

def process_input(fname):
    train_6 = open(fname, "r")
    D = []
    for line in train_6:
        ls = line.split()
        D.append([1.] + [float(l) for l in ls])
    return np.array(D)

D = process_input("hw1_6_train.dat")

if __name__ == "__main__":
    seed = 5
    # run in thread pool
    with Pool(32) as p:
        result = p.map(run_PLA_thread, [(D, s) for s in range(seed, 1126+seed)]) # np.random.randint(1, 8000, size=1126)

    # plotting
    updates = np.array(result)  # get all the updates
    average = np.average(updates)

    print("Parameters:")
    print("\tSeeds: {} to {} (total {})".format(seed, seed+1126-1, 1126))
    print("Results:")
    print("\tAvg error rate:", average)
    # print("\tbins: {}".format(len(set(updates))))

    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(updates, bins=40) # plot into a histogram
    # ax.set_xticks(bins+0.5)

    # print( len(n), len(bins))


    # # do x first
    # for i in range(len(n)):
    #     x = bins[i]
    #     y = n[i]
    #     if y:
    #         ax.annotate( "{}".format(int(x+0.5), int(y)) , xy=(x, 0), xycoords='data',
    #             xytext=(x, -6), textcoords='data')

    ax.set_title('B05902100 - Q6 (avg updates: {:.5})'.format(average)) # set title
    ax.set_xlabel('No. of updates') # set labels
    ax.set_ylabel('Frequency') 
    plt.show()

