message = '23|8|1|20|4|15|25|15|21|11|14|15|23|1|2|15|21|20|1|2|3'.split('|')
alf = ''.join([chr(i) for i in range(ord('a'), ord('z')+1)])
ans = [alf[int(i)] for i in message]
print(''.join([str(i) for i in ans]))