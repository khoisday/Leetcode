class doubleLinkedNode:
    def __init__(self, value = None, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.curr = doubleLinkedNode(homepage)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.curr.next = doubleLinkedNode(url,None,self.curr)
        self.curr = self.curr.next
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.curr.prev and steps > 0:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.value

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.curr.next and steps > 00:
            steps -= 1
            self.curr = self.curr.next 
        
        return self.curr.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)