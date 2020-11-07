def solution(grades, weights, threshold):

    score = {"A+": 10, "A0": 9, "B+": 8, "B0": 7, "C+": 6,
             "C0": 5, "D+": 4, "D0": 3, "F": 0}
    total = 0
    for grade, weight in zip(grades, weights):
        total += score[grade] * weight

    return total - threshold

print(solution(["B+","A0","C+"]	, [6,7,8]	,200))