class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        time = 0
        heap, queue = [], deque()
        for key, val in count.items():
            heapq.heappush(heap, -val)
        
        while heap or queue:
            if not heap:
                time = queue[0][0]
            else:
                val = heapq.heappop(heap)
                if val + 1 < 0:
                    queue.append(((time+n), val+1))
            if queue and queue[0][0] <= time:
                t, val = queue.popleft()
                heapq.heappush(heap, val)
            time += 1



        return time