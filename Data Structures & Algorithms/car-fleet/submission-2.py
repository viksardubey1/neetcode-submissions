class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        sorted_cars = sorted(cars, key = lambda x: x[0], reverse = True)
        for car in sorted_cars:
            time = (target - car[0]) / car[1]
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)


        