N = int(input())

prime_flags = [i for i in range(max(4, N + 1))]

prime_flags[0] = prime_flags[1] = None
prime_flags[2], prime_flags[3] = 2, 3

for i in range(2, int(N ** 0.5 + 1)):
    if prime_flags[i] is None:
        continue
    for j in range(i * 2, N + 1, i):
        prime_flags[j] = None
        
prime_nums = []

for i in range(2, N + 1):
    if prime_flags[i] is None:
        continue
    prime_nums.append(i)
    
prime_sums = [0]
for prime in prime_nums:
    prime_sums.append(prime + prime_sums[-1])

start = 0
end = 1
cnt = 0
while start < end and start >= 0 and end < len(prime_sums):
    curr = prime_sums[end] - prime_sums[start]
    
    if curr > N:
        start += 1
        continue
    if curr < N:
        end += 1
        continue
    
    cnt, start, end = cnt + 1, start + 1, end + 1
    
print(cnt)