def running_sum(L):
    for i in range(1,len(L)):
        L[i] = L[i -1] + L[i]
