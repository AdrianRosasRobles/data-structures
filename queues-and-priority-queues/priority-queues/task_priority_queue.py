import heapq

pq = []

heapq.heappush(pq, (3, "Email client"))
heapq.heappush(pq, (1, "Fix critical bug"))
heapq.heappush(pq, (2, "Update website"))
heapq.heappush(pq, (1, "Production outage"))

while pq:
    priority, task = heapq.heappop(pq)
    print("Task:", task, '---', "Priority:", priority)
