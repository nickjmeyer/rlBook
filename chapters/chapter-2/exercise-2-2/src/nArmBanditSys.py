
import numpy

class Handle:
    
    # initiate handle with random distribution of rewards
    def __init__(self, dist, **kwargs):
        self.dist = dist
        self.kwargs = kwargs
    
    # returns reward amount
    def pull(self):
        return self.dist(**self.kwargs)
        
        
def NormalHandles(loc = 0.0,scale = 1.0,n = None):
    if n == None:
        handles = Handle(numpy.random.normal, loc = loc, scale = scale)
    else:
        handles = [None]*n
        for i in range(n):
            handles[i] = Handle(numpy.random.normal, loc = loc, scale = scale)
    return handles
    
def EponentialHandles(scale = 1.0,n = None):
    if n == None:
        handles = Handle(numpy.random.exponential, scale = scale)
    else:
        handles = [None]*n
        for i in range(n):
            handles[i] = Handle(numpy.random.exponential, scale = scale)
    return handles
        
class Sys:
    def __init__(self, handles):
        if isinstance(handles, list):
            self.n = len(handles)
            self.handles = handles
        elif isinstance(Handle, handles):
            self.n = 1
            self.handles = [handles]
        else:
            pass
            ### print an error
            ### handles must either be a list of Handle objects 
            ### or a Handle object itself
            
a = NormalHandles(loc = 5.0, scale = 2.0, n = 10)
b = EponentialHandles(scale = 3, n = 10)
a[1].pull()

h1 = Handle(numpy.random.normal, loc = 10, scale = 2)
h2 = Handle(numpy.random.normal, loc = 8, scale = 3)
h3 = Handle(numpy.random.normal, loc = -2, scale = 5)
h4 = Handle(numpy.random.normal, loc = 6, scale = 1)
h5 = Handle(numpy.random.exponential, scale = 2)

hand = [h1, h2, h3, h4, h5]

s = Sys(hand)
barry = Agent(greedyPolicy, 0.1, 5)
run(s, barry)
barry.rewardList
barry.tries