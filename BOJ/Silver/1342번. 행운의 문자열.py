s = input()
 
lucky = set()
visited = [False]*len(s)
 
 
def bt(string):
    if len(string) == len(s):
        lucky.add(string)
        return
    for i in range(len(s)):
        if not visited[i] and (not string or string[-1] != s[i]):
            visited[i] = True
            bt(string+s[i])
            visited[i] = False
 
 
bt('')
print(len(lucky))
