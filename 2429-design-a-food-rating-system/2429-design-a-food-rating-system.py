
from sortedcontainers import SortedSet
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2353.Design%20a%20Food%20Rating%20System
        # Map food with its rating.
        self.food_rating_map = {}
        # Map food with the cuisine it belongs to.
        self.food_cuisine_map = {}

        # Store all food of cuisine in a set (to sort them on ratings/name)
        # Set element -> Tuple: (-1 * food_rating, food_name)
        self.cuisine_food_map = defaultdict(SortedSet)

        for i in range(len(foods)):
            # Store 'rating' and 'cuisine' of the current 'food' in 'food_rating_map' and 'food_cuisine_map' maps.
            self.food_rating_map[foods[i]] = ratings[i]
            self.food_cuisine_map[foods[i]] = cuisines[i]
            # Insert the '(-1 * rating, name)' element in the current cuisine's set.
            self.cuisine_food_map[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        # Fetch cuisine name for food.
        cuisine_name = self.food_cuisine_map[food]

        # Find and delete the element from the respective cuisine's set.
        old_element = (-self.food_rating_map[food], food)
        self.cuisine_food_map[cuisine_name].remove(old_element)

        # Update food's rating in 'food_rating' map.
        self.food_rating_map[food] = newRating
        # Insert the '(-1 * new rating, name)' element in the respective cuisine's set.
        self.cuisine_food_map[cuisine_name].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        highest_rated = self.cuisine_food_map[cuisine][0]
        # Return name of the highest-rated 'food' of 'cuisine'.
        return highest_rated[1]

    # def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
    #     self.rating = defaultdict(int)
    #     self.cuisines = defaultdict(list)
    #     for f, c, r in zip(foods, cuisines, ratings):
    #         self.rating[f] = [r, c]
    #         self.cuisines[c].append(f)
    #     self.highestRate = {}
    #     for c in self.cuisines.keys():
    #         self.calculate_food(c)

    # def changeRating(self, food: str, newRating: int) -> None:
    #     self.rating[food][0] = newRating
    #     c = self.rating[food][1]
    #     mx_f, mx_r = self.highestRate[c]
    #     if food != mx_f and (newRating > mx_r or newRating == mx_r and food < mx_f):
    #         self.highestRate[c] = [food, newRating]        
    #     else:
    #         self.calculate_food(c)

    # def highestRated(self, cuisine: str) -> str:
    #     return self.highestRate[cuisine][0]

    # def calculate_food(self, c:str):
    #     mx = 0
    #     food = ''
    #     for f in self.cuisines[c]:
    #         if mx < self.rating[f][0]:
    #             mx = self.rating[f][0]
    #             food = f
    #         elif mx == self.rating[f][0] and f < food:
    #             food = f
    #     self.highestRate[c] = [food, mx]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)