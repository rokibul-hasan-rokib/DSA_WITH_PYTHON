import heapq

pq = []
heapq.heappush(pq, (1, "Task A"))  # (priority, task)
heapq.heappush(pq, (2, "Task B"))
print(heapq.heappop(pq))