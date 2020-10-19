def solution(boxes):
    answer = -1

    box = []
    length = len(boxes)
    for i in boxes:
        for j in i:
            box.append(j)
    box.sort()

    k = 0
    count = 0
    while k<len(box) - 1:
        if box[k] == box[k+1]:
            count += 1
            k += 1
        k += 1

    return length - count

solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]])