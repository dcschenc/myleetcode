from heapq import heappush, heappop
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1648.Sell%20Diminishing-Valued%20Colored%20Balls
        count = defaultdict(int)
        mod = 10**9 + 7
        for item in inventory:
            count[item] += 1
        
        maxHeap = []
        for key, value in count.items():
            heapq.heappush(maxHeap, (-key, key, value))
        
        ans = 0
        while orders > 0:
            # Highest value
            _, firstMax, firstFreq = heapq.heappop(maxHeap)
            if len(maxHeap) > 0:
                # The second highest value to determine the range of items we are going to sell
                _, secondMax, secondFreq = heapq.heappop(maxHeap)
            else:
                # We have a case that we have only 1 item in heap, so simply set the second max as 0 to avoid edge cases
                secondMax, secondFreq = 0, 0

            # Calculate total of items we can sell in the max - second max group
            canSell = (firstMax - secondMax) * firstFreq
            if orders >= canSell:
                # Simply sell all items in the range
                orders -= canSell
                amount = firstMax * (firstMax + 1) // 2 - secondMax * (secondMax + 1) // 2
                ans += firstFreq * amount
                ans = ans % mod
                heapq.heappush(maxHeap, (-secondMax, secondMax, firstFreq + secondFreq))
            else:
                groupSize = orders // firstFreq
                remainder = orders % firstFreq
                amount = firstMax * (firstMax + 1) // 2 - (firstMax - groupSize) * (firstMax - groupSize + 1) // 2
                ans += firstFreq * amount
                ans += remainder * (firstMax - groupSize)
                ans = ans % mod
                orders = 0

        return ans

        inventory.sort(reverse=True)
        mod = 10**9 + 7
        ans = i = 0
        n = len(inventory)
        while orders > 0:
            while i < n and inventory[i] >= inventory[0]:
                i += 1
            nxt = 0
            if i < n:
                nxt = inventory[i]
            cnt = i
            x = inventory[0] - nxt
            tot = cnt * x
            if tot > orders:
                decr = orders // cnt
                a1, an = inventory[0] - decr + 1, inventory[0]
                ans += (a1 + an) * decr // 2 * cnt  ## avarege price (a1 + an)*decr//2
                ans += (inventory[0] - decr) * (orders % cnt)
            else:
                a1, an = nxt + 1, inventory[0]
                ans += (a1 + an) * x // 2 * cnt  ## avarege price (a1 + an)*decr//2
                inventory[0] = nxt
            orders -= tot
            ans %= mod
        return ans
        
        # inventory.sort(reverse=True)
        MOD = 10**9 + 7
        heap = [-num for num in inventory if num is not 0]
        heapq.heapify(heap)
        profit = 0
        fulfilled = 0
        amt = heapq.heappop(heap)
        size = 0
        next_ = amt
        while fulfilled < orders:
            while next_ == amt:
                size +=1

                if len(heap) > 0:
                    next_ = heapq.heappop(heap) 
                else: 
                    next_ = 0
            n = int(size * (-1)*(amt - next_))
            n = min(n, orders - fulfilled)
            remove_each, remove_rem = divmod(n, size)
            profit += size*(remove_each*(2*(-1)*amt - (remove_each-1))//2)
            amt += remove_each
            profit += (-1)*amt*remove_rem
            fulfilled += n
        return int(profit % MOD)

        """
        Using a heap means we don't necessarily have to sort the list. 
        When we have lots of balls with high inventory and small orders, 
        we won't do nlogn. Further, if we are keeping track of our 
        inventory in a heap, and the inventory doesn't change, we can 
        avoid resorting when a new set of orders comes in.        """

        heap = [-num for num in inventory if num is not 0]

        heapq.heapify(heap)

        profit = 0
        fulfilled = 0
        amt = heapq.heappop(heap)
        size = 0


        """
        ball with the highest inventory is at the top of the heap
        """
        next_ = amt

        while fulfilled < orders:

            """
            find all balls that have inventory equal to the ball(s) with 
            the highest current inventory -> 'amt'. These are the only 
            balls currently under consideration for sale right now. If we 
            sold any other balls, we wouldn't make as much. At the end 
            there will be 'size' such balls and the 'next_' ball we see 
            will have an inventory less than the balls under consideration.
            """

            while next_ == amt:
                size +=1

                if len(heap) > 0:
                    next_ = heapq.heappop(heap) 
                else: 
                    next_ = 0

            
            """ 
            all 'size' balls under consideration have the same inventory. 
            In order to maximize profit, we will select a ball from each 
            color, one after the other until they again have the same 
            inventory. We continue to do this until the inventory for each 
            ball is equal to the 'next_' lowest ball. We don't go any 
            further with our current balls under consideration because we 
            will need to include the 'next_' ball to maximize our profit. 
            """
            

            """
            Since we must stop at the inventory of 'next_', we can      
            decrease theinventory of each ball under consideration by amt_ 
            - next. This will beused to fulfill the order. Since we do 
            this for all balls currently under consideration which total 
            'size'. The max number of balls we can add to the order right 
            now is 'n' as below
            """

            n = int(size * (-1)*(amt - next_))

            """
            However, we can't add more than is currently required to 
            fulfill the order, so we will take the minimum of the max 
            balls we can add the order and the order minus the amount we  
            have already fullfilled. 
            """

            n = min(n, orders - fulfilled)

            """
            As mentioned above, the order in which we take the balls from 
            inventory which maximizes the profit is to take from each ball 
            once until they all have the same inventory and then repeat. 
            The number of times that we can do this is going to be the 
            total number of balls we are going to remove, 'n', divided by 
            the number of balls under consideration, 'remove_each'. There 
            may be some balls remaining that don't add up to size and we 
            can take these remaining balls in the last round, remove_rem
            """

            remove_each, remove_rem = divmod(n, size)

            """ 
            First we calculate the profit from removing each ball in each 
            'remove_each' round. Consider one ball. In the first 
            iteration, it's price is 'amt', the second time it's removed, 
            it is amt-1, then amt-2 and so on until in the last round, it 
            is amt-(remove_each -1). In otherwords, for each ball, the 
            profit gained through this process will be  amt + amt -1 + amt 
            -2 +...+ amt - (remove_each -1) = remove_each*amt - (1+2+...+
            (remove_each-1)). We can recognize the last part as the sum of 
            i from i =1 to remove_each -1 (k(k+1)/2)So we have remove_each 
            *amt - (remove_each -1)(remove_each)/2. In order to avoid 
            overflow, we rearrage the formula to (remove_each*(2*(-1)*amt 
            - (remove_each-1))//2). because our heap is a min heap and all 
            values are negative, we multiply amt by (-1). This is the 
            profit for each ball under consideration so we multiply this 
            by the number of balls under consideration 'size' 
            """

            profit += size*(remove_each*(2*(-1)*amt - (remove_each-1))//2)

            """
            reduce the inventory of each ball under consideration by the 
            number of rounds we made.
            """
            amt += remove_each

            """
            If there is a remainder, which only occurs when we can sell 
            more balls than required, cover that remainder with as many 
            balls as required. 
            """
            profit += (-1)*amt*remove_rem

            """
            update the number of balls we fulfilled in this round and 
            repeat.
            """
            fulfilled += n


        return int(profit % MOD)