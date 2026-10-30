class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        heap = []
        time = 0

        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 0
            freq[task] += 1

        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))

        res = []
        while heap or queue:
            while queue and queue[0][0]<time:
                _, task, value = queue.popleft()
                heapq.heappush(heap, (value, task))

            if heap:
                value, task = heapq.heappop(heap)
                res.append(task)
                if value+1 < 0:
                    queue.append((time+n, task, value+1))
            else:
                res.append("idle")
            time += 1

        return time


