def solution(dirs):
    answer = 0
    arrow = ['U','D','R','L']
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    pox = 0
    poy =0
    vis = []
    
    for i in range(len(dirs)):
        ind = arrow.index(dirs[i])
        pox += dx[ind]
        poy += dy[ind]
        
        if pox > 5 : 
            pox = 5
            continue
        elif pox < -5 : 
            pox = -5
            continue
        if poy > 5 : 
            poy = 5
            continue
        elif poy < -5 : 
            poy = -5
            continue
        
        
        if [poy, pox, poy-dy[ind], pox-dx[ind]] not in vis:
            if [poy-dy[ind], pox-dx[ind], poy, pox] not in vis:
                vis.append([poy, pox, poy-dy[ind], pox-dx[ind]])
                answer += 1
                print(vis)
        
    return answer