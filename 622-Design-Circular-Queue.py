from collections import deque

class MyCircularQueue(object):
    def __init__(self, k):
        """
        :type k: int
        """
        self.capacity = k
        self.queue = deque()
        self.size = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.size < self.capacity:
            self.queue.append(value)
            self.size += 1
            return True
        return False

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.size > 0:
            self.queue.popleft()
            self.size -= 1
            return True
        return False

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[0]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.capacity