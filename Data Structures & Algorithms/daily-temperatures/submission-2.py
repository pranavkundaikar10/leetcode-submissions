class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            print(f"current temp {temperatures[i]}")
            while stack and stack[-1][1] < temperatures[i]:
                idx, val = stack.pop()
                print(f"popped from stack {idx} and {val}")
                res[idx] = i - idx
            if i+1 < len(temperatures) and temperatures[i] < temperatures[i+1]:
                print('next large')
                res[i] = 1
            else:
                print(f'adding to stack {i} and {temperatures[i]}')
                stack.append((i, temperatures[i]))
            if stack:
                print(f'stack {stack[-1][1]}')
        return res
                

        