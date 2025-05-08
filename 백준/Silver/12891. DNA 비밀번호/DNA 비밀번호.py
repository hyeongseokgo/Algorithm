import sys
input = sys.stdin.readline

dna_l , part = map(int, input().split())
dna = input()
cnt = 0

pa, pc, pg, pt = map(int, input().split())

current = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in range(part):
    current[dna[i]] += 1

if pa <= current['A'] and pc <= current['C'] and pg <= current['G'] and pt <= current['T']:
    cnt += 1



for i in range(1, dna_l - part + 1):
    current[dna[i-1]] -= 1
    current[dna[i+part-1]] += 1
    if pa <= current['A'] and pc <= current['C'] and pg <= current['G'] and pt <= current['T']:
        cnt += 1

print(cnt)