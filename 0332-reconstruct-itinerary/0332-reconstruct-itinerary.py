class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        target  = collections.defaultdict(list)
            
        # sort in increasing order and we need small lexical so traverse from reverse  
        for s,d in sorted(tickets)[::-1]: 
            target[s].append(d)

            
        result = []
        def dfs(airport):
            while(target[airport]):
                dfs(target[airport].pop())
            result.insert(0,airport)
            
        dfs('JFK')
        
        return result