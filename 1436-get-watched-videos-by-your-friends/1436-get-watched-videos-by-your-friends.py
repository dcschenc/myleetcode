from collections import deque, Counter
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = deque()
        queue.append(id)
        cur_level = 0
        movies = Counter()
        visited = set()
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node in visited:
                  continue
                visited.add(node)
                if cur_level != level:
                    for nb in friends[node]:                      
                        queue.append(nb)
                else:
                    for mv in watchedVideos[node]:
                        movies[mv] += 1
            cur_level += 1
            if cur_level > level:
                break
        sorted_items = sorted(movies.items(), key=lambda x: (x[1], x[0]))
        return [item[0] for item in sorted_items]