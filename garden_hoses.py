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

# PS C:\Users\galan\ben_python\week-9-assignment-1-g
# PS C:\Users\galan\ben_python\week-9-assignment-1-garden-hoses-bishal482> pytest -q                  
                                                  
# ==================== ERRORS =====================
# ______ ERROR collecting tests/test_hw01.py ______
# tests\test_hw01.py:6: in <module>
#     main = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(main)
#                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# <frozen importlib._bootstrap_external>:1026: in exec_module
#     ???
# <frozen importlib._bootstrap>:488: in _call_with_frames_removed
#     ???
# garden_hoses.py:41: in <module>
#     sdfs
# E   NameError: name 'sdfs' is not defined
# ============ short test summary info ============ 
# ERROR tests/test_hw01.py - NameError: name 'sdfs' is not defined
# !!!! Interrupted: 1 error during collection !!!!! 
# 1 error in 0.22s
# PS C:\Users\galan\ben_python\week-9-assignment-1-garden-hoses-bishal482>