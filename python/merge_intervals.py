"""
Merge Intervals

Given a list of intervals where each interval is [start, end],
merge all overlapping intervals and return a list of non-overlapping intervals.

Two intervals overlap if the next interval starts before or at the end
of the current interval.

Example:
[1, 3] and [2, 6] overlap because 2 <= 3
Merged result: [1, 6]

Input:
intervals = [[1,3],[2,6],[8,10],[15,18]]

Output:
[[1,6],[8,10],[15,18]]

Explanation:
[1,3] and [2,6] overlap, so merge them into [1,6].
[8,10] and [15,18] do not overlap with anything.


Input:
intervals = [[1,4],[4,5]]

Output:
[[1,5]]

Explanation:
Touching intervals count as overlapping because 4 <= 4.


Input:
intervals = [[1,4],[2,3]]

Output:
[[1,4]]

Explanation:
[2,3] is fully contained inside [1,4].


Input:
intervals = [[1,4],[0,2],[3,5]]

Output:
[[0,5]]

Explanation:
After sorting by start:
[[0,2],[1,4],[3,5]]
All overlap into [0,5].


Input:
intervals = [[1,2],[3,4],[5,6]]

Output:
[[1,2],[3,4],[5,6]]

Explanation:
No intervals overlap.


Constraints:
- intervals is a list of [start, end] pairs
- start <= end
- intervals may be unsorted
- assume intervals has at least one interval unless clarified otherwise

Expected approach:
1. Sort intervals by start.
2. Keep a result list.
3. For each interval:
   - If result is empty, add it.
   - Else compare current start to last merged end.
   - If overlapping, update last merged end.
   - Else append current interval.

Target:
Time: O(n log n) because sorting dominates
Space: O(n) for output
"""

from dataclasses import dataclass

@dataclass
class Interval:
    start: int
    end: int

    def print(self):
        print(f"[{self.start}, {self.end}]")

def test_merge_intervals():
    tests = [
        (
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]],
        ),
        (
            [[1, 4], [4, 5]],
            [[1, 5]],
        ),
        (
            [[1, 4], [2, 3]],
            [[1, 4]],
        ),
        (
            [[1, 4], [0, 2], [3, 5]],
            [[0, 5]],
        ),
        (
            [[1, 2], [3, 4], [5, 6]],
            [[1, 2], [3, 4], [5, 6]],
        ),
        (
            [[1, 10]],
            [[1, 10]],
        ),
        (
            [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]],
            [[1, 10]],
        ),
    ]

    for intervals, expected in tests:
        result = merge_intervals(intervals)
        assert result == expected, f"FAILED: {intervals} -> {result}, expected {expected}"

    print("all tests passed")


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    interval_dcs = [Interval(i[0], i[1]) for i in intervals]
    interval_dcs.sort(key=lambda i: (i.start, i.end))

    merged: list[Interval] = []
    last_append: Interval | None = None
    for iv in interval_dcs:
        if len(merged) == 0:
            merged = [iv]
            last_append = iv
            continue
        else:
            assert last_append is not None, f"last_append should not be None! there should be a valid one from initializing merged list" 
            if iv.start > last_append.end:
                merged.append(iv)
                last_append = iv
            if iv.end > last_append.end:
                last_append.end = iv.end

    return [[i.start, i.end] for i in merged]

if __name__ == "__main__":
    test_merge_intervals()