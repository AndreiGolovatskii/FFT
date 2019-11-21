def tr(arr, k):
  arr.sort()
  ans = sum(arr)
  k = min(k, len(arr) - 1)
  for i in range(k):
    if arr[i] < 0:
      ans -= arr[i]
  return ans
  
def sol():
  n, k = map(int, input().split())
  arr = list(map(int, input().split()))
  ans = arr[0]
  for i in range(n):
    for j in range(i + 1, n + 1):
      ans = max(ans, tr(arr[i:j], k))
  for i in range(n):
    for j in range(n - 1, i - 1, -1):
      ans = max(ans, tr(arr[0:i] + arr[n - 1:j:-1], k))
  print(ans)

t = int(input())
for i in range(t):
  sol()
