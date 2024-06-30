class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Initialize an empty double-ended queue (deque)
        deque_cards = deque()
      
        # Sort the deck in descending order and iterate over the cards
        for card in sorted(deck, reverse=True):
            # If the deque is not empty, move the last element to the front
            if deque_cards:
                deque_cards.appendleft(deque_cards.pop())
          
            # Insert the current card to the front of the deque
            deque_cards.appendleft(card)
      
        # Convert the deque back to a list before returning it
        return list(deque_cards)