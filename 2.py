
ts = int(input())

for r in range(ts):
    sr = list(input())
    temp = sr

    result = ""
    ary = []
    avl = 0
    for i in temp:
        x = int(i)
        while avl > x:
            ary.append(")")
            avl -= 1
        if avl == 0:
            while x:
                ary.append("(")
                x -= 1
                avl += 1
        if avl < x:
            while x > avl:
                ary.append("(")
                avl += 1
        ary.append(i)
    while(avl):
        ary.append(")")
        avl -= 1
    print("Case #" + str(r + 1) + ":", ''.join(ary))


