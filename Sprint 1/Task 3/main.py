alf = 'qwertyuiopasdfghjklzxcvbnm_{}1234567890'
text = 'fhke37_kdrjknbmpr_04374j'
key = 'thekey'

key = key * (len(text)//len(key)+1)

ans = ''
for i in range(len(text)):
    ans += alf[(alf.index(text[i])+alf.index(key[i]))%len(alf)]

print(ans)