class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        start = set()
        for u, v in paths:
            cities.add(u)
            cities.add(v)
            start.add(u)
        destination = cities - start
        return list(destination)[0]