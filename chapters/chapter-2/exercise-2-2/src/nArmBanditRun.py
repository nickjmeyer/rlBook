

# takes in number of runs, agent and distribution 
# returns results
def run(Sys, Agent, runs = 1000):
     reward = Sys.handles[selectionIndex].pull()
     Agent.learn(selectionIndex, reward)