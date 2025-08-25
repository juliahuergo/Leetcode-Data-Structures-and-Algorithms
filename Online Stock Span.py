class StockSpanner(object):

    def __init__(self):
        self.stack = [] 
        self.nums = []

    def next(self, price):
        ans = 1
        while self.stack and price >= self.nums[self.stack[-1]]:
            self.stack.pop()
        
        if self.stack:
            ans = len(self.nums) - self.stack[-1]
        elif len(self.nums) != 0:
            ans = len(self.nums) + 1
            
        self.nums.append(price)
        self.stack.append(len(self.nums)-1)
        return ans
