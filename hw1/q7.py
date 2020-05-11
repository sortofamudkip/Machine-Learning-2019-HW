import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool

def sgn(a): 
    return 1 if a > 0 else -1

def Pocket(D):
    w = [0.] * 5
    TOTAL_UPDATES = 100
    best_w = [0.] * 5
    best_w_mistakes = evaluate(best_w, D)

    for i in range(TOTAL_UPDATES):
        done = True
        for x in D:
            y = x[5]
            sign = sgn(w[0]*x[0]+w[1]*x[1]+w[2]*x[2]+w[3]*x[3]+w[4]*x[4])
            if sign != y:
                done = False
                w[0] += y * x[0]
                w[1] += y * x[1]
                w[2] += y * x[2]
                w[3] += y * x[3]
                w[4] += y * x[4]
                mistakes = evaluate(w, D)
                if mistakes < best_w_mistakes:
                    best_w = list.copy(w)
                    best_w_mistakes = mistakes
        if done: break
    return best_w

def evaluate(w, Test):
    errors = 0.0
    for x in Test:
        y = x[5]
        sign = sgn(w[0]*x[0]+w[1]*x[1]+w[2]*x[2]+w[3]*x[3]+w[4]*x[4])
        if sign != y: errors += 1
    return float(errors / len(Test))

# threads
def run_thread(data):
    Train, Test, seed = data
    rs = np.random.RandomState(seed)
    Train_ = rs.permutation(Train) # shuffle data; this is thread safe supposedly
    w = Pocket(Train_) # get the pocket algorithm's w
    error_rate = evaluate(w, Test)
    
    print("finished:", seed)
    return error_rate

# process inputs

def process_input(fname):
    train_7 = open(fname, "r")
    D = []
    for line in train_7:
        ls = line.split()
        D.append([1.] + [float(l) for l in ls])
    return D

Train = process_input("hw1_7_train.dat")
Test = process_input("hw1_7_test.dat")

if __name__ == "__main__":
    seed = 5
    # run in thread pool
    with Pool(16) as p:
        result = p.map(run_thread, [(Train, Test, s) for s in range(seed, 1126+seed)])
    error_rate = np.array(result)

    avg = np.average(error_rate)

    print("Parameters:")
    print("\tSeeds: {} to {} (total {})".format(seed, seed+1126-1, 1126))
    print("Results:")
    print("\tAvg error rate:", avg)

    with open("q7.txt", "w") as f:
        for err in error_rate:
            f.write("{}\n".format(err))

    print("Results saved to q7.txt")


    # # plotting
    # fig, ax = plt.subplots()

    # n, bins, patches = ax.hist(error_rate, bins=100) # plot into a histogram
    # # ax.set_xticks(bins)
    # # ax.set_xticklabels(bins,rotation=45)
    # ax.set_title('B05902100 - Q7 (avg error rate: {:.5})'.format(avg)) # set title
    # ax.set_xlabel('Error rate') # set labels
    # ax.set_ylabel('Frequency') 
    # plt.show()

