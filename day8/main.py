

list = {}
with open('./input.txt') as f:
    rot = f.readline()
    rot = rot.strip('\n')
    f.readline()
    for x in f.readlines():
        if x.endswith('\n'): x = x.split('\n')[0];
        c = x.split('(')
        c = c[1].split(',')
        a = [c[0],c[1].strip(' )')]
        list[x.split(' ')[0]] = a
print(len(rot))
anser = 0
pos = 'AAA'
while True:
    for x in rot:
        print(pos)
        print(x)
        if x == 'L':
            pos = list[pos][0]
        elif x == 'R':
            pos = list[pos][1]
        anser += 1
        if pos == 'ZZZ': print("ZZZ"); break
    if pos == 'ZZZ': break
print(anser)
