def swap_case(s):
    upper = []
    
    for i,c in enumerate(s):
        if c.isupper():
           upper.append(i)
    l = []
    for i in s:
        l.append(i.upper())
    for i in upper:
        l[i] = l[i].lower()
    s = "".join(l)
    return s

if __name__ == '__main__':
