
web , solve = map(int, input().split())

web_pass = {}

for _ in range(web):
    a, b = input().split()
    web_pass[a] = b

for _ in range(solve):
    print(web_pass[input()])