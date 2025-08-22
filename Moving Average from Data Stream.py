from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        self.size = size
        self.queue = deque()

    def next(self, val):
        self.queue.append(val) 
        if len(self.queue) > self.size:
            self.queue.popleft()
        
        return sum(self.queue) / float(len(self.queue))
