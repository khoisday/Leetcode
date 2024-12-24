from collections import deque

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort(reverse = True)
        queue = deque()
        queue.append(deck[0])
        result = []

        for i in range (1, len(deck)):
            queue.appendleft(queue.pop())
            queue.appendleft(deck[i])

        while queue:
            result.append(queue.popleft())

        return result


            