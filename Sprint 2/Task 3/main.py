with open('program.txt', encoding = 'utf-8') as f:
    line = f.readline()
    d = [line.find('('), line.find(')')]
    line = line[d[0]+1:d[1]]
    vars = line.split(',')
    array = []
    for line in f.readlines():
        if '+=' in line or '==' in line or '-=' in line or '*=' in line or '/=' in line or '**=' in line:
            continue
        elif '=[' in line:
            array.append(line[:line.find('=')].lstrip())
        elif '=' in line:
            vars.append(line[:line.find('=')].lstrip())

with open('program.txt', encoding = 'utf-8') as f:
    text = f.read()

array = list(set(array))
vars = list(set(vars))

for i in range(len(array)):
    text = text.replace(array[i], 'R'+str(i+1))
for i in range(len(vars)):
    text = text.replace(vars[i], 'a'+str(i+1))

print(text)

