class MinStack(object):
    def __init__(self):
        self.stack = []
        self.monoStack = []  # Monotonic stack to track minimums
        
    def push(self, val):
        \\\
        :type val: int
        :rtype: None
        \\\
        self.stack.append(val)
        # If monoStack is empty or new value is less than or equal to current min,
        # add to monoStack
        if not self.monoStack or val <= self.monoStack[-1]:
            self.monoStack.append(val)

    def pop(self):
        \\\
        :rtype: None
        \\\
        if not self.stack:
            return
        # If popped value is the current minimum, remove from monoStack too
        if self.stack[-1] == self.monoStack[-1]:
            self.monoStack.pop()
        self.stack.pop()

    def top(self):
        \\\
        :rtype: int
        \\\
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        \\\
        :rtype: int
        \\\
        if self.monoStack:
            return self.monoStack[-1]
        return None