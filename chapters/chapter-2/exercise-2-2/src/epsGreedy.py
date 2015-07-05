
import random
import numpy

class Agent:
    
    def __init__(self, policy, epsilon, numHandles):
        self.policy = policy
        self.epsilon = epsilon
        self.numHandles = numHandles
        self.rewardList = [0]*numHandles
        self.tries = [0]*numHandles
        self.selectionIndex = None
        self.tryNum = [0]
    
    def action(self):
        ### pulls a handle based on the rewardList
        self.selectionIndex = self.policy(self.rewardList,
                                          self.epsilon,
                                          self.tryNum)
        return self.selectionIndex
 
    def learn(self, selectionIndex, reward):
        ### updates rewardList
        oldMean = self.rewardList[self.selectionIndex]
        newMean = (oldMean*self.tries[selectionIndex] + reward) / (self.tries[selectionIndex] + 1)
        self.rewardList[self.selectionIndex] = newMean
        self.tries[selectionIndex] = self.tries[selectionIndex] + 1
        self.tryNum = numpy.sum(self.tries) + 1
    
def greedyPolicy(rewardList, epsilon, time):    
    ## picks the handle with the highest expected reward
    ## if multiple handles have highest reward select randomly 
    m = max(rewardList)
    return random.choice([i for i,j in enumerate(rewardList) if j == m])


def epsGreedy(rewardList, epsilon, time):
    
    greedy = numpy.random.binomial(n = 1, p = (1 - epsilon))
    
    if greedy == 1:
        m = max(rewardList)
        return random.choice([i for i,j in enumerate(rewardList) if j == m])
    else:
        return random.choice(range(len(rewardList)))
        
        
def epsGreedyD(rewardList, epsilon, time):
    
    epsilonD = epsilon/(log(time))
    greedy = numpy.random.binomial(n = 1, p = (1 - epsilonD))
    
    if greedy == 1:
        m = max(rewardList)
        return random.choice([i for i,j in enumerate(rewardList) if j == m])
    else:
        return random.choice(range(len(rewardList)))

