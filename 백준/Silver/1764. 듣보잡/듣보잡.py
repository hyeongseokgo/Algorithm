

n, m = map(int, input().split())

hear = set()
for _ in range(n):
    hear.add(input())
see = set()
for _ in range(m):
    see.add(input())

result = sorted(hear & see)

print(len(result))
print('\n'.join(result))