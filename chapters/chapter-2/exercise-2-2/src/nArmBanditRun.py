
import matplotlib as plt
import numpy

# takes in number of runs, agent and distribution 
# returns results
def run(Sys, Agent, runs = 1000):
    r = [] * runs
    n = [] * runs
    ave = [] * runs
    for i in range(runs):
        selectionIndex = Agent.action()
        reward = Sys.handles[selectionIndex].pull()
        Agent.learn(selectionIndex, reward)
        r.append(reward)
        n.append(i)
        ave.append(numpy.mean(r[:i+1]))
    
    
    plt.pyplot.plot(n,ave)
    plt.pyplot.show()
    