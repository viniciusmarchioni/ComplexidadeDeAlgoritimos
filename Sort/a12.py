'''
def fibonacci(n):
    if n== 0 or n == 1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

def fibonacci2(n):
    tb = []
    for i in range(n+1):
        tb.append(0)
    tb[0] = 0
    tb[1] = 1
    for i in range(2,n+1):
        tb[i]=tb[i-1]+tb[i-2]
    return tb[n]

def fibonacci3(n):
    if n== 0 or n == 1:
        return n

    if n not in tb.keys():
        tb[n] = fibonacci3(n-1)+fibonacci3(n-2)

    return tb[n]
tb = {}

print(fibonacci3(45))

'''
def maior(text,text2):
    i = len(text)-1
    j = len(text2) - 1
    return msc(i,j,text,text2)

def msc(i,j,text,text2):
    if i<0 or j<0:
        return ""
    if text[i] == text2[j]:
        return msc(i-1, j-1, text, text2) + text[i]
    else:
        seq1 = msc(i-1,j,text,text2)
        seq2 = msc(i,j-1,text,text2)
        if(len(seq1) > len(seq2)):
            return seq1
        else:
            return seq2

#print(maior("xxxxxxxxace", "yyyyyyyyadcbe"))

def maiorsc(text,text2):
    m = len(text)
    n = len(text2)
    #tb = [m+1][n+1]
    tb = [[0] * (n+1) for x in range(m+1)]

    for i in range(1,m):
        for j in range(1,n):
            if text[i-1] == text2[j-1]:
                tb[i][j] = tb[i-1][j-1]+1
            else:
                tb[i][j] = max(tb[i-1][j],tb[i][j-1])
    
    i = m
    j = n
    seq = ""
    while i>0 and j>0:
        if text[i-1] == text2[j-1]:
            seq += text[i-1]
            i-=1
            j-=1
        elif tb[i-1][j] > tb[i][j-1]:
            i-= 1
        else:
            j-=1
    return seq[::-1]

print(maior("xxxxxxxxxxxxxxxxxace", "yyyyyyyyyyyyyadcbe"))