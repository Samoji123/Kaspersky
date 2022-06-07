a = input('Укажите путь к файлу: ')
with open(a, 'rb') as f:
    text = f.read()
    text = text[:2]
    flag = False
    if text == b'MZ':
        flag = True

if flag:
    print('file is executable')
else:
    print('file is not executable')

