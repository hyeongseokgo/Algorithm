pado = [1, 1, 1, 2, 2]

for i in range(4, 101):
    pado.append(pado[i]+pado[i-4])

time = int(input())
for _ in range(time):
    n = int(input())
    print(pado[n-1])