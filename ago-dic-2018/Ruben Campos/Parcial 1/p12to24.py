def transforma(string):
    s = list(string)
    #AM
    p = "a"
    if p in s:
        for i in range(0,4):
            s.pop()
        if s[0] == "1" and s[1] == "2":
            s[0] = "0"
            s[1] = "0"
            s[3] = "0"
            s[4] = "0"
    #PM
    p = "p"
    if p in s:
        for i in range(0,4):
            s.pop()
        if s[0] == "1" and s[1] == ":":
            s.insert(1, "3")
        if s[0] == "2" and s[1] == ":":
            s[0] = "1"
            s.insert(1, "4")
        if s[0] == "3":
            s[0] = "1"
            s.insert(1, "5")
        if s[0] == "4":
            s[0] = "1"
            s.insert(1, "6")
        if s[0] == "5":
            s[0] = "1"
            s.insert(1, "7")
        if s[0] == "6":
            s[0] = "1"
            s.insert(1, "8")
        if s[0] == "7":
            s[0] = "1"
            s.insert(1, "9")
        if s[0] == "8":
            s[0] = "2"
            s.insert(1, "0")
        if s[0] == "9":
            s[0] = "2"
            s.insert(1, "1")
        if s[0] == "1" and s[1] == "0":
            s[0] = "2"
            s[1] = "2"
        if s[0] == "1" and s[1] == "1":
            s[0] = "2"
            s[1] = "3"
    s.append("h")
    s.append("r")
    s.append("s")

    res = "".join(s)
    return res

string = "2:23p.m."
res = transforma(string)
print(res)
