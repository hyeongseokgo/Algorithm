num, money = map(int, input().split())

m_type = []

for _ in range(num):
    m_type.append(int(input()))

m_type.sort(reverse=True)

result = 0
for i in range(num):
    if m_type[i] <= money:
        result += money//m_type[i]
        money -= (money//m_type[i])*m_type[i]

print(result)