class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sumGas = sumCost = 0
        for i in range(len(gas)):
            sumGas += gas[i]
            sumCost += cost[i]
        
        if sumCost > sumGas:
            return -1

        station = 0
        currTank = 0

        for i in range(len(gas)):
            currTank += gas[i] - cost[i]

            if currTank < 0:
                station = i + 1
                currTank = 0
        return station
