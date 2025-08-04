def solution(k, dungeons):
    n = len(dungeons)
    vis = [False]* n
    ma = []
    def dfs(num, hp, time):
        if len(num) == n:
            ma.append(time)
            return
        
        for i in range(n):
            if not vis[i]:
                vis[i] = True
                a, b = dungeons[i]
                if a <= hp:
                    dfs(num + [dungeons[i]], hp-b, time+1)
                else:
                    dfs(num + [dungeons[i]], hp, time)
                vis[i] = False
    dfs([], k, 0)
    return max(ma)