'''
APP Assignment 
'''


'''
Q1. Single Number

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one. Linear runtime, constant extra space.

Example: `[2,2,1]` -> `1`, `[4,1,2,1,2]` -> `4`, `[1]` -> `1`
'''

print('\n===== Q1. Single Number =====')
def single_number(nums):
    result = 0
    for x in nums:
        result ^= x
    return result

print(single_number([2, 2, 1]))
print(single_number([4, 1, 2, 1, 2]))
print(single_number([1]))


'''
Q2. Find Palindromes in a Given Range

Given `m` and `n` (0 <= m <= n <= 10^6), return all palindromic numbers in the range [m, n].

Example: `m=10, n=50` -> `[11, 22, 33, 44]`
'''

print('\n===== Q2. Find Palindromes in a Given Range =====')
def palindromes_in_range(m, n):
    return [i for i in range(m, n + 1) if str(i) == str(i)[::-1]]

print(palindromes_in_range(10, 50))
print(palindromes_in_range(100, 150))
print(palindromes_in_range(1, 9))


'''
Q3. Regular Expression Matching

Implement regular expression matching with `.` (any single character) and `*` (zero or more of the preceding element). The match must cover the entire string.

Example: `s="abcd", p=".*"` -> `true`; `s="mississippi", p="misisp*."` -> `false`; `s="aa", p="a"` -> `false`
'''

print('\n===== Q3. Regular Expression Matching =====')
def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (p[j - 2] in (s[i - 1], '.') and dp[i - 1][j])
            else:
                dp[i][j] = p[j - 1] in (s[i - 1], '.') and dp[i - 1][j - 1]
    return dp[m][n]

print(is_match("abcd", ".*"))
print(is_match("mississippi", "misisp*."))
print(is_match("aa", "a"))


'''
Q4. Decode Ways with Pattern Generation

Digits string `s` is decoded with 1->A ... 26->Z. Print the total number of ways to decode it and all decoded strings. No segment may start with '0'.

Example: `"226"` -> Total Ways: 3, Decoded Strings: BBF, BZ, VF
'''

print('\n===== Q4. Decode Ways with Pattern Generation =====')
def decode_ways(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        if i > 1 and 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]
    results = []
    def backtrack(i, current):
        if i == n:
            results.append(current)
            return
        if s[i] == '0':
            return
        backtrack(i + 1, current + chr(64 + int(s[i])))
        if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
            backtrack(i + 2, current + chr(64 + int(s[i:i + 2])))
    backtrack(0, "")
    return dp[n], sorted(results)

for s in ["12", "226", "11106", "06"]:
    total, strings = decode_ways(s)
    print("Input:", s)
    print("Total Ways:", total)
    print("Decoded Strings:")
    if strings:
        for x in strings:
            print(x)
    else:
        print("None")
    print()


'''
Q5. Balanced Binary Tree

Given a binary tree (level-order list), determine if it is height-balanced.

Example: `[3,9,20,null,null,15,7]` -> `true`; `[1,2,2,3,3,null,null,4,4]` -> `false`; `[4]` -> `true`
'''

print('\n===== Q5. Balanced Binary Tree =====')
def build_tree(arr):
    if not arr or arr[0] is None:
        return None
    nodes = [[v, None, None] if v is not None else None for v in arr]
    kids = iter(nodes[1:])
    queue = [nodes[0]]
    for node in queue:
        for side in (1, 2):
            child = next(kids, None)
            if child is not None:
                node[side] = child
                queue.append(child)
    return nodes[0]

def is_balanced(root):
    def height(node):
        if node is None:
            return 0
        left = height(node[1])
        right = height(node[2])
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    return height(root) != -1

print(is_balanced(build_tree([3, 9, 20, None, None, 15, 7])))
print(is_balanced(build_tree([1, 2, 2, 3, 3, None, None, 4, 4])))
print(is_balanced(build_tree([4])))


'''
Q6. Reverse Integer

Reverse the digits of a signed 32-bit integer `x`. If the result is outside [-2^31, 2^31 - 1] return 0. Do not use 64-bit storage.

Example: `123` -> `321`, `-123` -> `-321`, `120` -> `21`
'''

print('\n===== Q6. Reverse Integer =====')
def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    limit = 2**31 // 10
    last = 7 if sign == 1 else 8
    rev = 0
    while x:
        digit = x % 10
        x //= 10
        if rev > limit or (rev == limit and digit > last):
            return 0
        rev = rev * 10 + digit
    return sign * rev

print(reverse_integer(123))
print(reverse_integer(-123))
print(reverse_integer(120))
print(reverse_integer(1534236469))


'''
Q7. Minimize Maximum Consecutive Zeros with Construction

Given `L` (length) and `K` (number of ones), generate all binary strings of length L with exactly K ones, print each one's longest zero block, then print the optimal string(s) and the minimum longest zero block.

Example: `4 2` -> optimal `1010, 0110, 0101`, minimum = 1
'''

print('\n===== Q7. Minimize Maximum Consecutive Zeros with Construction =====')
from itertools import combinations

def max_zero_block(s):
    return max(len(part) for part in s.split('1'))

def solve(L, K):
    strings = []
    for positions in combinations(range(L), K):
        chars = ['0'] * L
        for p in positions:
            chars[p] = '1'
        strings.append(''.join(chars))
    strings.sort(reverse=True)
    values = {s: max_zero_block(s) for s in strings}
    best = min(values.values())
    print("Possible Strings:")
    for s in strings:
        print(f"{s} → max zeros = {values[s]}")
    print("Optimal Arrangement(s):", ", ".join(s for s in strings if values[s] == best))
    print("Minimum Longest Zero Block:", best)

for L, K in [(4, 2), (5, 0), (5, 5)]:
    print("Input:", L, K)
    solve(L, K)
    print()


'''
Q8. Merge Triplets to Form Target Triplet

Given `triplets` and a `target = [x, y, z]`, you may repeatedly merge two triplets using element-wise max. Return true if `target` can be obtained.

Example: `triplets=[[2,5,3],[1,8,4],[1,7,5]], target=[2,7,5]` -> `true`
'''

print('\n===== Q8. Merge Triplets to Form Target Triplet =====')
def merge_triplets(triplets, target):
    found = [False] * 3
    for t in triplets:
        if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
            for i in range(3):
                if t[i] == target[i]:
                    found[i] = True
    return all(found)

print(merge_triplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]))
print(merge_triplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]))
print(merge_triplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]))


'''
Q9. Palindromic Substrings with Pattern Listing

Count all palindromic substrings of `s` (duplicates at different positions counted separately) and print them.

Example: `"ababa"` -> Total Count: 9; a b a b a aba bab aba ababa
'''

print('\n===== Q9. Palindromic Substrings with Pattern Listing =====')
def palindromic_substrings(s):
    n = len(s)
    found = []
    for center in range(2 * n - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < n and s[left] == s[right]:
            found.append((right - left + 1, left, s[left:right + 1]))
            left -= 1
            right += 1
    found.sort()
    return [item[2] for item in found]

for s in ["ababa", "racecar", "level"]:
    result = palindromic_substrings(s)
    print("Input:", s)
    print("Total Count:", len(result))
    print("Palindromic Substrings:")
    for p in result:
        print(p)
    print()


'''
Q10. Kth Smallest Element in a BST

Given the root of a BST (level-order list) and `k`, return the kth smallest value (1-indexed).

Example: `[5,3,6,2,4,null,null,1], k=3` -> `3`
'''

print('\n===== Q10. Kth Smallest Element in a BST =====')
def build_tree(arr):
    if not arr or arr[0] is None:
        return None
    nodes = [[v, None, None] if v is not None else None for v in arr]
    kids = iter(nodes[1:])
    queue = [nodes[0]]
    for node in queue:
        for side in (1, 2):
            child = next(kids, None)
            if child is not None:
                node[side] = child
                queue.append(child)
    return nodes[0]

def kth_smallest(root, k):
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node[1]
        node = stack.pop()
        k -= 1
        if k == 0:
            return node[0]
        node = node[2]

print("5th smallest element =", kth_smallest(build_tree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]), 5))
print(kth_smallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3))


'''
Q11. Missing Number

Given an array `nums` of `n` distinct numbers in the range [0, n], return the missing number.

Example: `[3,0,1]` -> `2`, `[0,1]` -> `2`, `[9,6,4,2,3,5,7,0,1]` -> `8`
'''

print('\n===== Q11. Missing Number =====')
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

print(missing_number([3, 0, 1]))
print(missing_number([0, 1]))
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))


'''
Q12. Coin Change

Return the fewest number of coins needed to make `amount`, or -1 if impossible. Infinite supply of each coin.

Example: `coins=[1,2,5], amount=11` -> `3`; `coins=[2], amount=3` -> `-1`; `coins=[1], amount=0` -> `0`
'''

print('\n===== Q12. Coin Change =====')
def coin_change(coins, amount):
    INF = amount + 1
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount] if dp[amount] != INF else -1

print(coin_change([1, 2, 5], 11))
print(coin_change([2], 3))
print(coin_change([1], 0))


'''
Q13. Cheapest Flights Within K Stops

Given `n` cities and `flights[i] = [from, to, price]`, return the cheapest price from `src` to `dst` with at most `k` stops, or -1.

Example: `n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src=0, dst=3, k=1` -> `700`
'''

print('\n===== Q13. Cheapest Flights Within K Stops =====')
def cheapest_flight(n, flights, src, dst, k):
    INF = float('inf')
    dist = [INF] * n
    dist[src] = 0
    for _ in range(k + 1):
        new_dist = dist[:]
        for u, v, w in flights:
            if dist[u] + w < new_dist[v]:
                new_dist[v] = dist[u] + w
        dist = new_dist
    return -1 if dist[dst] == INF else dist[dst]

print(cheapest_flight(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))
print(cheapest_flight(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
print(cheapest_flight(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))


'''
Q14. Merge k Sorted Lists

Merge `k` sorted linked lists into one sorted linked list.

Example: `[[1,4,5],[1,3,4],[2,6]]` -> `[1,1,2,3,4,4,5,6]`
'''

print('\n===== Q14. Merge k Sorted Lists =====')
import heapq

def build_list(arr):
    head = None
    for v in reversed(arr):
        head = [v, head]
    return head

def to_array(head):
    out = []
    while head:
        out.append(head[0])
        head = head[1]
    return out

def merge_k_lists(lists):
    heap = [(node[0], i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)
    dummy = [0, None]
    tail = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        tail[1] = node
        tail = node
        if node[1]:
            heapq.heappush(heap, (node[1][0], i, node[1]))
    return dummy[1]

print(to_array(merge_k_lists([build_list(x) for x in [[1, 4, 5], [1, 3, 4], [2, 6]]])))
print(to_array(merge_k_lists([build_list(x) for x in [[4, 5], [1, 6]]])))


'''
Q15. Reverse Bits

Reverse the bits of a given 32-bit integer.

Example: `43261596` -> `964176192`; `2147483644` -> `1073741822`
'''

print('\n===== Q15. Reverse Bits =====')
def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

print(reverse_bits(43261596))
print(reverse_bits(2147483644))


'''
Q16. Separate Letters and Numbers from a String

Return `[letters, digits]` extracted from the string in order of appearance.

Example: `"a1b2c3d4"` -> `["abcd", "1234"]`
'''

print('\n===== Q16. Separate Letters and Numbers from a String =====')
def separate(s):
    letters = ''.join(c for c in s if c.isalpha())
    digits = ''.join(c for c in s if c.isdigit())
    return [letters, digits]

print(separate("a1b2c3d4"))
print(separate("x9y8z7"))
print(separate("12345"))
print(separate("abcdef"))


'''
Q17. Merge Intervals

Merge all overlapping intervals and return the non-overlapping intervals.

Example: `[[1,3],[2,6],[8,10],[15,18]]` -> `[[1,6],[8,10],[15,18]]`
'''

print('\n===== Q17. Merge Intervals =====')
def merge_intervals(intervals):
    intervals = sorted(intervals)
    merged = [intervals[0][:]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge_intervals([[1, 4], [4, 5]]))
print(merge_intervals([[4, 7], [1, 4]]))


'''
Q18. Maximum Product Subarray

Find the contiguous subarray with the largest product and return the product.

Example: `[2,3,-2,4]` -> `6`; `[-2,0,-1]` -> `0`
'''

print('\n===== Q18. Maximum Product Subarray =====')
def max_product(nums):
    cur_max = cur_min = best = nums[0]
    for x in nums[1:]:
        candidates = (x, cur_max * x, cur_min * x)
        cur_max = max(candidates)
        cur_min = min(candidates)
        best = max(best, cur_max)
    return best

print(max_product([2, 3, -2, 4]))
print(max_product([-2, 0, -1]))


'''
Q19. Minimum Team Selection to Cover Required Skills

Given required skills and `N` candidates (each with a subset of skills), select the smallest team that covers all required skills and print their indices.

Example: skills `Python SQL MachineLearning DataStructures`, candidates `0:Python SQL, 1:SQL MachineLearning, 2:MachineLearning DataStructures, 3:DataStructures` -> `0 2`
'''

print('\n===== Q19. Minimum Team Selection to Cover Required Skills =====')
def min_team(required, candidates):
    index = {skill: i for i, skill in enumerate(required)}
    full = (1 << len(required)) - 1
    masks = []
    for skills in candidates:
        mask = 0
        for s in skills:
            if s in index:
                mask |= 1 << index[s]
        masks.append(mask)
    dp = {0: []}
    for i, m in enumerate(masks):
        if m == 0:
            continue
        for mask, team in list(dp.items()):
            new_mask = mask | m
            if new_mask not in dp or len(dp[new_mask]) > len(team) + 1:
                dp[new_mask] = team + [i]
    return dp[full]

tests = [
    ("Python SQL MachineLearning DataStructures", ["Python SQL", "SQL MachineLearning", "MachineLearning DataStructures", "DataStructures"]),
    ("Java Python SQL", ["Java", "Python SQL", "SQL"]),
    ("C++ Python DataStructures", ["C++", "Python", "DataStructures", "C++ Python DataStructures"]),
]
for skills, people in tests:
    print(*min_team(skills.split(), [p.split() for p in people]))


'''
Q20. Word Break with All Segmentations

Determine whether `s` can be segmented into dictionary words (words reusable) and print all valid segmentations.

Example: `s="catsanddog", wordDict=["cat","cats","and","sand","dog"]` -> `cats and dog`, `cat sand dog`
'''

print('\n===== Q20. Word Break with All Segmentations =====')
from functools import lru_cache

def word_break(s, word_dict):
    words = set(word_dict)
    max_len = max(len(w) for w in words)

    @lru_cache(None)
    def segments(i):
        if i == len(s):
            return [[]]
        out = []
        for j in range(i + 1, min(len(s), i + max_len) + 1):
            if s[i:j] in words:
                for rest in segments(j):
                    out.append([s[i:j]] + rest)
        return out

    return sorted((' '.join(x) for x in segments(0)), reverse=True)

tests = [
    ("AmritaMysuru", ["Amrita", "Rita", "Mysuru"]),
    ("applepenapple", ["apple", "pen"]),
    ("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
]
for s, d in tests:
    result = word_break(s, d)
    print("Input:", s)
    print("Can Segment:", bool(result))
    print("Segmentations:")
    if result:
        for r in result:
            print(r)
    else:
        print("None")
    print()


'''
Q21. Number of 1 Bits

Return the number of set bits (Hamming weight) of a positive integer `n`.

Example: `11` -> `3`, `128` -> `1`, `2147483645` -> `30`
'''

print('\n===== Q21. Number of 1 Bits =====')
def hamming_weight(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

print(hamming_weight(11))
print(hamming_weight(128))
print(hamming_weight(2147483645))


'''
Q22. Midpoint of Line Segment

Given endpoints (x1, y1) and (x2, y2), return the midpoint (mx, my).

Example: `(0,0), (4,4)` -> `(2,2)`; `(-2,4), (2,0)` -> `(0,2)`
'''

print('\n===== Q22. Midpoint of Line Segment =====')
def midpoint(p1, p2):
    mx = (p1[0] + p2[0]) / 2
    my = (p1[1] + p2[1]) / 2
    fmt = lambda v: int(v) if v == int(v) else v
    return (fmt(mx), fmt(my))

print(midpoint((0, 0), (4, 4)))
print(midpoint((1, 3), (5, 7)))
print(midpoint((-2, 4), (2, 0)))


'''
Q23. Sum of Cubes in a Given Range

Compute a^3 + (a+1)^3 + ... + b^3 for 1 <= a <= b <= 10^5.

Example: `4 9` -> `1989`; `1 3` -> `36`; `5 5` -> `125`
'''

print('\n===== Q23. Sum of Cubes in a Given Range =====')
def sum_of_cubes(a, b):
    total = lambda n: (n * (n + 1) // 2) ** 2
    return total(b) - total(a - 1)

print(sum_of_cubes(4, 9))
print(sum_of_cubes(1, 3))
print(sum_of_cubes(5, 5))


'''
Q24. Closest Pair of Points

Given `n` points in 2D, return the minimum Euclidean distance between any two distinct points.

Example: `[(0,0),(1,1)]` -> `√2`; `[(0,0),(3,4),(6,8)]` -> `5`
'''

print('\n===== Q24. Closest Pair of Points =====')
import math

def closest_pair_squared(points):
    px = sorted(points)
    def d2(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    def rec(lo, hi):
        n = hi - lo
        if n <= 3:
            best = float('inf')
            for i in range(lo, hi):
                for j in range(i + 1, hi):
                    best = min(best, d2(px[i], px[j]))
            return best
        mid = (lo + hi) // 2
        mid_x = px[mid][0]
        d = min(rec(lo, mid), rec(mid, hi))
        strip = [p for p in px[lo:hi] if (p[0] - mid_x) ** 2 < d]
        strip.sort(key=lambda p: p[1])
        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if (strip[j][1] - strip[i][1]) ** 2 >= d:
                    break
                d = min(d, d2(strip[i], strip[j]))
        return d
    return rec(0, len(px))

def show(points):
    d = closest_pair_squared(points)
    root = math.isqrt(d)
    print(root if root * root == d else f"√{d}")

show([(0, 0), (1, 1)])
show([(1, 1), (2, 2), (5, 5)])
show([(0, 0), (3, 4), (6, 8)])


'''
Q25. Count Trailing Zeros in Binary

Count the zeros from the rightmost side of the binary representation of `n` until the first `1`.

Example: `8` (1000) -> `3`; `12` (1100) -> `2`
'''

print('\n===== Q25. Count Trailing Zeros in Binary =====')
def trailing_zeros(n):
    return (n & -n).bit_length() - 1

print(trailing_zeros(8))
print(trailing_zeros(12))


'''
Q26. Sum of Unique Elements

Find the sum of elements that appear exactly once in the array and print those elements.

Example: `[1,3,2,3,2,4]` -> Unique Elements: 1 4, Sum: 5
'''

print('\n===== Q26. Sum of Unique Elements =====')
from collections import Counter

def sum_unique(arr):
    counts = Counter(arr)
    unique = [x for x in arr if counts[x] == 1]
    print("Unique Elements:", *unique if unique else ["None"])
    print("Sum:", sum(unique))

sum_unique([1, 3, 2, 3, 2, 4])
sum_unique([10, 20, 10, 30, 40, 30])
sum_unique([5, 5, 5, 5])


'''
Q27. Invert Binary Tree

Invert a binary tree and return its root.

Example: `[4,2,7,1,3,6,9]` -> `[4,7,2,9,6,3,1]`; `[2,1,3]` -> `[2,3,1]`
'''

print('\n===== Q27. Invert Binary Tree =====')
def build_tree(arr):
    if not arr or arr[0] is None:
        return None
    nodes = [[v, None, None] if v is not None else None for v in arr]
    kids = iter(nodes[1:])
    queue = [nodes[0]]
    for node in queue:
        for side in (1, 2):
            child = next(kids, None)
            if child is not None:
                node[side] = child
                queue.append(child)
    return nodes[0]

def to_list(root):
    result = []
    queue = [root]
    for node in queue:
        if node is None:
            result.append(None)
            continue
        result.append(node[0])
        queue.append(node[1])
        queue.append(node[2])
    while result and result[-1] is None:
        result.pop()
    return result

def invert(node):
    if node:
        node[1], node[2] = invert(node[2]), invert(node[1])
    return node

print(to_list(invert(build_tree([4, 2, 7, 1, 3, 6, 9]))))
print(to_list(invert(build_tree([2, 1, 3]))))


'''
Q28. Valid Anagram

Determine whether `t` is an anagram of `s`.

Example: `s="anagram", t="nagaram"` -> `true`; `s="rat", t="car"` -> `false`
'''

print('\n===== Q28. Valid Anagram =====')
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)

print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram("listen", "silent"))


'''
Q29. Happy Number

Replace a number by the sum of squares of its digits repeatedly. If it reaches 1 it is happy; if it loops forever it is not.

Example: `19` -> `true`; `2` -> `false`
'''

print('\n===== Q29. Happy Number =====')
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1

print(is_happy(19))
print(is_happy(2))


'''
Q30. Set Matrix Zeroes

If an element of an m x n matrix is 0, set its entire row and column to 0, in place.

Example: `[[1,1,1],[1,0,1],[1,1,1]]` -> `[[1,0,1],[0,0,0],[1,0,1]]`
'''

print('\n===== Q30. Set Matrix Zeroes =====')
def set_zeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row = any(matrix[0][j] == 0 for j in range(n))
    first_col = any(matrix[i][0] == 0 for i in range(m))
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if first_row:
        for j in range(n):
            matrix[0][j] = 0
    if first_col:
        for i in range(m):
            matrix[i][0] = 0
    return matrix

print(set_zeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(set_zeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))


'''
Q31. Card Probabilities

Given drawn cards, compute P(Ace), P(Face card), P(Red), the most frequent category among these three, and P(Black).

Example: `["AH","10D","KC","QS","2H","JD","7C","KH"]` -> P(Ace)=0.125 P(Face)=0.50 P(Red)=0.50, Most Frequent: Face, P(Black)=0.50
'''

print('\n===== Q31. Card Probabilities =====')
def card_probabilities(cards):
    total = len(cards)
    counts = {
        "Ace": sum(1 for c in cards if c[:-1] == "A"),
        "Face": sum(1 for c in cards if c[:-1] in ("J", "Q", "K")),
        "Red": sum(1 for c in cards if c[-1] in ("H", "D")),
    }
    black = sum(1 for c in cards if c[-1] in ("S", "C"))
    print(f"P(Ace)={counts['Ace'] / total:.3f} P(Face)={counts['Face'] / total:.3f} P(Red)={counts['Red'] / total:.3f}")
    print("Most Frequent Category:", max(counts, key=counts.get))
    print(f"P(Black)={black / total:.3f}")

card_probabilities(["AH", "10D", "KC", "QS", "2H", "JD", "7C", "KH"])


'''
Q32. Toggle K-th Bit

Toggle the k-th bit of `n` using XOR.

Example: `n=5, k=1` -> `7`; `n=4, k=2` -> `0`
'''

print('\n===== Q32. Toggle K-th Bit =====')
def toggle_bit(n, k):
    return n ^ (1 << k)

print(toggle_bit(5, 1))
print(toggle_bit(4, 2))


'''
Q33. Plus One

Increment a large integer represented as a digit array by one.

Example: `[1,2,3]` -> `[1,2,4]`; `[9]` -> `[1,0]`
'''

print('\n===== Q33. Plus One =====')
def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

print(plus_one([1, 2, 3]))
print(plus_one([4, 3, 2, 1]))
print(plus_one([9]))


'''
Q34. String Transformation with Given Substring

Replace each character of substring `sub` inside `s` with its previous letter in the alphabet ('a' wraps to 'z') and return the resulting string.

Example: `s="hackerrank", sub="hack"` -> `gzbjerrank`
'''

print('\n===== Q34. String Transformation with Given Substring =====')
def transform(s, sub):
    start = s.find(sub)
    changed = ''.join(chr((ord(c) - 97 - 1) % 26 + 97) for c in sub)
    return s[:start] + changed + s[start + len(sub):]

print(transform("hackerrank", "hack"))
print(transform("programming", "gram"))
print(transform("apple", "a"))


'''
Q35. Trapping Rain Water

Given bar heights (width 1), compute the total water trapped after raining.

Example: `[0,1,0,2,1,0,1,3,2,1,2,1]` -> `6`; `[4,2,0,3,2,5]` -> `9`
'''

print('\n===== Q35. Trapping Rain Water =====')
def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water

print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap([4, 2, 0, 3, 2, 5]))


'''
Q36. Generate Parentheses

Given `n` pairs of parentheses, generate all combinations of well-formed parentheses.

Example: `n=3` -> `["((()))","(()())","(())()","()(())","()()()"]`
'''

print('\n===== Q36. Generate Parentheses =====')
def generate_parentheses(n):
    result = []
    def backtrack(current, opened, closed):
        if len(current) == 2 * n:
            result.append(current)
            return
        if opened < n:
            backtrack(current + "(", opened + 1, closed)
        if closed < opened:
            backtrack(current + ")", opened, closed + 1)
    backtrack("", 0, 0)
    return result

print(generate_parentheses(3))
print(generate_parentheses(1))


'''
Q37. Spiral Matrix

Return all elements of an m x n matrix in spiral order.

Example: `[[1,2,3],[4,5,6],[7,8,9]]` -> `[1,2,3,6,9,8,7,4,5]`
'''

print('\n===== Q37. Spiral Matrix =====')
def spiral_order(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))


'''
Q38. Container With Most Water

Given line heights, find two lines that with the x-axis hold the most water. Area = (right - left) x min(height[left], height[right]).

Example: `[1,8,6,2,5,4,8,3,7]` -> `49`; `[1,1]` -> `1`; `[4,3,2,1,4]` -> `16`
'''

print('\n===== Q38. Container With Most Water =====')
def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        best = max(best, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best

print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_area([1, 1]))
print(max_area([4, 3, 2, 1, 4]))


'''
Q39. Matrix Chain Multiplication

Given dimensions `p` where matrix Ai is p[i-1] x p[i], return the minimum number of scalar multiplications, the optimal parenthesization and the step-by-step multiplication sequence.

Example: `[10,30,5,60]` -> Minimum Cost: 4500, `((A1 × A2) × A3)`
'''

print('\n===== Q39. Matrix Chain Multiplication =====')
def matrix_chain(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k
    steps = []
    def build(i, j):
        if i == j:
            return f"A{i}"
        k = split[i][j]
        left = build(i, k)
        right = build(k + 1, j)
        expr = f"({left} × {right})"
        cost = p[i - 1] * p[k] * p[j]
        steps.append(f"{expr} → cost = {p[i - 1]}×{p[k]}×{p[j]} = {cost}")
        return expr
    order = build(1, n)
    return dp[1][n], order, steps

for dims in [[10, 30, 5, 60], [40, 20, 30, 10, 30]]:
    cost, order, steps = matrix_chain(dims)
    print("Dimensions:", dims)
    print("Minimum Cost:", cost)
    print("Optimal Parenthesization:", order)
    print("Multiplication Sequence:")
    for i, s in enumerate(steps, 1):
        print(f"Step {i}: {s}")
    print("Total Cost:", cost)
    print()


'''
Q40. Validate and Complete a 9×9 Sudoku Board

Validate a partially filled Sudoku board; if valid, fill all empty cells and print the completed board in table format. If invalid, return false and the reason.
'''

print('\n===== Q40. Validate and Complete a 9×9 Sudoku Board =====')
def validate(board):
    reasons = []
    for i in range(9):
        row = [c for c in board[i] if c != '.']
        if len(row) != len(set(row)):
            reasons.append(f"Duplicate found in row {i + 1}")
        col = [board[r][i] for r in range(9) if board[r][i] != '.']
        if len(col) != len(set(col)):
            reasons.append(f"Duplicate found in column {i + 1}")
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            box = [board[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3) if board[r][c] != '.']
            if len(box) != len(set(box)):
                reasons.append(f"Duplicate found in 3×3 sub-grid starting at row {br + 1}, column {bc + 1}")
    return reasons

def can_place(board, r, c, d):
    for i in range(9):
        if board[r][i] == d or board[i][c] == d:
            return False
    br, bc = r // 3 * 3, c // 3 * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if board[i][j] == d:
                return False
    return True

def solve(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                for d in "123456789":
                    if can_place(board, r, c, d):
                        board[r][c] = d
                        if solve(board):
                            return True
                        board[r][c] = '.'
                return False
    return True

def print_board(board):
    for i, row in enumerate(board):
        if i in (3, 6):
            print("-" * 27)
        print(" | ".join(" ".join(row[j:j + 3]) for j in range(0, 9, 3)))

def process(rows):
    board = [list(r) for r in rows]
    reasons = validate(board)
    if reasons:
        print("Valid Sudoku: false")
        for r in reasons:
            print("Reason:", r)
        return
    print("Valid Sudoku: true")
    solve(board)
    print("Completed Sudoku:")
    print_board(board)

valid_rows = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
invalid_rows = ["83..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
process(valid_rows)
print()
process(invalid_rows)


'''
Q41. Find All Words in Grid

Given a character grid and a list of words, return all words that can be formed by moving up/down/left/right without reusing a cell. Use Trie + DFS backtracking.

Example: board `oaan/etae/ihkr/iflv`, words `["oath","pea","eat","rain"]` -> `["eat","oath"]`
'''

print('\n===== Q41. Find All Words in Grid =====')
def find_words(board, words):
    trie = {}
    for w in words:
        node = trie
        for ch in w:
            node = node.setdefault(ch, {})
        node['$'] = w
    m, n = len(board), len(board[0])
    found = []
    def dfs(r, c, parent):
        ch = board[r][c]
        node = parent[ch]
        if '$' in node:
            found.append(node.pop('$'))
        board[r][c] = '@'
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in node:
                dfs(nr, nc, node)
        board[r][c] = ch
        if not node:
            parent.pop(ch)
    for r in range(m):
        for c in range(n):
            if board[r][c] in trie:
                dfs(r, c, trie)
    return sorted(found)

board1 = [list("oaan"), list("etae"), list("ihkr"), list("iflv")]
print(find_words(board1, ["oath", "pea", "eat", "rain"]))
board2 = [list("ab"), list("cd")]
print(find_words(board2, ["abcb"]))


'''
Q42. House Robber

Given the money in each house, return the maximum amount you can rob without robbing two adjacent houses.

Example: `[1,2,3,1]` -> `4`; `[2,7,9,3,1]` -> `12`
'''

print('\n===== Q42. House Robber =====')
def rob(nums):
    take, skip = 0, 0
    for x in nums:
        take, skip = skip + x, max(take, skip)
    return max(take, skip)

print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))


'''
Q43. Find Euler Path

For an undirected graph, check whether an Euler Path exists and print node degrees, odd-degree nodes, start node and the Euler path.

Example: `n=4, edges=[[0,1],[1,2],[2,0],[1,3]]` -> Exists: true, Odd nodes [1, 3], Path: 1 → 0 → 2 → 1 → 3
'''

print('\n===== Q43. Find Euler Path =====')
from collections import deque

def euler_path(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    for a in adj:
        a.sort()
    degree = [len(a) for a in adj]
    odd = [i for i in range(n) if degree[i] % 2 == 1]
    non_zero = [i for i in range(n) if degree[i] > 0]

    connected = True
    if non_zero:
        seen = {non_zero[0]}
        queue = deque([non_zero[0]])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    queue.append(v)
        connected = all(v in seen for v in non_zero)

    exists = connected and len(odd) in (0, 2)
    print("Euler Path Exists:", str(exists).lower())
    print("Node Degrees:")
    for i in range(n):
        print(f"{i} → {degree[i]}")
    print("Odd Degree Nodes:", odd)

    if not exists:
        reasons = []
        if len(odd) not in (0, 2):
            reasons.append("More than 2 nodes have odd degree")
        if not connected:
            reasons.append("graph is disconnected")
        print("Reason:", " and ".join(reasons))
        return

    start = odd[0] if odd else (non_zero[0] if non_zero else 0)
    graph = [a[:] for a in adj]
    stack = [start]
    circuit = []
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v].pop(0)
            graph[u].remove(v)
            stack.append(u)
        else:
            circuit.append(stack.pop())
    circuit.reverse()
    print("Start Node:", start)
    print("Euler Path:", " → ".join(map(str, circuit)))

euler_path(4, [[0, 1], [1, 2], [2, 0], [1, 3]])
print()
euler_path(4, [[0, 1], [1, 2], [2, 3]])
print()
euler_path(4, [[0, 1], [2, 3]])


'''
Q44. Rotate Image

Rotate an n x n matrix by 90 degrees clockwise, in place.

Example: `[[1,2,3],[4,5,6],[7,8,9]]` -> `[[7,4,1],[8,5,2],[9,6,3]]`
'''

print('\n===== Q44. Rotate Image =====')
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))


'''
Q45. Climbing Stairs with Patterns

Climb `n` steps taking 1 or 2 steps at a time. Print the total number of distinct ways and all step patterns.

Example: `n=3` -> Total Ways: 3; 1 + 1 + 1, 1 + 2, 2 + 1
'''

print('\n===== Q45. Climbing Stairs with Patterns =====')
def climb(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n + 1):
        ways[i] = ways[i - 1] + (ways[i - 2] if i > 1 else 0)
    return ways[n]

def patterns(n):
    if n == 0:
        return [[]]
    out = []
    for step in (1, 2):
        if step <= n:
            for rest in patterns(n - step):
                out.append([step] + rest)
    return out

for n in [2, 3, 4]:
    print("Input: n =", n)
    print("Total Ways:", climb(n))
    print("Patterns:")
    for p in patterns(n):
        print(" + ".join(map(str, p)))
    print()


'''
Q46. Filter Characters from a String

Remove all characters from `target` that are present in `reference`.

Example: `target="programming", reference="grm"` -> `"poain"`
'''

print('\n===== Q46. Filter Characters from a String =====')
def filter_characters(target, reference):
    remove = set(reference)
    return ''.join(c for c in target if c not in remove)

print(filter_characters("programming", "grm"))
print(filter_characters("hello world", "lo"))
print(filter_characters("abcdef", "xyz"))


'''
Q47. Sum of Odd Numbers in a List

Find the sum of all odd numbers in a list using: (1) a regular function parameter, (2) list comprehension, (3) a user-defined function.

Example: `[1,2,3,4,5,6]` -> `9`
'''

print('\n===== Q47. Sum of Odd Numbers in a List =====')
def sum_odd_regular(nums):
    total = 0
    for x in nums:
        if x % 2 != 0:
            total += x
    return total

def sum_odd_comprehension(nums):
    return sum([x for x in nums if x % 2 != 0])

def is_odd(x):
    return x % 2 != 0

def sum_odd_user_defined(nums):
    return sum(filter(is_odd, nums))

for nums in [[1, 2, 3, 4, 5, 6], [10, 15, 20, 25, 30, 35], [2, 4, 6, 8]]:
    print(sum_odd_regular(nums), sum_odd_comprehension(nums), sum_odd_user_defined(nums))


'''
Q48. Palindrome Number Using a Decorator Function

Check whether an integer is a palindrome using a decorator function that displays the result.

Example: `121` -> `121 is a Palindrome`; `1234` -> `1234 is Not a Palindrome`
'''

print('\n===== Q48. Palindrome Number Using a Decorator Function =====')
def display_result(func):
    def wrapper(num):
        result = func(num)
        if result:
            print(f"{num} is a Palindrome")
        else:
            print(f"{num} is Not a Palindrome")
        return result
    return wrapper

@display_result
def is_palindrome(num):
    return str(num) == str(num)[::-1]

is_palindrome(121)
is_palindrome(1234)


'''
Q49. Cumulative Average Using a Closure Function

Use a closure that keeps a list, appends each entered number, and displays the cumulative average after every insertion.

Example: inputs `10 20 30 40` -> 10.0, 15.0, 20.0, 25.0
'''

print('\n===== Q49. Cumulative Average Using a Closure Function =====')
def make_average():
    numbers = []
    def add(x):
        numbers.append(x)
        return sum(numbers) / len(numbers)
    return add

n = int(input("Enter n: "))
average = make_average()
for _ in range(n):
    value = int(input("Enter number: "))
    print("Cumulative Average:", average(value))


'''
Q50. Remove Elements Greater Than 20 Using Decorator and Filter

Remove all elements greater than 20 from `[5, 10, 23, 40, 8]` using a decorator function and `filter()`.

Output: `[5, 10, 8]`
'''

print('\n===== Q50. Remove Elements Greater Than 20 Using Decorator and Filter =====')
def show_lists(func):
    def wrapper(nums):
        print("Original list:", nums)
        result = func(nums)
        print("Filtered list:", result)
        return result
    return wrapper

@show_lists
def remove_greater_than_20(nums):
    return list(filter(lambda x: x <= 20, nums))

remove_greater_than_20([5, 10, 23, 40, 8])


'''
Q51. File and Directory Management Using os and time Modules

Create `My_Project/assignments/task1`, display the working directory (`getcwd`, `getcwdb`), create `sample.py`, check the directory with `isdir`, calculate total file size with `os.walk`, show access/modified times with `time.ctime`, and list the directory contents.
'''

print('\n===== Q51. File and Directory Management Using os and time Modules =====')
import os
import time

path = os.path.join("My_Project", "assignments", "task1")
os.makedirs(path, exist_ok=True)

print("Current Working Directory:", os.getcwd())
print("Byte String Format:", os.getcwdb())

file_path = os.path.join(path, "sample.py")
with open(file_path, "w") as f:
    f.write("print('Python Assignment')\n")

print(os.path.isdir(path))

total_size = 0
for root, dirs, files in os.walk("My_Project"):
    for name in files:
        total_size += os.path.getsize(os.path.join(root, name))
print("total_size:", total_size, "bytes")

print("access time:", time.ctime(os.path.getatime(file_path)))
print("Last modified time:", time.ctime(os.path.getmtime(file_path)))
print("list of files in the directory:", os.listdir(path))


'''
Q52. CSV Data Cleaning and JSON File Conversion

Clean a raw CSV employee dataset using `csv` and `json`: strip whitespace, skip records with missing age/salary or salary "Unknown", convert types with `int()` / `float()`, handle `ValueError`, and write `cleaned_data.json` with indent 2.
'''

print('\n===== Q52. CSV Data Cleaning and JSON File Conversion =====')
import csv
import json

raw_data = """Name,Age,Salary,Join Date
Alice, 30, 95000, 2015-03-01
Bob, , 60000, 2018-07-15
Charlie, 35, Unknown, 2024-02-01
Diana, 40, 110000, 2021-11-03"""

lines = raw_data.split('\n')
reader = csv.DictReader(lines)

cleaned_records = []
for row in reader:
    row = {k.strip(): (v or '').strip() for k, v in row.items()}
    if not row["Age"] or not row["Salary"] or row["Salary"].lower() == "unknown":
        continue
    try:
        age = int(row["Age"])
        salary = float(row["Salary"])
    except ValueError:
        continue
    cleaned_records.append({
        "name": row["Name"],
        "age": age,
        "salary": salary,
        "join_date": row["Join Date"],
    })

with open("cleaned_data.json", "w") as f:
    json.dump(cleaned_records, f, indent=2)

with open("cleaned_data.json") as f:
    print(f.read())


'''
Q53. Longest Substring Without Repeating Characters (Sliding Window)

Read a string and find the length of the longest substring without repeating characters using a sliding window and a Boolean visited array of size 26.

Example: `"abcabcbb"` -> 3; `"bbbbb"` -> 1; `"pwwkew"` -> 3
'''

print('\n===== Q53. Longest Substring Without Repeating Characters (Sliding Window) =====')
s = input("Enter a string: ")

visited = [False] * 26
left = 0
longest = 0
for right in range(len(s)):
    index = ord(s[right]) - ord('a')
    while visited[index]:
        visited[ord(s[left]) - ord('a')] = False
        left += 1
    visited[index] = True
    longest = max(longest, right - left + 1)

print("Length of the longest unique substring:", longest)


'''
Q54. Generator Function to Extract Vowels from a Name

Create a generator `getvowels()` that yields only the vowels (`aeiouAEIOU`) of a name, and display them with a for loop.

Example: `Priyanka` -> i, a, a
'''

print('\n===== Q54. Generator Function to Extract Vowels from a Name =====')
def getvowels(name):
    vowels = "aeiouAEIOU"
    for ch in name:
        if ch in vowels:
            yield ch

name = input("Enter name: ")
for v in getvowels(name):
    print(v)


'''
Q55. User-Defined Iterator for Decimal Values

Create a class `NumberIterator(start, stop, step)` implementing `__iter__()` and `__next__()` that generates 0.0 to 1.0 with step 0.25 and stops with `StopIteration`. (The question explicitly requires a class.)
'''

print('\n===== Q55. User-Defined Iterator for Decimal Values =====')
class NumberIterator:
    def __init__(self, start=0.0, stop=1.0, step=0.25):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

for value in NumberIterator(0.0, 1.0, 0.25):
    print(value)


'''
Q56. Move All Zeros to the End of a List

Move all zeros to the end while keeping the order of non-zero elements, using list comprehension.

Example: `[0,1,0,2,0,3]` -> `[1,2,3,0,0,0]`
'''

print('\n===== Q56. Move All Zeros to the End of a List =====')
def move_zeros(l):
    non_zero = [x for x in l if x != 0]
    zeros = [x for x in l if x == 0]
    return non_zero + zeros

print(move_zeros([0, 1, 0, 2, 0, 3]))
print(move_zeros([4, 0, 5, 0, 2, 0, 8]))


'''
Q57. Student Performance Analyzer

Given student marks, calculate each student's average, find the highest average, randomly select one student, display the current date, use `Counter` to classify grades and use `reduce()` to calculate total marks.
'''

print('\n===== Q57. Student Performance Analyzer =====')
import random
from collections import Counter
from datetime import date
from functools import reduce

students = {
    "Tarun": [82, 91, 78],
    "Karthik": [65, 72, 68],
    "Chadrika": [91, 95, 89],
    "Trisha": [76, 81, 79],
    "Atul": [88, 84, 92],
}

averages = {name: sum(marks) / len(marks) for name, marks in students.items()}
for name, avg in averages.items():
    print(f"{name}: {avg:.2f}")

top = max(averages, key=averages.get)
print("Highest Average:", top, f"({averages[top]:.2f})")

print("Randomly Selected Student:", random.choice(list(students)))
print("Current Date:", date.today())

def grade(avg):
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    return "D"

print("Grade Distribution:", dict(Counter(grade(a) for a in averages.values())))

total_marks = reduce(lambda acc, marks: acc + sum(marks), students.values(), 0)
print("Total Marks of All Students:", total_marks)


'''
Q58. Automated Course Project Team Allocation

Group 12 students by department (`defaultdict`), generate teams (`itertools.combinations`), randomly select one (`random.sample`), compute total marks (`functools.reduce`) and average (`math`), record the allocation date (`datetime`) and take the team size from the command line (`sys.argv`).
'''

print('\n===== Q58. Automated Course Project Team Allocation =====')
import sys
import math
import random
from collections import defaultdict
from itertools import combinations
from functools import reduce
from datetime import datetime

sys.argv = ["allocation.py", "3"]
team_size = int(sys.argv[1])

students = [
    ("Anita", "CSE", 85), ("Rahul", "CSE", 78), ("Priya", "CSE", 92),
    ("Kiran", "AI", 88), ("Meena", "AI", 76), ("Arjun", "AI", 91),
    ("Sneha", "Data Science", 82), ("Varun", "Data Science", 69), ("Divya", "Data Science", 95),
    ("Rohit", "Cyber Security", 73), ("Neha", "Cyber Security", 89), ("Sanjay", "Cyber Security", 80),
]

groups = defaultdict(list)
for name, dept, marks in students:
    groups[dept].append((name, marks))

print("===== PROJECT TEAM ALLOCATION =====")
print("Team Size:", team_size)
print("Allocation Date:", datetime.now().strftime("%d-%m-%Y"))

for dept, members in groups.items():
    print()
    print("Department:", dept)
    if len(members) < team_size:
        print("Not enough students to form a team")
        continue
    possible_teams = list(combinations(members, team_size))
    team = random.sample(possible_teams, 1)[0]
    total = reduce(lambda acc, member: acc + member[1], team, 0)
    average = math.fsum(m for _, m in team) / len(team)
    print("Selected Team:")
    for i, (name, marks) in enumerate(team, 1):
        print(f"{i}. {name} - {marks}")
    print("Total Marks:", total)
    print(f"Average Marks: {average:.2f}")


'''
Q59. Student Marks Management System

Accept student name and marks in a loop. Validate the name with `assert`, handle `ValueError` for non-numeric marks, raise a user-defined `InvalidMarksError` for marks outside 0-100, store valid records in `student_records.txt`, and use try/except/finally. (A custom exception requires a class definition.)
'''

print('\n===== Q59. Student Marks Management System =====')
class InvalidMarksError(Exception):
    pass

while True:
    try:
        name = input("Enter student name: ").strip()
        assert name != "", "Student name cannot be empty"
        marks = float(input("Enter marks: "))
        if marks < 0 or marks > 100:
            raise InvalidMarksError("Marks must be between 0 and 100")
        with open("student_records.txt", "a") as f:
            f.write(f"{name},{marks}\n")
        print("Record saved successfully")
    except AssertionError as e:
        print("Error:", e)
    except ValueError:
        print("Error: Marks must be numeric")
    except InvalidMarksError as e:
        print("Error:", e)
    finally:
        print("Record processing completed")
    again = input("Do you want to enter another record? (y/n): ").strip().lower()
    if again != "y":
        break


'''
Q60. Insert Sensor Reading into a NumPy Array

Insert a new integer reading at a given position in `[10, 20, 30, 40, 50]`. Validate with `isdigit()` (raise `ValueError`), validate the position (raise `IndexError`), and use try/except/finally.
'''

print('\n===== Q60. Insert Sensor Reading into a NumPy Array =====')
import numpy as np

readings = np.array([10, 20, 30, 40, 50])
print("Original array:", readings)

try:
    position = int(input("Enter insertion position: "))
    element = input("Enter new element: ")
    if not element.isdigit():
        raise ValueError("Only integer digits are allowed")
    if position < 0 or position > len(readings):
        raise IndexError("Invalid insertion position")
    readings = np.insert(readings, position, int(element))
    print("Updated array:", readings)
except ValueError as e:
    print("ValueError:", e)
except IndexError as e:
    print("IndexError:", e)
finally:
    print("Operation completed")


'''
Q61. Precious Metal Loan Management

Write `calculate_interest(metal, purity, amount, tenure)` that determines the interest rate by metal and purity, calculates the interest, handles missing arguments with `TypeError`, invalid metal/purity with `ValueError`, and uses try/except/else/finally. (Interest rates are assumed.)
'''

print('\n===== Q61. Precious Metal Loan Management =====')
def calculate_interest(metal, purity, amount, tenure):
    rates = {
        "gold": {18: 12.0, 22: 10.0, 24: 8.0},
        "silver": {925: 14.0, 950: 13.0, 999: 12.0},
        "platinum": {900: 11.0, 950: 10.0, 999: 9.0},
    }
    metal = metal.lower()
    if metal not in rates:
        raise ValueError(f"Invalid metal type: {metal}")
    purity_value = int(str(purity).upper().replace("K", ""))
    if purity_value not in rates[metal]:
        raise ValueError(f"Unsupported purity {purity} for {metal}")
    rate = rates[metal][purity_value]
    return rate, amount * rate * tenure / 100

cases = [
    ("Missing metal type", lambda: calculate_interest()),
    ("Missing purity", lambda: calculate_interest("gold")),
    ("Missing amount", lambda: calculate_interest("gold", 22)),
    ("Missing tenure", lambda: calculate_interest("gold", 22, 500000)),
    ("Missing multiple arguments", lambda: calculate_interest("silver")),
    ("Invalid metal", lambda: calculate_interest("diamond", 999, 100000, 2)),
    ("Invalid purity", lambda: calculate_interest("gold", 15, 100000, 2)),
    ("Valid", lambda: calculate_interest("gold", 22, 500000, 2)),
]

for title, call in cases:
    print("Case:", title)
    try:
        rate, interest = call()
    except TypeError as e:
        print("TypeError:", e)
    except ValueError as e:
        print("ValueError:", e)
    else:
        print(f"Interest Rate: {rate}%  Interest: {interest}")
    finally:
        print("Loan processing completed")
    print()


'''
Q62. Rat in a Maze Using Backtracking

Find a path for the rat from (0,0) to (N-1,N-1) in an N x N binary maze (1 = open, 0 = blocked) moving up/down/left/right using backtracking. Print the solution path matrix or "No solution exists".
'''

print('\n===== Q62. Rat in a Maze Using Backtracking =====')
def solve_maze(maze):
    n = len(maze)
    path = [[0] * n for _ in range(n)]

    def is_safe(r, c):
        return 0 <= r < n and 0 <= c < n and maze[r][c] == 1 and path[r][c] == 0

    def explore(r, c):
        if not is_safe(r, c):
            return False
        path[r][c] = 1
        if r == n - 1 and c == n - 1:
            return True
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if explore(r + dr, c + dc):
                return True
        path[r][c] = 0
        return False

    if explore(0, 0):
        print("Solution Path:")
        for row in path:
            print(*row)
    else:
        print("No solution exists")

solve_maze([[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]])
print()
solve_maze([[1, 0, 0], [0, 0, 0], [0, 0, 1]])


'''
Q63. Debugging a Coin-Toss Game

Use `breakpoint()` to debug a coin-toss prediction game. At the `(Pdb)` prompt use: `p guess`, `p toss`, `p result`, `p type(guess)`, `n` (next statement), `c` (continue).
'''

print('\n===== Q63. Debugging a Coin-Toss Game =====')
import random

guess = input("Predict heads or tails: ").strip().lower()
toss = random.choice(["heads", "tails"])
breakpoint()
result = toss
if result == guess:
    print("You win! The toss was", result)
else:
    print("You lose! The toss was", result)


'''
Q64. Printer Class and Object Identities

Create a Printer class and three printer objects holding print capacity, color/mono tone and type of printer. Display their object identities. (The question explicitly requires a class.)
'''

print('\n===== Q64. Printer Class and Object Identities =====')
class Printer:
    def __init__(self, print_capacity, tone, printer_type):
        self.print_capacity = print_capacity
        self.tone = tone
        self.printer_type = printer_type

printer1 = Printer(500, "Color", "Inkjet")
printer2 = Printer(1000, "Mono", "Laser")
printer3 = Printer(300, "Color", "Dot Matrix")

for name, p in [("printer1", printer1), ("printer2", printer2), ("printer3", printer3)]:
    print(name, "| id:", id(p), "| capacity:", p.print_capacity, "| tone:", p.tone, "| type:", p.printer_type)


'''
Q65. MovieTicket Class

Create a MovieTicket class with a constructor accepting `movie_name`, `theatre` and `seat_number`. Create three ticket objects. (The question explicitly requires a class.)
'''

print('\n===== Q65. MovieTicket Class =====')
class MovieTicket:
    def __init__(self, movie_name, theatre, seat_number):
        self.movie_name = movie_name
        self.theatre = theatre
        self.seat_number = seat_number

ticket1 = MovieTicket("Inception", "PVR Mysuru", "A1")
ticket2 = MovieTicket("Interstellar", "INOX Mysuru", "B7")
ticket3 = MovieTicket("Dune", "Cinepolis Mysuru", "C12")

for t in (ticket1, ticket2, ticket3):
    print(t.movie_name, "|", t.theatre, "|", t.seat_number)
