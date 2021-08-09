def solution(n):
    cases = [0] # shallow copy of the cases (list)
    def dfs(queens, next_queen):
        #print("dfs시작=",queens,next_queen)
        # column check
        # 만약 이미 퀸 자리가 있는 열이라면 제외 (백트래킹)
        if next_queen in queens:
            return

        # diagonal check
        # 대각에 퀸을 자리하게 되는 경우면 제외(백트래킹)
        for row, column in enumerate(queens):
            #print("row,col=",row,column)
            h = len(queens) - row
            if next_queen == column + h or next_queen == column - h:
                #print("대각에 있어서 제외")
                return

        queens.append(next_queen)
        # end check
        # n개까지 모든 퀸을 찾았으면 조건에 맞는 경우를 찾았기 때문에 경우의 수를 더해주고 리턴
        if len(queens) == n:
            cases[0] += 1
            #print("end=",queens)
            return
        #print("dfs재귀시작전",queens[:])
        # 1~n-1개 까지 찾은 경우에 그 이후 퀸이 놓일 수 있는 자리를 찾기 위해서 dfs를 실행
        for next_queen in range(n):
            dfs(queens[:], next_queen) # deep copy of queens

    # 첫째 줄에서의 퀸을 놓을 자리를 for 문을 실행해보며 가능한 경우의 수를 계산한다.
    for next_queen in range(n):
        queens = []
        #print("외부for문에서의=",queens,next_queen)
        dfs(queens, next_queen)
    return cases[0]