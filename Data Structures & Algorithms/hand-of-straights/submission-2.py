class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (not len(hand)%groupSize == 0):
            return False
        hMap = {}
        hand.sort()
        for elem in hand:
            if elem in hMap:
                hMap[elem] = hMap[elem] + 1
            else:
                hMap[elem] = 1
        for num in hMap:
            curr = hMap[num]
            if (curr > 0):
                for i in range(groupSize):
                    if (num+i in hMap):
                        if (hMap[num+i] < curr):
                            return False
                        hMap[num+i] -= curr
                    else:
                        return False
        return True