class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(i, j) for i, j in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []

        for i, car in enumerate(cars):
            t = (target - car[0])/ car[1]
            if stack and stack[-1] >= t:
                continue
            stack.append(t)

        return len(stack)