with open('slovar.txt') as f:
    text = ''
    for i in f.readlines():
        i = i.split(':')[0]
        text += i + '\n'

with open('slovar.txt', 'w') as f:
    f.write(text)