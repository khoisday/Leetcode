class TopVotedCandidate:
    def __init__(self, persons, times):
        self.times = times
        self.leaders = []
        vote_count = {}  # Track vote counts
        leader = None    # Current leader
        
        # Calculate leader at each voting time
        for p in persons:
            vote_count[p] = vote_count.get(p, 0) + 1
            
            # Update leader if current person has more or equal votes
            if leader is None or vote_count[p] >= vote_count[leader]:
                leader = p
            
            self.leaders.append(leader)
    
    def q(self, t):
        # Find the largest time index less than or equal to t
        i = bisect.bisect_right(self.times, t) - 1
        return self.leaders[i] if i >= 0 else None