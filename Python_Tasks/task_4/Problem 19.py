# Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem
n = int(input())
arr = list(map(int, input().split()))

unique_scores = set(arr)
unique_scores.remove(max(unique_scores))

print(max(unique_scores))
