def findSubstring( s, words) :

    l = len(words[0])
    total = l * len(words)
    limit = len(s)
    for word in words:
        s = s.replace(word,"4"*len(word))
    ans = []
    i = 0
    while True:
        if i >= limit:
            break
        if s[i] =="4":
            ans.append(i)
            i += total
        i += 1
    return ans

