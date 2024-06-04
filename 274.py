class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h = len(citations)
        
        while h > 0:
            if citations[h-1] >= h:
                break
            else:
                h -= 1

        return h


s = Solution()
print(s.hIndex(citations = [3,0,6,1,5]))