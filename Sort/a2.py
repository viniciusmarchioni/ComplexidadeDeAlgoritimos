def sort(v, n):
    for i in range(n):
        chave = v[i]
        j=i-1
        while j>0 and v[j]>chave:
            v[j+1]=v[j]
            j = j - 1
        v[j + 1] = chave