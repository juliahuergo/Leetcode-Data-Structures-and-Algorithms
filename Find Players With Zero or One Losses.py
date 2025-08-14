class Solution(object):
    def findWinners(self, matches):
        ans = [[],[]]
        counts = defaultdict(int)
        players = set()
        
        for arr in matches:
            players.add(arr[0])
            players.add(arr[1])
            counts[arr[1]] += 1
        
        players = sorted(players)
        for player in players:
            if counts[player] == 0:
                ans[0].append(player)
            elif counts[player] == 1:
                ans[1].append(player)
        
        return ans
