import heapq

def min_cost_connect(lengths):
    """
    Compute the minimal total cost to join all hoses into one.

    Parameters:
        lengths (list[int]): List of positive integers representing hose lengths.

    Returns:
        int: Minimal total cost to connect all hoses.
    """
    if not lengths or len(lengths) == 1:
        return 0

    # Convert the list into a min-heap
    heap = list(lengths)
    heapq.heapify(heap)

    total_cost = 0

    # Repeat until only one hose remains
    while len(heap) > 1:
        # Pop the two smallest hoses
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost = a + b
        total_cost += cost
        # Push the combined hose back into the heap
        heapq.heappush(heap, cost)

    return total_cost


# Optional manual test
if __name__ == "__main__":
    print(min_cost_connect([1,2,3,4]))   # 19
    print(min_cost_connect([5,2,4]))     # 18
    print(min_cost_connect([8,4,6,12]))  # 58
    print(min_cost_connect([20,4,8,2]))  # 54
