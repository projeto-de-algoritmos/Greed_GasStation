class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        tank = 0
        canCompleteCircuit = 0
        specificValue = {}
        for k in range(len(gas)):
            result = gas[k]-cost[k]
            if result not in specificValue: 
                specificValue[result] = [k]
            else:
                specificValue[result].append(k)
        keyList = list(specificValue.keys())
        keyList.sort(reverse=True)
        for key in keyList:
            for idx in specificValue[key]:
                start_station = idx
                for i in range(idx, len(gas)*2):
                    index = i % len(gas)
                    tank += gas[index]
                    tank -= cost[index]
                    if tank < 0:
                        tank = 0
                        break
                    idx_next_station = (index + 1) % len(gas)
                    if start_station == idx_next_station:
                        canCompleteCircuit = 1
                        break
                if canCompleteCircuit:
                    break
            if canCompleteCircuit:
                break
        return start_station