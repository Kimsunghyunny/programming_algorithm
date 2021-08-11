def solution(gems):
    
    kind = len(set(gems))
    dic = {gems[0]:1}
    ans = [0, len(gems)-1]
    l, r = 0, 0
    
    while l < len(gems) and r < len(gems):
        if len(dic) == kind:
            if r - l < ans[1] - ans[0]:
                ans = [l, r]
            if dic[gems[l]] == 1:
                del dic[gems[l]]
            else:
                dic[gems[l]] -= 1
            l += 1
        else:
            r += 1
            if r == len(gems):
                break
            if gems[r] in dic.keys():
                dic[gems[r]] += 1
            else:
                dic[gems[r]] = 1
            
    return [ans[0]+1, ans[1]+1]