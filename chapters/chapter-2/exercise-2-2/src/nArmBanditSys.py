
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
            handles[i] = Handle(numpy.random.normal, scale = scale)
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
a[1].pull()