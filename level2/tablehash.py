def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x:(x[col-1], -x[0]))
    data = data[row_begin-1:row_end]
    S = []
    for i in data:
        sum = 0
        for j in i:
            sum += j % row_begin
        S.append(sum)
        row_begin +=1
    if len(S) == 1:
        return S[0]
    else:
        answer = S[0]
        for i in range(1, len(S)):
            answer = answer ^ S[i]
       
    return int(answer)


data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]

print(solution(data, 2, 2, 3))