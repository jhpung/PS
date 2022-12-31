import sys
input = sys.stdin.readline

N = int(input())

t1 = 0
t2 = 0
t1_time = 0
t2_time = 0

prev = 0

def to_time(i):
  minute = i // 60
  second = i % 60

  return '{:02d}:{:02d}'.format(minute, second)


def to_int(time):
  minute, second = map(int,time.split(':'))

  return minute * 60 + second

for i in range(N):
  team, time = input().split()

  curr = to_int(time)
  diff = curr - prev

  if t1 > t2:
    t1_time += diff
  if t2 > t1:
    t2_time += diff

  if team == '1':
    t1 += 1
  if team == '2':
    t2 += 1
  
  prev = curr

if t1 > t2:
  t1_time += to_int('48:00') - prev
if t2 > t1:
  t2_time += to_int('48:00') - prev

print(to_time(t1_time))
print(to_time(t2_time))