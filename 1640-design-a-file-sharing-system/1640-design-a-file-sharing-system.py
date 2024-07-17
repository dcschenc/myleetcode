from sortedcontainers import SortedSet, SortedList
# https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1500.Design%20a%20File%20Sharing%20System
class FileSharing:
    def __init__(self, m: int):
        self.cur = 0
        self.chunks = m
        self.reused = []
        self.user_chunks = defaultdict(set)

    def join(self, ownedChunks: List[int]) -> int:
        if self.reused:
            userID = heappop(self.reused)
        else:
            self.cur += 1
            userID = self.cur
        self.user_chunks[userID] = set(ownedChunks)
        return userID

    def leave(self, userID: int) -> None:
        heappush(self.reused, userID)
        self.user_chunks.pop(userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        if chunkID < 1 or chunkID > self.chunks:
            return []
        res = []
        for k, v in self.user_chunks.items():
            if chunkID in v:
                res.append(k)
        if res:
            self.user_chunks[userID].add(chunkID)
        return sorted(res)


# class FileSharing:
#     def __init__(self, m: int):
#         self.chunks = defaultdict(SortedSet)
#         self.users = defaultdict(Set)
#         self.ids = SortedList()       
        
#     def join(self, ownedChunks: List[int]) -> int:
#         mx = max(self.ids, default=0)
#         if len(self.ids) == mx:
#             user_id = mx + 1
#         else:
#             for i in range(1, mx):
#                 if i not in self.ids:
#                     user_id = i
#                     break
#         self.ids.add(user_id)
#         self.users[user_id] = set(ownedChunks)
#         for c in ownedChunks:
#             self.chunks[c].add(user_id)
#         return user_id        

#     def leave(self, userID: int) -> None:
#         for c in self.users[userID]:            
#             self.chunks[c].remove(userID)             
#         self.ids.remove(userID)    

#     def request(self, userID: int, chunkID: int) -> List[int]:        
#         users =  self.chunks[chunkID].copy()  
#         if len(users) > 0:    
#             self.chunks[chunkID].add(userID)
#             self.users[userID].add(chunkID)
#         return users


# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)