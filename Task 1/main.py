# -*- codind: uth-8 -*-
import re
from random import choice

with open('cotest.txt') as f:
    stext = f.read()
with open('slovar.txt') as f:
    dict = f.read().split('\n')

text = stext.split('?')
cord = [0]
lastlen = 0
regalf = re.compile(u'[a-zA-Z-]+')

def ces(text, key):
    alf = ''.join([chr(i) for i in range(ord('a'), ord('z')+1)])
    Alf = alf.upper()
    ans = ''
    for i in range(len(text)):
        if (text[i] not in alf) and (text[i] not in Alf):
            ans += text[i]
        elif text[i].isupper():
            ans += Alf[(Alf.index(text[i]) - key)%len(Alf)]
        elif text[i].islower():
            ans += alf[(alf.index(text[i]) - key)%len(alf)]
    return ans

for sent in text:
    if sent.rfind('.') >= 0:
        cord.append(lastlen + sent.rfind('.')+1)
    elif sent.rfind('!') >= 0:
        cord.append(lastlen + sent.rfind('!')+1)
    lastlen += len(sent)+1

pars = [stext[cord[i-1]: cord[i]] for i in range(1, len(cord))]

big_answer = ''
keys = []

for par in pars:
    for key in range(1, 27):
        ans = ces(par, key)
        words = regalf.findall(ans)
        counter = 0
        for i in range(50):
            rand = choice(words)
            if rand in dict:
                counter += 1
        if counter >= 10:
            print(par, key, ans, sep = '\n')
            big_answer += ans + '\n'
            keys.append(key)
            break

with open('ans.txt', 'w') as f:
    f.write(big_answer)
with open('keys.txt', 'w') as f:
    f.write(''.join([str('key' + str(i+1) + ': ' + str(e) + '; ') for i, e in enumerate(keys)]))