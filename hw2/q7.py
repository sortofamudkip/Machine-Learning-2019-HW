import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
import time

def singlesign(a): return 1 if a > 0 else -1

sign = np.vectorize(singlesign)

def make_data(N: int, seed):
  def f(x):
    u = seed.uniform(); s = sign(x)
    # if u < 0.2: print("flip: {}".format(x))
    return s if u > 0.2 else -s 
  X = np.sort(seed.uniform(low= -1, high= 1, size=N))
  Y = np.array([f(x) for x in X])
  return X, Y

# def h(s, theta, x): return s * sign(x)

def Ein(X, Y, s, theta):
  def h(x):
    return s * sign(x - theta)
  results = h(X) != Y
  Ein = np.count_nonzero(results) / len(X)
  # print(f"{h(X)} vs {Y}", end=" ")
  # print("Ein = {}, s = {:+2}, theta = {}".format(Ein, s, theta))
  return Ein

def Eout(s, theta): return 0.5 + 0.3*s*(np.abs(theta)-1)

def run_thread(seed: int):
  DATASIZE = 20
  rs = np.random.RandomState(seed)
  X, Y = make_data(DATASIZE, seed=rs)
  best_Ein = np.inf; best_s = 777; best_theta = 888
  # list all possible dichotomies and choose the one with the lowest Ein
  for i in range(DATASIZE):
    theta = (X[i-1] + X[i])/2 if i > 0 else -1.0
    # s = +1
    Ein_positive = Ein(X, Y,  1, theta)
    if Ein_positive < best_Ein: best_Ein, best_s, best_theta = Ein_positive, 1, theta
    # s = -1
    Ein_negative = Ein(X, Y, -1, theta)
    if Ein_negative < best_Ein: best_Ein, best_s, best_theta = Ein_negative, -1, theta
  # get the best s and theta and then compare it to Eout
  assert best_Ein != np.inf and best_s != 777 and best_theta != 888
  eout = Eout(best_s, best_theta)
  # print(f"best s = {best_s}, best theta: {best_theta}, best Ein: {best_Ein}, Eout: {eout}")
  return best_Ein - eout

def plot(result):
  avg = np.average(result)

  fig, ax = plt.subplots()
  n, bins, patches = ax.hist(result, bins=30) # plot into a histogram
  ax.set_title('B05902100 - Q7 (avg Ein - Eout: {:.5})'.format(avg)) # set title
  ax.set_xlabel('Ein - Eout') # set labels
  ax.set_ylabel('Frequency') 
  plt.savefig("20.png")
  return avg


if __name__ == '__main__':
  seconds = time.time()
  seed = 1234
  # run in thread pool
  with Pool(8) as p:
      result = p.map(run_thread, [s for s in range(seed, 1000+seed)])
  
  print("time:", time.time() - seconds)
  avg = plot(result)
