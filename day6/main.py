lines = []
with open('./input.txt','r') as f:
    for line in f.readlines():
        a, line = line.split(':')
        del(a)
        lines.append(line.strip())
def part1():
    time = lines[0].replace(' ', ',')
    dis = lines[1].replace(' ',',')
    time = time.split(',')
    dis = dis.split(',')
    time = [eval(i) for i in time]
    dis = [eval(i) for i in dis]
    anser = 1
    for disnum,x in enumerate(time):
        ways = 0
        for a in range(x+1):
            distens = a*(x-a)
            if distens > dis[disnum]:
                ways +=1
        anser *= ways
    print(anser)


def part2():
    time = lines[0].replace(' ', '')
    dis = lines[1].replace(' ','')
    time = int(time)
    dis = int(dis)
    anser = 1
    ways = 0
    for a in range(time+1):
        distens = a*(time-a)
        if distens > dis:
            ways +=1
    anser *= ways
    print(anser)

if __name__ == "__main__":
    part1()
    part2()
    
