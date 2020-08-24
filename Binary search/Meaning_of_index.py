vector = [1,3,5,7,9]
k = 3

l = 0;
r = len(vector) - 1
while l <= r:
    m = (l + r) // 2
    if vector[m] >=k:
        r = m - 1
    else:
        l = m + 1

print(l, vector[l]) # which relative position of L ? if k in vector -> l = index of vector('k') or
                    # appropriate index to enter the list