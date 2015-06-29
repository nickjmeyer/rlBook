
import random

class Agent:
    
    def __init__(self, policy, numHandles):
        self.policy = policy
        self.numHandles = numHandles
        self.rewardList = [0]*numHandles
        self.tries = [0]*numHandles
        self.selectionIndex = None
    
    def action(self):
        ### pulls a handle based on the rewardList
        self.selectionIndex = self.policy(self.rewardList)
        return self.selectionIndex
 
    def learn(self, reward):
        ### updates rewardList
        oldMean = self.rewardList[self.selectionIndex]
        newMean = (oldMean*self.tries[selectionIndex] + reward) / (self.tries[selectionIndex] + 1)
        self.rewardList[self.selectionIndex] = newMean
        self.tries[selectionIndex] = self.tries[selectionIndex] + 1
    
def greedyPolicy(rewardList):    
    ## picks the handle with the highest expected reward
    ## if multiple handles have highest reward select randomly 
    m = max(rewardList)
    return random.choice([i for i,j in enumerate(rewardList) if j == m])




