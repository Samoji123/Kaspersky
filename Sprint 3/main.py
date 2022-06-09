class virys():
    def __init__(self):
        self.status = False
        self.timer = 0

n = int(input())
k = int(input())
files = [virys()]

for hours in range(n):
    for v in files:
        if v.status:
            [files.append(virys()) for i in range(k)]
        elif not v.status and v.timer == 1:
            v.status = True
        v.timer += 1

print(len(files))