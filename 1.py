import numpy as np

ts = int(input())

for i in range(ts):
    ms = int(input())

    mtrx = [[] * 3] * 3
    mtrx = np.zeros((ms, ms))
   
    cR = 0
    cC = 0
   
    for j in range(ms):
        sr = input().split(" ")
        rd = []
        for k in sr:
            if k in rd:
                cR += 1
                break
            rd.append(k)
       
        for k in range(len(sr)):
            mtrx[k][j] = sr[k]
   
    for j in mtrx:
        rd = []
        for k in j:
            if k in rd:
                cC += 1
                break
            rd.append(k)

    print("Case #" + str(i + 1) + ":", int(mtrx.trace()) ,cR, cC)
