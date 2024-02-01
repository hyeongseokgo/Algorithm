import numpy as np
def solution(wallpaper):
    # 앞 샾 좌표 리스트, 뒷 샾 좌표 리스트
    sh_list = []
    rsh_list = []
    for i in range(len(wallpaper)):
        # 한 줄에서 앞 # 찾기
        shap = wallpaper[i].find('#')
        rshap = wallpaper[i].rfind('#')
        if shap != -1:
            sh_list.append([i,shap])
            if shap != rshap:
                sh_list.append([i,rshap])
    s = np.array(sh_list).T
    print(np.min(s[0]), np.min(s[1]), np.max(s[0]), np.max(s[1]))
    result = [int(np.min(s[0])), int(np.min(s[1])), int(np.max(s[0]))+1, int(np.max(s[1]))+1]
    return result