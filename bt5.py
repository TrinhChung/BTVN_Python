
def bt5Run():
    lst = []
    print("Nhap day so")
    while True:
        lst = list(map(int, input().split()))
        if ((len(lst) + 1 > lst[0]) and len(lst) > 1):
            break;
        else:
            print("Day so khong dung dinh dang!")
            continue;

    count = [0]*lst[0];
    ddict = {}
    for i in range(1, lst[0] + 1):
        if (lst[i] in ddict):
            ddict[lst[i]] += 1;
        else:
            ddict[lst[i]] = 1;

    print(ddict)

