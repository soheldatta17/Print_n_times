arr=[]
ar=[]
def printNtimes(a: int) -> None:
    pass
    if a in arr:
        print(*ar[:arr.index(a)+1:])
        return
    if a-1 in arr:
        arr.append(a)
        ar.append("Coding Ninjas")
        arr.sort()
        print(*ar[:arr.index(a)+1:])
        return
    arr.append(a)
    ar.append("Coding Ninjas")
    if a==1:
        arr.sort()
        print(*ar)
        return
    return printNtimes(a-1)