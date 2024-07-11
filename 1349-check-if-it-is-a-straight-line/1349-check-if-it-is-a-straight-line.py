class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for x, y in coordinates[2:]:
            if (x - x1) * (y2 - y1) != (x2 - x1) * (y - y1):
                return False
        return True

        # x0, y0 = coordinates[0]
        # x1, y1 = coordinates[1]
        # if y1 == y0:
        #     for x, y in coordinates[1:]:
        #         if y != y0:
        #             return False
        #     return True
        # a = (x1 - x0) / (y1 - y0)
        # for x, y in coordinates[1:]:
        #     if y - y0 == 0 or (x - x0) / (y - y0) != a:
        #         return False
        # return True