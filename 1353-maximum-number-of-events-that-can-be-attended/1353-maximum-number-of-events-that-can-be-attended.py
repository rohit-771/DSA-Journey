class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort()
        day=1
        i=0
        heap=[]
        meetings=0
        while len(heap) or i<len(events):
            while i<len(events) and events[i][0] == day:
                heapq.heappush(heap, events[i][1])
                i+=1
            while len(heap) and heap[0] < day:
                heapq.heappop(heap)
            if len(heap):
                meetings+=1
                heapq.heappop(heap)
            day+=1
        return meetings