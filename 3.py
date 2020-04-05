def int_sct(x, y):
    if x[0] > y[0] and x[0] < y[1]:
        return True
    if x[1] > y[0] and x[1] < y[1]:
        return True
    return False

def int_sctR(x, y):
    return int_sct(x, y) or int_sct(y, x) or x[0] == y[0] or x[1] == y[1]

ts = int(input())

for r in range(ts):
    N = int(input())

    ary = []
    for i in range(N):
        s = input().split(" ")
        data = (int(s[0]), int(s[1]), i)
        ary.append(data)

    orig = ary
    ary.sort(key=lambda x: x[0])
    print("Case #" + str(r + 1) + ": ", end='')
   
    aryj = []
    aryc = []
    p = q = 0
    pb = True
    for i in range(len(ary)):
        if ary[i][0] >= p:
            aryj.append(ary[i][2])
            p = ary[i][1]
        else:
            if ary[i][0] >= q:
                aryc.append(ary[i][2])
                q = ary[i][1]
            else:
                pb = False
                break
    
    if not pb:
        print("IMPOSSIBLE")
    else:
        temp = [0] * len(ary)
        for i in aryj:
            temp[i] = "J"
        for i in aryc:
            temp[i] = "C"
        print(''.join(temp))