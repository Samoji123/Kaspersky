with open('prog.txt', encoding='utf-8') as f:
    text = f.read()
    text = text[:2]
    flag = False
    if text == 'MZ':
        flag = True

if flag:
    print('file is executable')
else:
    print('file is not executable')

