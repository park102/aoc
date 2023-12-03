with open("./input.txt") as f:
    file =f.read()
file = file.split('\n')
cubes = {'red':12,'green':13,'blue':14}
def part1():
    anser = 0
    for x in file:
        valid = True
        if x == '': break;
        id = int(x.split(':',1)[0].split(" ")[1])
        games = x.split(":")[1]
        game = games.split(';')
        for x in game:
            cube = x.split(',')
            for x in cube:
                coler = x.split(' ')[2]
                num = x.split(' ')[1]
                if cubes[coler] < int(num):
                    valid = False
                    break
            if valid == False:
                break
        if valid == True:
            anser += id
    print(anser)
def part2():
    anser = 0
    for x in file:
        lest = {'red':0,'green':0,'blue':0}
        valid = True
        if x == '': break;
        id = int(x.split(':',1)[0].split(" ")[1])
        games = x.split(":")[1]
        game = games.split(';')
        for x in game:
            cube = x.split(',')
            for x in cube:
                coler = x.split(" ")[2]
                num = int(x.split(" ")[1])
                if lest[coler] < num:
                    lest[coler] = num
        print(lest)
        anser += lest['red'] * lest["green"] * lest["blue"]
        print(anser)

if __name__ == "__main__":
#    part1()
    part2()
