import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [stone * -1 for stone in stones]
        heapq.heapify(new_stones)
        while len(new_stones) != 1:
            heaviest = heapq.heappop(new_stones) * -1
            second_heaviest = heapq.heappop(new_stones) * -1
            heapq.heappush(new_stones, -1 * abs(heaviest - second_heaviest))
        return heapq.heappop(new_stones) * -1


        