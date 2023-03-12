import heapq


def min_time_required(tasks):
    tasks.sort()  # 按任务的开始时间排序
    heap = []  # 用来存放当前正在运行的任务的结束时间

    for start, end, duration in tasks:
        # 找到当前时间之前结束的任务，把它们从 heap 中弹出
        while heap and heap[0] < start:
            heapq.heappop(heap)

        # 将当前任务的结束时间加入 heap
        heapq.heappush(heap, end)

    return len(heap)


print(min_time_required([[1, 2, 4], [3, 4, 3], [2, 3, 1]]))
print(min_time_required([[1, 3, 2], [2, 5, 3], [5, 6, 2]]))
