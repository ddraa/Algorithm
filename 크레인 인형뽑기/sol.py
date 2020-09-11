def solution(board, moves):
    answer = 0
    bucket = []
    count = 0
    for i in moves:
        for t in range(len(board)):
            if board[t][i-1] != 0:
                bucket.append(board[t][i-1])
                board[t][i-1] = 0 # del

                # check
                if len(bucket) > 1 and bucket[-1] == bucket[-2]:
                    bucket.pop()
                    bucket.pop()
                    count += 2
                break
    return count

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])