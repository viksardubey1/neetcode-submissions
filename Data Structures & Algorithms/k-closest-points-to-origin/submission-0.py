import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lambda_func = lambda x, y: (x**2 + y**2)**(1/2)
        heap = [(lambda_func(item[0], item[1]), item) for item in points]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            point = heapq.heappop(heap)
            res.append(point[1])
        return res


        