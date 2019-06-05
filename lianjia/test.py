import re
def switchstr(s):
    s = s.split('-')
    s[0] = s[0].replace('h','H')
    s[1] = s[1].replace('w','W')
    s = ''.join(s)
    return s
print(switchstr('hello-world'))
