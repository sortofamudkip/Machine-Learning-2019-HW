import numpy as np
import matplotlib.pyplot as plt
from time import time as now
import json

def sgn(a): return 1 if a > 0 else -1

def process_input(fname):
    train_6 = open(fname, "r")
    D = []
    for line in train_6:
        ls = line.split()
        D.append([1.] + [float(l) for l in ls])
    return np.array(D)

def theta(s): return 1/(1+np.exp(-s))

Train = process_input("hw3_train.dat")
Y_pos = dimensions = len(Train[0]) - 1
Test = process_input("hw3_test.dat")


def get_err(w, D):
    err = 0
    X = D[:, :Y_pos]; Y = D[:, Y_pos]
    N = len(D)
    for i in range(N):
        if sgn(np.dot(X[i], w)) != Y[i]: err += 1
    return err / N

def get_ein(w): return get_err(w, Train)
def get_eout(w): return get_err(w, Test)

def gradient_descent():
    w = np.zeros(dimensions)
    T = 2000; eta = 0.01
    N = len(Train)

    Eins = np.empty(T+1); Eout = np.empty(T+1)
    Eins[0] = get_ein(w); Eout[0] = get_eout(w)

    X = Train[:, :Y_pos]; Y = Train[:, Y_pos]
    def compute_gradient():
        s = np.zeros(dimensions)
        for i in range(N):
            s += theta(-Y[i]* np.dot(w, X[i])) * (-Y[i]*X[i])
        return s / N
        
    for t in range(T):
        gradient = compute_gradient()
        w = w - eta * gradient
        Eins[t+1] = get_ein(w); Eout[t+1] = get_eout(w)

    return list(Eins), list(Eout)

def stochastic_gradient_descent():
    w = np.zeros(dimensions)
    T = 2000; eta = 0.001
    N = len(Train)
    X = Train[:, :Y_pos]; Y = Train[:, Y_pos]

    Eins = np.empty(T+1); Eout = np.empty(T+1)
    Eins[0] = get_ein(w); Eout[0] = get_eout(w)
        
    for t in range(T):
        y = Y[t % N]; x = X[t % N]
        w = w + eta * theta(-y * np.dot(w, x)) * (y * x)
        Eins[t+1] = get_ein(w); Eout[t+1] = get_eout(w)

    return list(Eins), list(Eout)

if __name__ == '__main__':
    before = now()

    ein_gradient_descent, eout_gradient_descent = gradient_descent()
    ein_stochastic_gradient_descent, eout_stochastic_gradient_descent = stochastic_gradient_descent()

    with open("results.json", "w") as f:
        results = {
            "ein_stochastic" : ein_stochastic_gradient_descent,
            "eout_stochastic": eout_stochastic_gradient_descent,
            "ein_gradient" : ein_gradient_descent,
            "eout_gradient": eout_gradient_descent
        }
        json.dump(results, f, indent=4)

    # plt.hist([ein_stochastic_gradient_descent, eout_stochastic_gradient_descent], label=['Ein, stochastic', 'Eout, stochastic'])
    # plt.legend(loc='upper right')
    # # plt.set_title("Stochastic Gradient Descent")
    # # plt.set_xlabel('Error rate') # set labels
    # # plt.set_ylabel('Frequency') 

    # plt.show()


    after = now()
    print("time:", after - before, "seconds")