import heapq

pq = []

heapq.heappush(pq, (4, "John"))
heapq.heappush(pq, (2, "Sarah"))
heapq.heappush(pq, (5, "Mike"))
heapq.heappush(pq, (1, "Emma"))
heapq.heappush(pq, (3, "David"))

while pq:
    priority, patient = heapq.heappop(pq)
    print("Patient:", patient, '---', "Priority:", priority)
