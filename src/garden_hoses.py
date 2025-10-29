"""
HW01 — Garden Hoses: Minimal Join Cost

Implement min_cost_connect(lengths) -> int

Behavior:
- Given a list of positive integers (hose lengths), return the minimal total cost
  to connect all hoses into one, where joining two hoses costs the sum of their lengths.
- If the list has 0 or 1 item, return 0.

Steps TODO:
1) Read & Understand: restate the problem in your own words.
2) Re-phrase: explain why always joining the two shortest hoses is best.
3) Identify: inputs (list), output (int), variables (heap, total).
4) Break down: while heap has 2+, pop two, add, push back sum.
5) Pseudocode: write it above your code as comments.
6) Write code (use heapq).
7) Debug: test with small lists and print states.
8) Optimize: confirm O(n log n) with heapify + pops/pushes.
"""

def min_cost_connect(lengths):
    # TODO: implement using a min-heap (heapq)
    # raise NotImplementedError to show failing tests until implemented
    raise NotImplementedError


if __name__ == "__main__":
    # Optional manual check
    sample = [8, 4, 6, 12]
    # print(min_cost_connect(sample))
    pass
